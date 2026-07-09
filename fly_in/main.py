from zone_network import Zone_Network, InvalidConfiguration, Hub
from pydantic import ValidationError
import sys
import pygame


def main() -> None:

    try:
        """start_hub = Hub(
            name="start",
            x_coord=0,
            y_coord=0,
            metadata=["color=green"]
        )"""

        if len(sys.argv) != 2:
            print("[ERROR] No valid map was issued.")
            sys.exit(1)

        network = Zone_Network.from_file(sys.argv[1])

        # Access attributes cleanly via dot notation instead of dict keys
        # print(f"nb_drones: {network.nb_drones}")
        # print(f"Start hub has conf: {network.start_hub}")
        # print(f"End hub has conf: {network.end_hub}")

        # for h in network.hub:
        #     print(f"This hub has conf: {h}")

        # print(f"{network.connection}")

        start_display(network)

    except (InvalidConfiguration, ValidationError) as e:
        print(f"Configuration Error: {e}")
        sys.exit(1)


def start_display(network: Zone_Network) -> None:
    pygame.init()
    pygame.font.init()

    WIDTH, HEIGHT = 800, 600
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Zone Network Visualizer")
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.SysFont("Arial", 14)

    BG_COLOR = (30, 30, 40)
    LINE_COLOR = (180, 180, 180)
    TEXT_COLOR = (255, 255, 255)
    START_COLOR = (50, 205, 50)
    END_COLOR = (220, 20, 60)
    HUB_COLOR = (70, 130, 180)

    nodes = [network.start_hub, network.end_hub, *network.hub]
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
    cell_size = max(30, int(cell_size))

    content_width = max(WIDTH, int(span_x * cell_size + (2 * margin)))
    content_height = max(HEIGHT, int(span_y * cell_size + (2 * margin)))

    world_surface = pygame.Surface((content_width, content_height))

    offset_x = margin - min_x * cell_size
    offset_y = margin - min_y * cell_size

    # Camera and Zoom settings
    camera_x = 0
    camera_y = 0
    zoom_level = 1.0

    def world_to_screen(world_x: int, world_y: int) -> tuple[int, int]:
        screen_x = int(offset_x + world_x * cell_size)
        screen_y = int(content_height - (offset_y + world_y * cell_size))
        return screen_x, screen_y

    def get_node_style(node: Hub) -> tuple[tuple[int, int, int], str]:
        if node.name == network.start_hub.name:
            return START_COLOR, " (Start)"
        if node.name == network.end_hub.name:
            return END_COLOR, " (Goal)"
        return HUB_COLOR, ""

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    zoom_level = min(4.0, zoom_level + 0.1)
                elif event.button == 5:
                    min_zoom_x = WIDTH / content_width
                    min_zoom_y = HEIGHT / content_height
                    absolute_min_zoom = max(0.2, max(min_zoom_x, min_zoom_y))
                    zoom_level = max(absolute_min_zoom, zoom_level - 0.1)

        # Keyboard panning controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            camera_x -= 10
        if keys[pygame.K_RIGHT]:
            camera_x += 10
        if keys[pygame.K_UP]:
            camera_y -= 10
        if keys[pygame.K_DOWN]:
            camera_y += 10

        world_surface.fill(BG_COLOR)

        hub_lookup = {
            node.name: world_to_screen(node.x_coord, node.y_coord)
            for node in nodes
        }

        for start_name, end_name in network.connection:
            if start_name in hub_lookup and end_name in hub_lookup:
                pygame.draw.line(
                    world_surface,
                    LINE_COLOR,
                    hub_lookup[start_name],
                    hub_lookup[end_name],
                    3,
                )

        # Draw Connections Between Hubs and labels
        for node in nodes:
            pos: tuple[int, int] = world_to_screen(node.x_coord, node.y_coord)
            node_color, label_suffix = get_node_style(node)

            pygame.draw.circle(world_surface, node_color, pos, 16)
            pygame.draw.circle(world_surface, (20, 20, 20), pos, 12)
            pygame.draw.circle(world_surface, node_color, pos, 6)

            text_surface = FONT.render(
                f"{node.name}{label_suffix}",
                True,
                TEXT_COLOR,
            )
            text_rect = text_surface.get_rect(center=(pos[0], pos[1] - 26))
            SCREEN.blit(text_surface, text_rect)
            world_surface.blit(text_surface, text_rect)

        SCREEN.fill((0, 0, 0))
        visible_width = int(WIDTH / zoom_level)
        visible_height = int(HEIGHT / zoom_level)
        camera_rect = pygame.Rect(
            camera_x,
            camera_y,
            visible_width,
            visible_height
            )

        # Keep camera bounded within world boundaries
        camera_rect.clamp_ip(world_surface.get_rect())

        # Grab the visible camera patch and stretch/shrink it to fit window
        sub_surface = world_surface.subsurface(camera_rect)
        scaled_surface = pygame.transform.smoothscale(
            sub_surface,
            (WIDTH, HEIGHT)
            )

        SCREEN.blit(scaled_surface, (0, 0))
        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
    # start_display()
