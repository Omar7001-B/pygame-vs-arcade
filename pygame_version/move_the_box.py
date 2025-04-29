import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
GOAL_SIZE = 50
PLAYER_COLOR = (0, 128, 255)  # Blue
GOAL_COLOR = (0, 255, 0)      # Green
BG_COLOR = (30, 30, 30)       # Dark gray
TEXT_COLOR = (255, 255, 255)  # White
FPS = 60

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Move the Box - Pygame Version')
clock = pygame.time.Clock()

# Game state
class GameState:
    def __init__(self):
        self.player_pos = [SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2]
        self.goal_pos = [3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2]
        self.player_rect = pygame.Rect(self.player_pos[0], self.player_pos[1], PLAYER_SIZE, PLAYER_SIZE)
        self.goal_rect = pygame.Rect(self.goal_pos[0], self.goal_pos[1], GOAL_SIZE, GOAL_SIZE)
        self.player_speed = 5
        self.game_won = False

# Create game state
game = GameState()

# Main game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle player movement
    if not game.game_won:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            game.player_pos[0] -= game.player_speed
        if keys[pygame.K_RIGHT]:
            game.player_pos[0] += game.player_speed
        if keys[pygame.K_UP]:
            game.player_pos[1] -= game.player_speed
        if keys[pygame.K_DOWN]:
            game.player_pos[1] += game.player_speed
        
        # Keep player on screen
        game.player_pos[0] = max(0, min(game.player_pos[0], SCREEN_WIDTH - PLAYER_SIZE))
        game.player_pos[1] = max(0, min(game.player_pos[1], SCREEN_HEIGHT - PLAYER_SIZE))
        
        # Update player rectangle position
        game.player_rect.x = game.player_pos[0]
        game.player_rect.y = game.player_pos[1]
        
        # Check for collision with goal
        if game.player_rect.colliderect(game.goal_rect):
            game.game_won = True
    
    # Draw everything
    screen.fill(BG_COLOR)
    
    # Draw goal
    pygame.draw.rect(screen, GOAL_COLOR, game.goal_rect)
    
    # Draw player
    pygame.draw.rect(screen, PLAYER_COLOR, game.player_rect)
    
    # Display win message if player reached goal
    if game.game_won:
        font = pygame.font.Font(None, 72)
        text = font.render("You Win!", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
    
    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit() 