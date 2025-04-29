import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CIRCLE_RADIUS = 50
CIRCLE_COLOR = arcade.color.RED
BG_COLOR = arcade.color.WHITE
TEXT_COLOR = arcade.color.BLUE
SCREEN_TITLE = "Click the Circle to Win - Arcade"

class CircleGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(BG_COLOR)
        
        # Circle position (center of the screen)
        self.circle_x = SCREEN_WIDTH // 2
        self.circle_y = SCREEN_HEIGHT // 2
        
        # Game state
        self.game_won = False

    def on_draw(self):
        """Render the screen"""
        arcade.start_render()
        
        # Draw the circle
        arcade.draw_circle_filled(self.circle_x, self.circle_y, CIRCLE_RADIUS, CIRCLE_COLOR)
        
        # If game is won, display the win message
        if self.game_won:
            arcade.draw_text("You Win!", SCREEN_WIDTH//2, 100, 
                            TEXT_COLOR, 64, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        """Called when the mouse button is pressed"""
        if not self.game_won:
            # Calculate distance between mouse click and circle center
            distance = ((x - self.circle_x) ** 2 + (y - self.circle_y) ** 2) ** 0.5
            
            # Check if click is within the circle
            if distance <= CIRCLE_RADIUS:
                self.game_won = True

def main():
    """ Main function """
    game = CircleGame()
    arcade.run()

if __name__ == "__main__":
    main() 