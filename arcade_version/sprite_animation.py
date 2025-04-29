import arcade

# Window settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Sprite Animation - Arcade Version"

# Colors
WHITE = arcade.color.WHITE
BLACK = arcade.color.BLACK
GRAY = arcade.color.GRAY

# Animation settings
SPRITE_WIDTH = 64
SPRITE_HEIGHT = 64
ANIMATION_FRAMES = 8
SPRITE_SCALING = 1.0

class AnimatedSprite(arcade.Sprite):
    def __init__(self, center_x, center_y, speed):
        # Initialize parent class
        super().__init__()
        
        # Set sprite properties
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = speed
        
        # Animation tracking
        self.current_texture = 0
        self.scale = SPRITE_SCALING
        
        # Create textures - different colored squares with faces
        self.textures = []
        colors = [
            arcade.color.RED,
            arcade.color.ORANGE,
            arcade.color.YELLOW,
            arcade.color.GREEN,
            arcade.color.BLUE,
            arcade.color.PURPLE,
            arcade.color.VIOLET,
            arcade.color.PINK
        ]
        
        # Generate textures for animation
        for i, color in enumerate(colors):
            # Create a texture filled with the specified color
            texture = arcade.Texture.create_filled(
                f"frame_{i}", 
                (SPRITE_WIDTH, SPRITE_HEIGHT), 
                color
            )
            
            # Add the texture to our list
            self.textures.append(texture)
        
        # Set the initial texture
        self.texture = self.textures[0]
        
        # Add facial features to show animation
        self.eye_size = 8
        self.pupil_size = 4
        self.mouth_width = 20
    
    def update(self):
        # Move the sprite
        self.center_x += self.change_x
        
        # Handle wrapping around the screen
        if self.center_x > SCREEN_WIDTH + self.width/2:
            self.center_x = -self.width/2
    
    def update_animation(self, delta_time: float = 1/60):
        # Update animation frame by advancing to the next texture
        self.current_texture += 1
        if self.current_texture >= len(self.textures):
            self.current_texture = 0
        self.texture = self.textures[self.current_texture]

class AnimationDemo(arcade.Window):
    def __init__(self, width, height, title):
        # Initialize parent class
        super().__init__(width, height, title)
        
        # Set background color
        arcade.set_background_color(WHITE)
        
        # Initialize sprite list
        self.sprite_list = None
        self.animated_sprite = None
        
    def setup(self):
        # Create sprite list
        self.sprite_list = arcade.SpriteList()
        
        # Create animated sprite
        self.animated_sprite = AnimatedSprite(
            100,  # x position
            SCREEN_HEIGHT // 2,  # y position
            2     # speed
        )
        
        # Add sprite to the list
        self.sprite_list.append(self.animated_sprite)
    
    def on_draw(self):
        # Clear the screen
        self.clear()
        
        # Draw ground
        arcade.draw_rectangle_filled(
            SCREEN_WIDTH // 2, 20, SCREEN_WIDTH, 40, GRAY
        )
        
        # Draw sprites
        self.sprite_list.draw()
        
        # Draw facial features on top of the sprite
        # Eyes (white circles)
        arcade.draw_circle_filled(
            self.animated_sprite.center_x - 12,
            self.animated_sprite.center_y + 12,
            self.animated_sprite.eye_size,
            arcade.color.WHITE
        )
        arcade.draw_circle_filled(
            self.animated_sprite.center_x + 12,
            self.animated_sprite.center_y + 12,
            self.animated_sprite.eye_size,
            arcade.color.WHITE
        )
        
        # Pupils (move based on frame)
        pupil_offset = (self.animated_sprite.current_texture % 3) - 1  # -1, 0, or 1
        arcade.draw_circle_filled(
            self.animated_sprite.center_x - 12 + pupil_offset,
            self.animated_sprite.center_y + 12,
            self.animated_sprite.pupil_size,
            arcade.color.BLACK
        )
        arcade.draw_circle_filled(
            self.animated_sprite.center_x + 12 + pupil_offset,
            self.animated_sprite.center_y + 12,
            self.animated_sprite.pupil_size,
            arcade.color.BLACK
        )
        
        # Mouth (changes size with frame)
        mouth_height = 5 + (self.animated_sprite.current_texture % 4) * 2
        arcade.draw_rectangle_filled(
            self.animated_sprite.center_x,
            self.animated_sprite.center_y - 12,
            self.animated_sprite.mouth_width,
            mouth_height,
            arcade.color.BLACK
        )
        
        # Draw frame number for demonstration
        arcade.draw_text(
            f"Frame: {self.animated_sprite.current_texture + 1}/{ANIMATION_FRAMES}",
            self.animated_sprite.center_x - 40,
            self.animated_sprite.center_y + 40,
            BLACK, 14
        )
        
        # Draw title and information
        arcade.draw_text(
            "Arcade Sprite Animation Demo",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30,
            BLACK, 24, anchor_x="center"
        )
        
        arcade.draw_text(
            "Arcade provides built-in animation support",
            20, 140, BLACK, 14
        )
        
        arcade.draw_text(
            "Textures are automatically managed",
            20, 120, BLACK, 14
        )
        
        arcade.draw_text(
            "Animation is updated through the sprite's update_animation method",
            20, 100, BLACK, 14
        )
    
    def on_update(self, delta_time):
        # Move sprites
        self.sprite_list.update()
        
        # Update animations - Using Arcade's automatic animation system
        self.sprite_list.update_animation()

def main():
    # Create the game window
    window = AnimationDemo(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    
    # Set up the game
    window.setup()
    
    # Run the game
    arcade.run()

if __name__ == "__main__":
    main() 