import pygame
import sys

# Initialize pygame
pygame.init()

# Window settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Animation - Pygame Version")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)

# Animation settings
SPRITE_WIDTH = 64
SPRITE_HEIGHT = 64
ANIMATION_FRAMES = 8
ANIMATION_SPEED = 5  # Frames per animation update
FPS = 60

class AnimatedSprite:
    def __init__(self, x, y, speed):
        # Position and movement
        self.x = x
        self.y = y
        self.speed = speed
        
        # Animation state
        self.current_frame = 0
        self.frame_count = 0
        self.frames = []
        
        # Create animation frames (different colored squares for demonstration)
        colors = [
            (255, 0, 0),    # Red
            (255, 127, 0),  # Orange
            (255, 255, 0),  # Yellow
            (0, 255, 0),    # Green
            (0, 0, 255),    # Blue
            (75, 0, 130),   # Indigo
            (148, 0, 211),  # Violet
            (255, 192, 203) # Pink
        ]
        
        # Create a list of surfaces for each frame
        for color in colors:
            # Create a surface for this frame
            frame = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT), pygame.SRCALPHA)
            
            # Draw the main square body
            pygame.draw.rect(frame, color, (0, 0, SPRITE_WIDTH, SPRITE_HEIGHT))
            
            # Add some details to show it's different (eyes and mouth)
            # Eyes
            eye_color = (255, 255, 255)
            pygame.draw.circle(frame, eye_color, (20, 20), 8)
            pygame.draw.circle(frame, eye_color, (44, 20), 8)
            
            # Pupils (move slightly based on frame to show animation)
            pupil_x_offset = (self.current_frame % 3) - 1  # -1, 0, or 1
            pupil_color = (0, 0, 0)
            pygame.draw.circle(frame, pupil_color, (20 + pupil_x_offset, 20), 4)
            pygame.draw.circle(frame, pupil_color, (44 + pupil_x_offset, 20), 4)
            
            # Mouth (changes with each frame)
            mouth_height = 5 + (self.current_frame % 4) * 2
            pygame.draw.rect(frame, (0, 0, 0), (22, 40, 20, mouth_height))
            
            # Add the frame to our animation list
            self.frames.append(frame)
    
    def update(self):
        # Move the sprite
        self.x += self.speed
        
        # Handle wrapping around the screen
        if self.x > SCREEN_WIDTH:
            self.x = -SPRITE_WIDTH
        
        # Update animation frame
        self.frame_count += 1
        if self.frame_count >= ANIMATION_SPEED:
            self.frame_count = 0
            self.current_frame = (self.current_frame + 1) % ANIMATION_FRAMES
    
    def draw(self, surface):
        # Draw the current frame at the sprite's position
        surface.blit(self.frames[self.current_frame], (self.x, self.y))
        
        # Draw frame number for demonstration purposes
        font = pygame.font.Font(None, 24)
        frame_text = font.render(f"Frame: {self.current_frame + 1}/{ANIMATION_FRAMES}", True, BLACK)
        surface.blit(frame_text, (self.x, self.y - 30))

def main():
    clock = pygame.time.Clock()
    
    # Create animated sprite
    sprite = AnimatedSprite(50, SCREEN_HEIGHT // 2 - SPRITE_HEIGHT // 2, 2)
    
    # Main game loop
    running = True
    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update sprite
        sprite.update()
        
        # Draw everything
        screen.fill(WHITE)
        
        # Draw ground
        pygame.draw.rect(screen, GRAY, (0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40))
        
        # Draw sprite
        sprite.draw(screen)
        
        # Draw instructions and info
        font = pygame.font.Font(None, 36)
        title_text = font.render("Pygame Sprite Animation Demo", True, BLACK)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 20))
        
        info_font = pygame.font.Font(None, 24)
        info_text1 = info_font.render("Pygame requires manual frame management", True, BLACK)
        info_text2 = info_font.render("Each frame is a separate surface", True, BLACK)
        info_text3 = info_font.render("Animation timing is handled with counter variables", True, BLACK)
        
        screen.blit(info_text1, (20, SCREEN_HEIGHT - 100))
        screen.blit(info_text2, (20, SCREEN_HEIGHT - 75))
        screen.blit(info_text3, (20, SCREEN_HEIGHT - 50))
        
        # Update display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(FPS)

    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 