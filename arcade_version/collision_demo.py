import arcade

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Arcade Collision Demo"

# Colors
BLUE = arcade.color.BLUE
RED = arcade.color.RED
GREEN = arcade.color.GREEN
BLACK = arcade.color.BLACK
WHITE = arcade.color.WHITE

class MovingSprite(arcade.SpriteSolidColor):
    """A sprite that moves around the screen and changes color on collision"""
    
    def __init__(self, width, height, color):
        # Initialize the sprite
        super().__init__(width, height, color)
        
        # Set initial position and velocity
        self.center_x = 50
        self.center_y = 50
        self.change_x = 3
        self.change_y = 2
        
        # Default appearance
        self.default_color = color
        self.collision_color = RED
        self.in_collision = False
        self.color = self.default_color
    
    def update(self):
        """Update the sprite's position and check for boundary collisions"""
        # Move the sprite
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        # Bounce off screen edges
        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y *= -1
        
        # Update color based on collision state
        self.color = self.collision_color if self.in_collision else self.default_color

class StationaryBlock(arcade.SpriteSolidColor):
    """A stationary block sprite"""
    
    def __init__(self, width, height, color):
        # Initialize the sprite
        super().__init__(width, height, color)
        
        # Set position in the center of the screen
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2

class CollisionDemo(arcade.Window):
    """Main application class"""
    
    def __init__(self, width, height, title):
        # Initialize the window
        super().__init__(width, height, title)
        
        # Set the background color
        arcade.set_background_color(BLACK)
        
        # Sprite lists
        self.moving_sprite_list = None
        self.stationary_sprite_list = None
        
        # Individual sprites
        self.moving_sprite = None
        self.stationary_block = None
        
        # Collision state
        self.is_colliding = False
    
    def setup(self):
        """Set up the game and initialize variables"""
        # Create sprite lists
        self.moving_sprite_list = arcade.SpriteList()
        self.stationary_sprite_list = arcade.SpriteList()
        
        # Create and add the moving sprite
        self.moving_sprite = MovingSprite(30, 30, BLUE)
        self.moving_sprite_list.append(self.moving_sprite)
        
        # Create and add the stationary block
        self.stationary_block = StationaryBlock(100, 100, GREEN)
        self.stationary_sprite_list.append(self.stationary_block)
    
    def on_draw(self):
        """Render the screen"""
        # Clear the screen
        self.clear()
        
        # Draw the sprites
        self.stationary_sprite_list.draw()
        self.moving_sprite_list.draw()
        
        # Draw outlines for better visibility
        arcade.draw_rectangle_outline(
            self.stationary_block.center_x, 
            self.stationary_block.center_y,
            self.stationary_block.width,
            self.stationary_block.height,
            BLACK, 2
        )
        
        arcade.draw_rectangle_outline(
            self.moving_sprite.center_x, 
            self.moving_sprite.center_y,
            self.moving_sprite.width,
            self.moving_sprite.height,
            BLACK, 2
        )
        
        # Display stats
        arcade.draw_text(
            f"FPS: {int(self.current_fps)}",
            10, SCREEN_HEIGHT - 30,
            WHITE, 24
        )
        
        arcade.draw_text(
            f"Collision: {'Yes' if self.is_colliding else 'No'}",
            10, SCREEN_HEIGHT - 60,
            WHITE, 24
        )
        
        arcade.draw_text(
            "Library: Arcade",
            10, SCREEN_HEIGHT - 90,
            WHITE, 24
        )
    
    def on_update(self, delta_time):
        """Movement and game logic"""
        # Update the sprites
        self.moving_sprite_list.update()
        
        # Check for collisions
        collision_list = arcade.check_for_collision_with_list(
            self.moving_sprite, self.stationary_sprite_list
        )
        
        # Update collision state
        self.is_colliding = len(collision_list) > 0
        self.moving_sprite.in_collision = self.is_colliding
        
        # Track FPS
        if hasattr(self, '_fps_counter'):
            self._fps_counter += 1
            self._fps_time += delta_time
            if self._fps_time >= 1.0:
                self.current_fps = self._fps_counter / self._fps_time
                self._fps_counter = 0
                self._fps_time = 0
        else:
            self._fps_counter = 0
            self._fps_time = 0
            self.current_fps = 60  # Initial estimate

def main():
    """Main function"""
    window = CollisionDemo(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main() 