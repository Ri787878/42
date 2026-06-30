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

    # Constants
    WIDTH, HEIGHT = 800, 600
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Zone Network Visualizer")
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.SysFont("Arial", 14)

    # --- Fixed Camera State ---
    zoom_scale = 1.0
    pan_x = 0.0
    pan_y = 0.0
    is_dragging = False
    drag_start_x, drag_start_y = 0, 0

    def world_to_screen(world_x, world_y):
        """Transforms raw Hub coordinates to screen space based on zoom and pan."""
        # Scale from the center of the screen to make zooming feel natural
        screen_x = (world_x - WIDTH // 2) * zoom_scale + WIDTH // 2 + pan_x
        screen_y = (world_y - HEIGHT // 2) * zoom_scale + HEIGHT // 2 + pan_y
        return int(screen_x), int(screen_y)
    
    def reset_camera_to_network():
        """Calculates the center of all hubs and centers the camera on them."""
        global zoom_scale, pan_x, pan_y
        if not network.hub:
            return
        # Find the middle point of your network bounding box
        all_x = [h.x_coord for h in network.hub]
        all_y = [h.y_coord for h in network.hub]
        
        avg_x = sum(all_x) / len(all_x)
        avg_y = sum(all_y) / len(all_y)
        
        # Reset values
        zoom_scale = 1.0
        # Offset the pan so that the average coordinate lands precisely in the center of the screen
        pan_x = -avg_x
        pan_y = -avg_y
    
    # Run auto-center once at startup
    reset_camera_to_network()

    # Color Palette
    BG_COLOR = (30, 30, 40)       # Dark slate
    LINE_COLOR = (150, 150, 150)   # Light gray for connections
    TEXT_COLOR = (255, 255, 255)   # White for labels
    START_COLOR = (50, 205, 50)    # Lime Green
    END_COLOR = (220, 20, 60)      # Crimson
    HUB_COLOR = (70, 130, 180)     # Steel Blue

    # Create a quick lookup dictionary to find Hub coordinates by their names
    hub_lookup = {h.name: (h.x_coord, h.y_coord) for h in network.hub}

    running = True
    while running:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        SCREEN.fill(BG_COLOR)

        # --- Draw Connections (Lines) ---
        for start_name, end_name in network.connection:
            if start_name in hub_lookup and end_name in hub_lookup:
                start_pos = hub_lookup[start_name]
                end_pos = hub_lookup[end_name]
                pygame.draw.line(SCREEN, LINE_COLOR, start_pos, end_pos, 3)

        # --- Draw Hubs (Nodes) ---
        for h in network.hub:
            pos = (h.x_coord, h.y_coord)

            # Color code hubs based on their role
            if h.name == network.start_hub.name:
                node_color = START_COLOR
                label_suffix = " (Start)"
            elif h.name == network.end_hub.name:
                node_color = END_COLOR
                label_suffix = " (Goal)"
            else:
                node_color = HUB_COLOR
                label_suffix = ""

            # Draw the outer ring and filled center for the hub
            pygame.draw.circle(SCREEN, node_color, pos, 16)
            pygame.draw.circle(SCREEN, (20, 20, 20), pos, 12)  # Hollow center effect
            pygame.draw.circle(SCREEN, node_color, pos, 6)

            # Render and draw Text Label
            text_surface = FONT.render(f"{h.name}{label_suffix}", True, TEXT_COLOR)
            # Position text slightly above the hub node
            text_rect = text_surface.get_rect(center=(h.x_coord, h.y_coord - 25))
            SCREEN.blit(text_surface, text_rect)

        # Update display
        pygame.display.flip()
        CLOCK.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
    # start_display()