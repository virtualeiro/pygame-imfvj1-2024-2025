import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Character Move Example')

# Set up clock
clock = pygame.time.Clock()
FPS = 60

# Set up character
character = pygame.Rect(50, screen_height // 2 - 25, 50, 50)  # x, y, width, height
character_speed = 200  # Pixels per second

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Main loop
running = True
x1=10
y1=20
x2=120
y2=120
elapsedTime=0
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get deltaTime (time since last frame) in seconds
    deltaTime = clock.tick(FPS) / 1000  # Converts milliseconds to seconds
    elapsedTime+=deltaTime
    # Update character position
    character.x += character_speed * deltaTime
    
    x = x1 + elapsedTime * (x2 - x1) 
    y = y1 + elapsedTime * (y2 - y1)
    pygame.draw.circle(screen, (255,0,0), (x,y),2)

    # Check if character has moved off the screen
    if character.x > screen_width:
        character.x = 0 - character.width  # Reset to the left side

    # Fill the screen with white
    #screen.fill(WHITE)

    # Draw the character (as a blue rectangle)
    pygame.draw.rect(screen, BLUE, character)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()