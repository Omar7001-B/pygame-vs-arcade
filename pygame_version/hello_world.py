import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the window
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hello World - Pygame Version")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font setup
font = pygame.font.Font(None, 64)  # Default font, size 64
hello_text = font.render("Hello World!", True, WHITE)
text_rect = hello_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with black
    screen.fill(BLACK)
    
    # Draw the hello world text
    screen.blit(hello_text, text_rect)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit() 