import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CIRCLE_RADIUS = 50
CIRCLE_COLOR = (255, 0, 0)  # Red
BG_COLOR = (255, 255, 255)  # White
TEXT_COLOR = (0, 0, 255)    # Blue
FPS = 60

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Click the Circle to Win - Pygame')

# Circle position (center of the screen)
circle_x = SCREEN_WIDTH // 2
circle_y = SCREEN_HEIGHT // 2

# Font for the win message
font = pygame.font.SysFont(None, 64)

# Game state
game_won = False
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_won:
            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Calculate distance between mouse click and circle center
            distance = math.sqrt((mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2)
            
            # Check if click is within the circle
            if distance <= CIRCLE_RADIUS:
                game_won = True

    # Fill the screen with white
    screen.fill(BG_COLOR)
    
    # Draw the circle
    pygame.draw.circle(screen, CIRCLE_COLOR, (circle_x, circle_y), CIRCLE_RADIUS)
    
    # If game is won, display the win message
    if game_won:
        win_text = font.render("You Win!", True, TEXT_COLOR)
        text_rect = win_text.get_rect(center=(SCREEN_WIDTH//2, 100))
        screen.blit(win_text, text_rect)

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)

pygame.quit() 