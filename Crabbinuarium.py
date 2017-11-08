# to import the pygame and sys to get the function in it

import sys
from object import Crab
from food import Food
from poison import Poison
from game_over import Game_over
from start_game import Start_game
import pygame
import time


# to run the game
def run_game():

    # to start the pygame program
    pygame.init()
    # to make the screen
    screen = pygame.display.set_mode((700,475))
    #to set the caption of the game
    pygame.display.set_caption("Crabbinuarium")
    # load background image to the screen
    bg = pygame.image.load('underwater.jpg').convert()
    # to know the resolution size
    screen_rect = screen.get_rect()
    # to make the naming easier later
    crab = Crab(screen)

    # to make sum of food
    foods = pygame.sprite.Group()
    food = Food(screen)

    # to make sum of the poison
    poisons = pygame.sprite.Group()
    poison = Poison(screen)

    # to make the crab not go over the screen on the right
    added_x = 0

    # make the jump time in the past so it can be compared with the time later
    jump_time = 0

    # score and highscore
    score = 0
    score_str = str(score)
    shown_score = 'Score : ' + score_str

    highscore = 0
    highscore_str = str(highscore)
    shown_highscore = 'Highscore : ' + highscore_str

    # start button
    game_run = False
    status_game_over = False

    crab_location = 378

    clock = pygame.time.Clock()


    # loop while game run
    while True:
        screen.blit(bg,[0,0])
        pressed = pygame.key.get_pressed()
        pygame.mouse.set_visible(False)



        # to get the command for each input and get the output of each action
        for event in pygame.event.get():
            # if the system want to quit/stop
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     if event.key == pygame.K_SPACE and crab.rect.y >= crab_location:
                         jump_time = time.time()

        # to know if the game is on staring game or game over and the resetting of the data game
        if game_run == False:
            # start button / game over and the final score
            if status_game_over == True:
                Game_over(screen).blitme()
                basicfont = pygame.font.SysFont(None, 50)
                current_score = basicfont.render(shown_score, True, (0, 0, 255))
                current_score_rect = current_score.get_rect()
                current_score_rect.x = screen_rect.centerx-100
                current_score_rect.y = 0
                screen.blit(current_score, (current_score_rect.x, current_score_rect.y))
                if pressed[pygame.K_z]:
                    game_run = False
                    status_game_over = False



            else:
                Start_game(screen).blitme()
                if pressed[pygame.K_z]:
                    game_run = True
                    status_game_over = False

                    # to reset the current data
                    crab_location = 378
                    added_x = 0
                    poisons.empty()
                    foods.empty()


                    score = 0
                    score_str = str(score)
                    shown_score = 'Score : ' + score_str



        elif game_run == True :

            # to compare the time of space for o.5 sec, in the 0.5 sec, the image will jump up, later it will fall down
            if time.time() - jump_time <= 0.75 :
                crab.rect.top -= 1
            elif crab.rect.y <= crab_location:
                  crab.rect.top += 1

            # to make the crab move

            if pressed[pygame.K_LEFT] and crab.rect.left > 0 :
                crab.rect.x -= 1
            elif pressed[pygame.K_RIGHT] and crab.rect.right < (screen_rect.right - added_x):
                crab.rect.x += 1

            # to draw the image

            crab.blitme()

            # to make add food each 500 frame to the group
            if (pygame.time.get_ticks()) % 500 == 0:
                foods.add(Food(screen))

            # to make the food appear
            for food in foods:
                food.blitme()
                # to make the food fall
                food.rect.y += 1
                # to make the food remove after it reach bottom to save data
                if food.rect.y == screen_rect.bottom :
                    foods.remove(food)


                # if the food and crap collide, the food will be remove and the crab grow
                food_collide = pygame.sprite.collide_rect(food , crab)

                if food_collide:
                    foods.remove(food)
                    score += 1
                    crab.growth()
                    added_x += 3
                    crab_location -= 1

                    # to show current score
                    score_str = str(score)
                    shown_score = 'Score : ' + score_str

                    # to show current highscore
                    if highscore <= score:
                        highscore = score
                        highscore_str = str(highscore)
                        shown_highscore = 'Highscore : ' + highscore_str


            # to make poison appear each 500 frame
            if (pygame.time.get_ticks()) % 500 == 0:
                poisons.add(Poison(screen))

            # to make the poison appear
            for poison in poisons:
                poison.blitme()
                # to make the poison fall
                poison.rect.y += 1
                # to make the poison remove after it reach bottom to save data
                if poison.rect.y == screen_rect.bottom :
                    poisons.remove(poison)


                # if the poison and crap collide, the food will be remove and the crab get reset
                poison_collide = pygame.sprite.collide_rect(poison , crab)

                if poison_collide:

                    game_run = False
                    status_game_over = True
                    crab.reset()



            # show score and highscore
            basicfont = pygame.font.SysFont(None, 34)
            current_score = basicfont.render(shown_score, True, (0, 0, 255))
            current_score_rect = current_score.get_rect()
            current_score_rect.x = screen_rect.right-250
            current_score_rect.y = 0
            screen.blit(current_score, (current_score_rect.x, current_score_rect.y))


            current_highscore = basicfont.render(shown_highscore, True, (0, 0, 255))
            current_highscore_rect = current_highscore.get_rect()
            current_highscore_rect.x = screen_rect.centerx-100
            current_highscore_rect.y = 0
            screen.blit(current_highscore, (current_highscore_rect.x,current_highscore_rect.y))

        # to set the frame speed
        clock.tick(200)

        # to update the screen
        pygame.display.flip()

# to run the game
run_game()
