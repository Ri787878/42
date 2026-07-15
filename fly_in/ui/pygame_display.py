from io import BytesIO
import base64
import json
from pathlib import Path
import sys

import pygame

from zone_network import Zone_Network, Hub
from drones import build_drone


def load_drone_sprite() -> pygame.Surface:
    piskel_path = (
        Path(__file__).resolve().parent.parent
        / "sprites"
        / "drone.piskel"
    )
    raw = json.loads(piskel_path.read_text(encoding="utf-8"))

    layer_data = json.loads(raw["piskel"]["layers"][0])
    frame_data = layer_data["chunks"][0]["base64PNG"]
    encoded_png = frame_data.split(",", 1)[1]

    sprite_bytes = base64.b64decode(encoded_png)
    sprite = pygame.image.load(BytesIO(sprite_bytes)).convert_alpha()
    return pygame.transform.smoothscale(sprite, (68, 68))


def draw_step_counter(
    screen: pygame.Surface,
    font: pygame.font.Font,
    step_number: int,
    total_steps: int,
) -> None:
    label = font.render(f"Step {step_number} / {total_steps}",
                        True,
                        (255, 255, 255))
    label_rect = label.get_rect(topright=(screen.get_width() - 20, 20))

    box_rect = label_rect.inflate(14, 10)
    box = pygame.Surface(box_rect.size, pygame.SRCALPHA)
    box.fill((15, 15, 20, 180))

    screen.blit(box, box_rect.topleft)
    pygame.draw.rect(screen, (255, 215, 0), box_rect, 1, border_radius=6)
    screen.blit(label, label_rect)


