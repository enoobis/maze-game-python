# Import necessary modules
import pygame

# Initialize pygame
pygame.init()

# Set the window size and title
size = (650, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Maze Game")

# Load the player image
player_image = pygame.image.load("C:\\Users\\enoobis\\Desktop\\kur\\player.png")

# Set the player's starting position
player_x = 50
player_y = 50

# Load the wall image
wall_image = pygame.image.load("C:\\Users\\enoobis\\Desktop\\kur\\wall.png")

# Set the wall positions
walls = [[100, 100], [200, 200], [300, 300]]

# Load the door image
door_image = pygame.image.load("C:\\Users\\enoobis\\Desktop\\kur\\door.png")

# Set the door position
door_x = 400
door_y = 400

# Load the key image
key_image = pygame.image.load("C:\\Users\\enoobis\\Desktop\\kur\\key.png")

# Set the key position
key_x = 50
key_y = 450

# Initialize the player's inventory
inventory = []

# Initialize the player's inventory
inventory = []

# Initialize the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_y -= 10
                if [player_x, player_y] in walls:
                    player_y += 10
            elif event.key == pygame.K_a:
                player_x -= 10
                if [player_x, player_y] in walls:
                    player_x += 10
            elif event.key == pygame.K_s:
                player_y += 10
                if [player_x, player_y] in walls:
                    player_y -= 10
            elif event.key == pygame.K_d:
                player_x += 10
                if [player_x, player_y] in walls:
                    player_x -= 10

    # Clear the screen to black
    screen.fill((0, 0, 0))

    # Draw the player
    screen.blit(player_image, (player_x, player_y))

    # Draw the walls
    for wall in walls:
        screen.blit(wall_image, (wall[0], wall[1]))

    # Draw the door
    screen.blit(door_image, (door_x, door_y))

    # Draw the key if it has not been collected yet
    if "key" not in inventory:
        screen.blit(key_image, (key_x, key_y))

    # Check for collision with key
    if player_x == key_x and player_y == key_y:
        inventory.append("key")

    # Check for collision with door
    if player_x == door_x and player_y == door_y:
        if "key" in inventory:
            font = pygame.font.Font(None, 36)
            text = font.render("You have unlocked the door and won the game!", True, (255, 255, 255))
            screen.blit(text, (50, 50))
            pygame.display.flip()
            pygame.time.wait(3000) # wait for 3 seconds before closing the game
            running = False
        else:
            font = pygame.font.Font(None, 36)
            text = font.render("You need a key to open the door.", True, (255, 255, 255))
            screen.blit(text, (50, 50))
            pygame.display.flip()
            pygame.time.wait(3000) # wait for 3 seconds before continuing the game
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()