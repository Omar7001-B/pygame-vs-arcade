import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
GOAL_SIZE = 50
PLAYER_COLOR = arcade.color.BLUE
GOAL_COLOR = arcade.color.GREEN
BG_COLOR = arcade.color.DARK_SLATE_GRAY
TITLE = "Move the Box - Arcade Version"
PLAYER_SPEED = 5

class MoveTheBox(arcade.Window):
    """Main application class."""

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(BG_COLOR)
        
        # Game state
        self.player = None
        self.goal = None
        self.game_won = False
        
    def setup(self):
        """Set up the game and initialize variables."""
        # Create the player and goal sprites
        self.player = arcade.SpriteSolidColor(PLAYER_SIZE, PLAYER_SIZE, PLAYER_COLOR)
        self.goal = arcade.SpriteSolidColor(GOAL_SIZE, GOAL_SIZE, GOAL_COLOR)
        
        # Set initial positions
        self.player.center_x = SCREEN_WIDTH // 4
        self.player.center_y = SCREEN_HEIGHT // 2
        self.goal.center_x = 3 * SCREEN_WIDTH // 4
        self.goal.center_y = SCREEN_HEIGHT // 2
        
        # Movement states
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        
        # Reset game state
        self.game_won = False
        
    def on_draw(self):
        """Render the screen."""
        # Clear the screen
        self.clear()
        
        # Draw the goal and player
        self.goal.draw()
        self.player.draw()
        
        # Display win message if the player reached the goal
        if self.game_won:
            arcade.draw_text("You Win!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                            arcade.color.WHITE, 72, anchor_x="center")
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if self.game_won:
            return
            
        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
    
    def on_key_release(self, key, modifiers):
        """Called whenever a key is released."""
        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
        elif key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
    
    def on_update(self, delta_time):
        """Movement and game logic."""
        if self.game_won:
            return
            
        # Calculate player movement based on keys pressed
        if self.left_pressed and not self.right_pressed:
            self.player.center_x -= PLAYER_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player.center_x += PLAYER_SPEED
        
        if self.up_pressed and not self.down_pressed:
            self.player.center_y += PLAYER_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player.center_y -= PLAYER_SPEED
        
        # Keep player on screen
        if self.player.center_x < PLAYER_SIZE // 2:
            self.player.center_x = PLAYER_SIZE // 2
        elif self.player.center_x > SCREEN_WIDTH - PLAYER_SIZE // 2:
            self.player.center_x = SCREEN_WIDTH - PLAYER_SIZE // 2
        
        if self.player.center_y < PLAYER_SIZE // 2:
            self.player.center_y = PLAYER_SIZE // 2
        elif self.player.center_y > SCREEN_HEIGHT - PLAYER_SIZE // 2:
            self.player.center_y = SCREEN_HEIGHT - PLAYER_SIZE // 2
        
        # Check for collision with goal
        if arcade.check_for_collision(self.player, self.goal):
            self.game_won = True

def main():
    """Main function to start the game."""
    window = MoveTheBox(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main() 