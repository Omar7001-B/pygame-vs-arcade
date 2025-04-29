import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snake Game - Arcade Version"

GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# We'll set the game to run at a normal frame rate
FRAME_RATE = 60  # Normal frame rate for smooth rendering

# But we'll only move the snake every X frames
MOVE_EVERY_X_FRAMES = 5  # Move only every 30 frames (0.5 seconds at 60 FPS)

# Colors
SNAKE_COLOR = arcade.color.GREEN
FOOD_COLOR = arcade.color.RED
BG_COLOR = arcade.color.BLACK
TEXT_COLOR = arcade.color.WHITE

# Direction constants
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Snake:
    """Snake player class"""
    
    def __init__(self):
        # Initialize the snake at the center of the screen
        self.x = GRID_WIDTH // 2
        self.y = GRID_HEIGHT // 2
        
        # Initial body (just the head)
        self.body = [(self.x, self.y)]
        
        # Initial direction
        self.direction = RIGHT
        
        # Movement offsets for each direction
        self.direction_offsets = {
            UP: (0, 1),
            RIGHT: (1, 0),
            DOWN: (0, -1),
            LEFT: (-1, 0)
        }
    
    def move(self):
        """Move the snake by adding a new head and removing the tail"""
        # Get movement offset based on current direction
        dx, dy = self.direction_offsets[self.direction]
        
        # Calculate new head position
        new_head_x = self.body[0][0] + dx
        new_head_y = self.body[0][1] + dy
        
        # Add new head to the beginning of the body
        self.body.insert(0, (new_head_x, new_head_y))
    
    def grow(self):
        """Grow the snake by not removing the tail on the next move"""
        # The tail is not removed when the snake eats, which makes it grow
        pass
    
    def check_collision_with_self(self):
        """Check if the snake has collided with itself"""
        return self.body[0] in self.body[1:]
    
    def check_collision_with_walls(self):
        """Check if the snake has collided with the walls"""
        # We're no longer checking for wall collisions since we want wrap-around behavior
        return False
    
    def check_collision_with_food(self, food):
        """Check if the snake has collided with the food"""
        return self.body[0] == food
    
    def draw(self):
        """Draw the snake on the screen"""
        for segment in self.body:
            x, y = segment
            # Draw each segment as a rectangle
            arcade.draw_rectangle_filled(
                x * GRID_SIZE + GRID_SIZE // 2,
                y * GRID_SIZE + GRID_SIZE // 2,
                GRID_SIZE,
                GRID_SIZE,
                SNAKE_COLOR
            )

class SnakeGame(arcade.Window):
    """Main game class"""
    
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(BG_COLOR)
        
        # Initialize game states
        self.snake = None
        self.food = None
        self.score = 0
        self.game_over = False
        
        # Frame counter for controlling snake speed
        self.frame_count = 0
        
        # Set up the game
        self.setup()
    
    def setup(self):
        """Set up the game for a new round"""
        # Create a new snake
        self.snake = Snake()
        
        # Create initial food
        self.generate_food()
        
        # Reset score and game state
        self.score = 0
        self.game_over = False
    
    def generate_food(self):
        """Generate a new food at a random position"""
        while True:
            # Random position for food
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            
            # Make sure food doesn't spawn on snake
            if (x, y) not in self.snake.body:
                self.food = (x, y)
                break
    
    def on_draw(self):
        """Render the screen"""
        arcade.start_render()
        
        # Draw food
        food_x, food_y = self.food
        arcade.draw_rectangle_filled(
            food_x * GRID_SIZE + GRID_SIZE // 2,
            food_y * GRID_SIZE + GRID_SIZE // 2,
            GRID_SIZE,
            GRID_SIZE,
            FOOD_COLOR
        )
        
        # Draw snake
        self.snake.draw()
        
        # Draw score
        arcade.draw_text(
            f"Score: {self.score}",
            10,
            SCREEN_HEIGHT - 30,
            TEXT_COLOR,
            20
        )
        
        # Draw game over screen if game is over
        if self.game_over:
            arcade.draw_text(
                "Game Over",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 + 50,
                TEXT_COLOR,
                54,
                anchor_x="center"
            )
            arcade.draw_text(
                f"Score: {self.score}",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                TEXT_COLOR,
                30,
                anchor_x="center"
            )
            arcade.draw_text(
                "Press R to Restart",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 - 50,
                TEXT_COLOR,
                24,
                anchor_x="center"
            )
            arcade.draw_text(
                "Press Q to Quit",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 - 100,
                TEXT_COLOR,
                24,
                anchor_x="center"
            )
    
    def on_key_press(self, key, modifiers):
        """Handle key presses"""
        if not self.game_over:
            # Change direction based on key press
            if key == arcade.key.UP and self.snake.direction != DOWN:
                self.snake.direction = UP
            elif key == arcade.key.DOWN and self.snake.direction != UP:
                self.snake.direction = DOWN
            elif key == arcade.key.LEFT and self.snake.direction != RIGHT:
                self.snake.direction = LEFT
            elif key == arcade.key.RIGHT and self.snake.direction != LEFT:
                self.snake.direction = RIGHT
        else:
            # Restart or quit the game
            if key == arcade.key.R:
                self.setup()
            elif key == arcade.key.Q:
                arcade.close_window()
    
    def update(self, delta_time):
        """Update the game state"""
        if not self.game_over:
            # Increment the frame counter
            self.frame_count += 1
            
            # Only move the snake every X frames
            if self.frame_count >= MOVE_EVERY_X_FRAMES:
                self.frame_count = 0  # Reset counter
                
                # Move the snake
                self.snake.move()
                
                # Get the current head position and handle wrapping around screen edges
                head_x, head_y = self.snake.body[0]
                
                # Wrap around if snake goes off screen
                if head_x < 0:
                    self.snake.body[0] = (GRID_WIDTH - 1, head_y)
                elif head_x >= GRID_WIDTH:
                    self.snake.body[0] = (0, head_y)
                
                if head_y < 0:
                    self.snake.body[0] = (head_x, GRID_HEIGHT - 1)
                elif head_y >= GRID_HEIGHT:
                    self.snake.body[0] = (head_x, 0)
                
                # Check for collision with self only (not walls)
                if self.snake.check_collision_with_self():
                    self.game_over = True
                    return
                
                # Check for collision with food
                if self.snake.check_collision_with_food(self.food):
                    # Increase score
                    self.score += 1
                    
                    # Generate new food
                    self.generate_food()
                else:
                    # Remove tail if no food was eaten
                    self.snake.body.pop()

def main():
    """Main function to start the game"""
    window = SnakeGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # Run at normal frame rate for smooth rendering
    arcade.run()

if __name__ == "__main__":
    main() 