def start_display(network: Zone_Network, route: list[Hub]) -> None:
    pygame.init()
    pygame.font.init()

    WIDTH, HEIGHT = 1500, 800
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Zone Network Visualizer")
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.SysFont("Arial", 14)

    BG_COLOR = (30, 30, 40)
    LINE_COLOR = (180, 180, 180)
    ROUTE_COLOR = (255, 215, 0)
    START_COLOR = (50, 205, 50)
    END_COLOR = (220, 20, 60)
    HUB_COLOR = (70, 130, 180)

    nodes = [network.start_hub, network.end_hub, *network.hubs]
    min_x = min(node.x_coord for node in nodes)
    max_x = max(node.x_coord for node in nodes)
    min_y = min(node.y_coord for node in nodes)
    max_y = max(node.y_coord for node in nodes)

    margin = 70
    span_x = max(1, max_x - min_x)
    span_y = max(1, max_y - min_y)

    cell_size = min(
        (WIDTH - 2 * margin) / span_x,
        (HEIGHT - 2 * margin) / span_y,
    )
    cell_size = max(150, int(cell_size))

    content_width = max(WIDTH, int(span_x * cell_size + (2 * margin)))
    content_height = max(HEIGHT, int(span_y * cell_size + (2 * margin)))

    world_surface = pygame.Surface((content_width, content_height))

    offset_x = margin - min_x * cell_size
    offset_y = margin - min_y * cell_size

    camera_x = 0
    camera_y = 0
    zoom_level = 1.0

    def world_to_screen(world_x: float, world_y: float) -> tuple[int, int]:
        screen_x = int(offset_x + world_x * cell_size)
        screen_y = int(content_height - (offset_y + world_y * cell_size))
        return screen_x, screen_y

    def get_node_style(node: Hub) -> tuple[tuple[int, int, int], str]:
        if node.name == network.start_hub.name:
            return START_COLOR, " (Start)"
        if node.name == network.end_hub.name:
            return END_COLOR, " (Goal)"
        return HUB_COLOR, ""

    def draw_route(
         surface: pygame.Surface,
         path: list[Hub],
         color: tuple[int, int, int]) -> None:
        if len(path) < 2:
            return

        for start_hub, end_hub in zip(path, path[1:]):
            pygame.draw.line(
                surface,
                color,
                world_to_screen(start_hub.x_coord, start_hub.y_coord),
                world_to_screen(end_hub.x_coord, end_hub.y_coord),
                4,
            )

    def draw_drone(
         surface: pygame.Surface,
         position: tuple[int, int],
         sprite: pygame.Surface) -> None:
        rect = sprite.get_rect(center=position)
        surface.blit(sprite, rect)

    def route_position(
         path: list[Hub],
         segment_index: int,
         progress: float) -> tuple[float, float]:
        if len(path) == 1:
            hub = path[0]
            return float(hub.x_coord), float(hub.y_coord)

        if segment_index >= len(path) - 1:
            hub = path[-1]
            return float(hub.x_coord), float(hub.y_coord)

        start_hub = path[segment_index]
        end_hub = path[segment_index + 1]

        x = (start_hub.x_coord + (end_hub.x_coord - start_hub.x_coord)
             * progress)
        y = (start_hub.y_coord + (end_hub.y_coord - start_hub.y_coord)
             * progress)
        return float(x), float(y)

    drone = build_drone(network, route)
    drone_sprite = load_drone_sprite()

    STEP_DURATION_MS = 1000
    current_segment = 0
    segment_progress = 0.0

    running = True
    while running:
        dt = CLOCK.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    zoom_level = min(4.0, zoom_level + 0.1)
                elif event.button == 5:
                    min_zoom_x = WIDTH / content_width
                    min_zoom_y = HEIGHT / content_height
                    absolute_min_zoom = max(0.1, max(min_zoom_x, min_zoom_y))
                    zoom_level = max(absolute_min_zoom, zoom_level - 0.1)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            camera_x -= 10
        if keys[pygame.K_RIGHT]:
            camera_x += 10
        if keys[pygame.K_UP]:
            camera_y -= 10
        if keys[pygame.K_DOWN]:
            camera_y += 10

        if len(route) > 1 and current_segment < len(route) - 1:
            segment_progress += dt / STEP_DURATION_MS
            if segment_progress >= 1.0:
                segment_progress = 0.0
                current_segment += 1
                drone.advance()

        world_surface.fill(BG_COLOR)

        hub_lookup = {
            node.name: world_to_screen(node.x_coord, node.y_coord)
            for node in nodes
        }

        for left_name, right_name in network.connection:
            if left_name in hub_lookup and right_name in hub_lookup:
                pygame.draw.line(
                    world_surface,
                    LINE_COLOR,
                    hub_lookup[left_name],
                    hub_lookup[right_name],
                    3,
                )

        draw_route(world_surface, route, ROUTE_COLOR)

        for node in nodes:
            pos = world_to_screen(node.x_coord, node.y_coord)
            node_color, _ = get_node_style(node)
            pygame.draw.circle(world_surface, node_color, pos, 16)
            pygame.draw.circle(world_surface, (20, 20, 20), pos, 12)
            pygame.draw.circle(world_surface, node_color, pos, 6)

        for node in nodes:
            pos = world_to_screen(node.x_coord, node.y_coord)
            node_color, _ = get_node_style(node)
            text_surface = FONT.render(node.name, True, node_color)
            text_rect = text_surface.get_rect(center=(pos[0], pos[1] - 28))
            bg_rect = text_rect.inflate(6, 4)
            pygame.draw.rect(
                world_surface,
                (20, 20, 25),
                bg_rect,
                border_radius=4)
            world_surface.blit(text_surface, text_rect)

        drone_x, drone_y = route_position(
            route,
            current_segment,
            segment_progress)
        draw_drone(
            world_surface,
            world_to_screen(drone_x, drone_y),
            drone_sprite)

        SCREEN.fill((0, 0, 0))

        visible_width = int(WIDTH / zoom_level)
        visible_height = int(HEIGHT / zoom_level)
        camera_rect = pygame.Rect(
            camera_x,
            camera_y,
            visible_width,
            visible_height,
        )

        camera_rect.clamp_ip(world_surface.get_rect())

        sub_surface = world_surface.subsurface(camera_rect)
        scaled_surface = pygame.transform.smoothscale(
            sub_surface,
            (WIDTH, HEIGHT),
        )

        SCREEN.blit(scaled_surface, (0, 0))

        total_steps = max(len(route) - 1, 1)
        visible_step = min(current_segment + 1, total_steps)
        draw_step_counter(SCREEN, FONT, visible_step, total_steps)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
