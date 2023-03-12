import pygame, sys, random
from pygame.locals import *

pygame.init()

# Colors
BACKGROUND = (255, 255, 255)
ELEMENTCOLOR = (100, 100, 100)

# GAME Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

GAME_WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Create a surface obj with set windows parameters
pygame.display.set_caption("PONG!")

# PADDLE Variables
PADDLEINSET = 20
PADDLEWIDTH = 10
PADDLEHEIGHT = 60
PADDLESPEED = 4

# BALL Variables
BALLSIZE = 10

# Main function with game loop
def main():
    running = True

    left_paddle_y = 50
    right_paddle_y = 50
    ball_X = WINDOW_WIDTH // 2
    ball_Y = WINDOW_HEIGHT // 2
    ball_X_momentum = 1
    ball_Y_momentum = 1

    # Main gameplay loop
    while running:
        # Get inputs
        for event in pygame.event.get():
            #print(event.type)
            if event.type == QUIT:
                pygame.quit()
                return
            
            # Gets sequence of boolean values representing state of every key on
            # keyboard and if they have been pressed
        pressed = pygame.key.get_pressed()
        # print(pressed)
        if pressed[K_ESCAPE]:
            pygame.quit()
            return
            
        if pressed[K_w]:
            left_paddle_y -= PADDLESPEED
        elif pressed[K_s]:
            left_paddle_y += PADDLESPEED

        if pressed[K_UP]:
            right_paddle_y -= PADDLESPEED
        elif pressed[K_DOWN]:
            right_paddle_y += PADDLESPEED

        # Handle if paddle has gone above or below the the screen
        if left_paddle_y < 0:
            left_paddle_y = 0
        if left_paddle_y > WINDOW_HEIGHT - PADDLEHEIGHT:
            left_paddle_y = WINDOW_HEIGHT - PADDLEHEIGHT
        if right_paddle_y < 0:
            right_paddle_y = 0
        if right_paddle_y > WINDOW_HEIGHT - PADDLEHEIGHT:
            right_paddle_y = WINDOW_HEIGHT - PADDLEHEIGHT
            
        if ball_Y < BALLSIZE: # ball has hit the top of the screen
            ball_Y_momentum = 1
        if ball_Y > WINDOW_HEIGHT - BALLSIZE: # ball has hit the bottom
            ball_Y_momentum = -1
            
        
        # Processing
        # pygame.Rect obj for holding rect coordinates
        left_paddle_rect = pygame.Rect(PADDLEINSET, left_paddle_y, PADDLEWIDTH, PADDLEHEIGHT)
        right_paddle_rect = pygame.Rect(WINDOW_WIDTH - PADDLEINSET - PADDLEWIDTH, right_paddle_y, 
                                        PADDLEWIDTH, PADDLEHEIGHT)
        
        ball_X = ball_X + ball_X_momentum
        ball_Y = ball_Y + ball_Y_momentum

        # Render elements of the game
        GAME_WINDOW.fill(BACKGROUND) # Fill a surface with a solid color 
        # Draw a straight line 
        pygame.draw.line(GAME_WINDOW, ELEMENTCOLOR, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT), 2)
        # Draw Rectangle
        pygame.draw.rect(GAME_WINDOW, ELEMENTCOLOR, left_paddle_rect)
        pygame.draw.rect(GAME_WINDOW, ELEMENTCOLOR, right_paddle_rect)
        # Draw ball
        pygame.draw.circle(GAME_WINDOW, ELEMENTCOLOR, (ball_X, ball_Y), BALLSIZE)
        
        pygame.display.update()
        fpsClock.tick(FPS)
    

    pygame.quit()


if __name__=="__main__":
    main()
