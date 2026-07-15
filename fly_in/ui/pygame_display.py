from io import BytesIO
import base64
import json
from pathlib import Path
import sys

import pygame

from drones import Drone
from hub import Hub
from zone_network import Zone_Network


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
    return pygame.transform.smoothscale(sprite, (34, 34))


def draw_step_counter(
    screen: pygame.Surface,
    font: pygame.font.Font,
    step_number: int,
    total_steps: int,
) -> None:
    label = font.render(
        f"Step {step_number} / {total_steps}",
        True,
        (255, 255, 255),
    )
    label_rect = label.get_rect(topright=(screen.get_width() - 20, 20))

    box_rect = label_rect.inflate(14, 10)
    box = pygame.Surface(box_rect.size, pygame.SRCALPHA)
    box.fill((15, 15, 20, 180))

    screen.blit(box, box_rect.topleft)
    pygame.draw.rect(screen, (255, 215, 0), box_rect, 1, border_radius=6)
    screen.blit(label, label_rect)


def start_display(network: Zone_Network, drones: list[Drone]) -> None:
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

    def all_drones_arrived(drones: list[Drone]) -> bool:
        return all(
            drone.current_hub.name == drone.planned_path[-1].name
            for drone in drones
        )

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
        route: list[Hub],
        color: tuple[int, int, int],
    ) -> None:
        if len(route) < 2:
            return

        for start_hub, end_hub in zip(route, route[1:]):
            pygame.draw.line(
                surface,
                color,
                world_to_screen(start_hub.x_coord, start_hub.y_coord),
                world_to_screen(end_hub.x_coord, end_hub.y_coord),
                4,
            )

    def route_position(
        route: list[Hub],
        segment_index: int,
        progress: float,
    ) -> tuple[float, float]:
        if len(route) == 1:
            hub = route[0]
            return float(hub.x_coord), float(hub.y_coord)

        if segment_index >= len(route) - 1:
            hub = route[-1]
            return float(hub.x_coord), float(hub.y_coord)

        start_hub = route[segment_index]
        end_hub = route[segment_index + 1]

        dx = end_hub.x_coord - start_hub.x_coord
        dy = end_hub.y_coord - start_hub.y_coord
        x = start_hub.x_coord + dx * progress
        y = start_hub.y_coord + dy * progress
        return float(x), float(y)

    def draw_drone(
        surface: pygame.Surface,
        position: tuple[int, int],
        sprite: pygame.Surface,
    ) -> None:
        rect = sprite.get_rect(center=position)
        surface.blit(sprite, rect)

    drone_sprite = load_drone_sprite()

    DRONE_STEP_MS = 1000
    DRONE_START_DELAY_MS = 220

    drone_segments = [0 for _ in drones]
    drone_progress = [0.0 for _ in drones]
    drone_timers = [
        index * DRONE_START_DELAY_MS for index in range(len(drones))
    ]

    simulation_step = 1

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

        for index, drone in enumerate(drones):
            path = drone.planned_path
            if len(path) < 2:
                continue

            drone_timers[index] += dt

            while (
                drone_timers[index] >= DRONE_STEP_MS
                and drone_segments[index] < len(path) - 1
            ):
                drone_timers[index] -= DRONE_STEP_MS
                drone_segments[index] += 1
                drone.current_hub = path[drone_segments[index]]
                drone.next_step_index = min(
                    drone_segments[index] + 1,
                    len(path) - 1,
                )

            if drone_segments[index] >= len(path) - 1:
                drone_progress[index] = 1.0
            else:
                drone_progress[index] = drone_timers[index] / DRONE_STEP_MS

        if not all_drones_arrived(drones):
            active_steps = [
                drone.next_step_index
                for drone in drones
                if drone.planned_path
            ]
            simulation_step = max(active_steps) if active_steps else 1

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

        for drone in drones:
            draw_route(world_surface, drone.planned_path, ROUTE_COLOR)

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
                border_radius=4,
            )
            world_surface.blit(text_surface, text_rect)

        for index, drone in enumerate(drones):
            path = drone.planned_path
            if not path:
                continue

            x, y = route_position(
                path,
                drone_segments[index],
                drone_progress[index],
            )
            screen_pos = world_to_screen(x, y)

            offset = index * 4
            screen_pos = (screen_pos[0] + offset, screen_pos[1] + offset)
            draw_drone(world_surface, screen_pos, drone_sprite)

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
        total_steps = max(
            (len(drone.planned_path) - 1 for drone in drones if drone.planned_path),
            default=1,
        )
        draw_step_counter(
            SCREEN,
            FONT,
            min(simulation_step, total_steps),
            total_steps,
        )
        pygame.display.flip()

    pygame.quit()
    sys.exit()
