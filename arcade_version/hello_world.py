import arcade

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Hello World - Arcade Version"

class HelloWorldGame(arcade.Window):
    """Main application class."""

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """Set up the game. Called once when the program starts."""
        pass  # Nothing to set up for a simple hello world

    def on_draw(self):
        """Render the screen."""
        
        # Clear the screen
        self.clear()
        
        # Draw the text
        arcade.draw_text(
            "Hello World!",
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            arcade.color.WHITE,
            64,
            anchor_x="center",
            anchor_y="center"
        )

def main():
    """Main function"""
    window = HelloWorldGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main() 