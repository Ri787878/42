from zone_network import Zone_Network, InvalidConfiguration
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
    SMALL_FONT = pygame.font.SysFont("Arial", 12)

    BG_COLOR = (30, 30, 40)
    GRID_COLOR = (55, 55, 70)
    AXIS_COLOR = (95, 95, 120)
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

    content_width = span_x * cell_size
    content_height = span_y * cell_size
    offset_x = (WIDTH - content_width) / 2 - min_x * cell_size
    offset_y = (HEIGHT - content_height) / 2 - min_y * cell_size

    def world_to_screen(world_x: int, world_y: int) -> tuple[int, int]:
        screen_x = int(offset_x + world_x * cell_size)
        screen_y = int(HEIGHT - (offset_y + world_y * cell_size))
        return screen_x, screen_y

    def get_node_style(node: object) -> tuple[tuple[int, int, int], str]:
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

        SCREEN.fill(BG_COLOR)

        hub_lookup = {
            node.name: world_to_screen(node.x_coord, node.y_coord)
            for node in nodes
        }

        for start_name, end_name in network.connection:
            if start_name in hub_lookup and end_name in hub_lookup:
                pygame.draw.line(
                    SCREEN,
                    LINE_COLOR,
                    hub_lookup[start_name],
                    hub_lookup[end_name],
                    3,
                )

        for node in nodes:
            pos = world_to_screen(node.x_coord, node.y_coord)
            node_color, label_suffix = get_node_style(node)

            pygame.draw.circle(SCREEN, node_color, pos, 16)
            pygame.draw.circle(SCREEN, (20, 20, 20), pos, 12)
            pygame.draw.circle(SCREEN, node_color, pos, 6)

            text_surface = FONT.render(
                f"{node.name}{label_suffix} ({node.x_coord}, {node.y_coord})",
                True,
                TEXT_COLOR,
            )
            text_rect = text_surface.get_rect(center=(pos[0], pos[1] - 26))
            SCREEN.blit(text_surface, text_rect)

        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
    # start_display()
