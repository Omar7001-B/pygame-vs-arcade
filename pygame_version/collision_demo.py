import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the window
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Collision Demo")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Game objects
class MovingSprite:
    def __init__(self, x, y, width, height, color, speed_x, speed_y):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.default_color = color
        self.collision_color = RED
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.in_collision = False
    
    def update(self):
        # Move the sprite
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Bounce off screen edges
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed_y *= -1
    
    def draw(self):
        # Draw the sprite - use collision color if in collision
        color = self.collision_color if self.in_collision else self.default_color
        pygame.draw.rect(screen, color, self.rect)
        
        # Add a small outline to make it more visible
        pygame.draw.rect(screen, BLACK, self.rect, 2)

class StationaryBlock:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        # Add a small outline to make it more visible
        pygame.draw.rect(screen, BLACK, self.rect, 2)

# Create game objects
moving_sprite = MovingSprite(50, 50, 30, 30, BLUE, 3, 2)
stationary_block = StationaryBlock(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50, 100, 100, GREEN)

# Game stats text
font = pygame.font.Font(None, 24)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

def check_collision():
    # Manual collision detection in Pygame
    return moving_sprite.rect.colliderect(stationary_block.rect)

def display_stats(fps, colliding):
    # Display FPS and collision status
    fps_text = font.render(f"FPS: {int(fps)}", True, WHITE)
    collision_text = font.render(f"Collision: {'Yes' if colliding else 'No'}", True, WHITE)
    library_text = font.render("Library: Pygame", True, WHITE)
    
    screen.blit(fps_text, (10, 10))
    screen.blit(collision_text, (10, 40))
    screen.blit(library_text, (10, 70))

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Update
    moving_sprite.update()
    
    # Check collision
    collision = check_collision()
    moving_sprite.in_collision = collision
    
    # Draw
    screen.fill(BLACK)
    stationary_block.draw()
    moving_sprite.draw()
    
    # Display stats
    current_fps = clock.get_fps()
    display_stats(current_fps, collision)
    
    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS) 