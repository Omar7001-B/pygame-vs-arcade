import pygame
import random
import sys
import time

# Initialize pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SNAKE_SPEED = 10

# Direction constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game - Pygame Version')
clock = pygame.time.Clock()

# Initialize game elements
def init_game():
    # Initial snake position (middle of screen)
    initial_position = (GRID_WIDTH // 2, GRID_HEIGHT // 2)
    snake_body = [initial_position]
    
    # Initial direction
    direction = RIGHT
    
    # Generate first food
    food_position = generate_food(snake_body)
    
    # Score
    score = 0
    
    return snake_body, direction, food_position, score, False

def generate_food(snake_body):
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        food_position = (x, y)
        
        # Make sure food doesn't spawn on snake
        if food_position not in snake_body:
            return food_position

def game_over_screen(score):
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("Game Over", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    restart_text = font.render("Press R to Restart", True, WHITE)
    quit_text = font.render("Press Q to Quit", True, WHITE)
    
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100))
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 100))
    quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 170))
    
    screen.fill(BLACK)
    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    screen.blit(restart_text, restart_rect)
    screen.blit(quit_text, quit_rect)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        clock.tick(SNAKE_SPEED)

def run_game():
    # Initialize game state
    snake_body, direction, food_position, score, game_over = init_game()
    
    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Change direction based on key press
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT
        
        if not game_over:
            # Move snake
            head_x, head_y = snake_body[0]
            new_head = (head_x + direction[0], head_y + direction[1])
            
            # Check for collision with walls
            if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
                new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or
                new_head in snake_body):
                game_over = True
            else:
                # Add new head to snake
                snake_body.insert(0, new_head)
                
                # Check if snake ate food
                if new_head == food_position:
                    # Generate new food and increase score
                    food_position = generate_food(snake_body)
                    score += 1
                else:
                    # Remove tail if no food was eaten
                    snake_body.pop()
            
            # Draw everything
            screen.fill(BLACK)
            
            # Draw snake
            for segment in snake_body:
                pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, 
                                                segment[1] * GRID_SIZE, 
                                                GRID_SIZE, GRID_SIZE))
            
            # Draw food
            pygame.draw.rect(screen, RED, (food_position[0] * GRID_SIZE,
                                          food_position[1] * GRID_SIZE,
                                          GRID_SIZE, GRID_SIZE))
            
            # Draw score
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))
            
            pygame.display.flip()
            clock.tick(SNAKE_SPEED)
        else:
            # Show game over screen and get restart decision
            if game_over_screen(score):
                snake_body, direction, food_position, score, game_over = init_game()
    
    pygame.quit()
    sys.exit()

# Start the game
if __name__ == "__main__":
    run_game() 