import pygame
from pygame.locals import*
import random
import os 
pygame.mixer.init()
pygame.mixer.music.load('play2.mp3')
pygame.mixer.music.play()

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    #game window
    sc_width = 900
    sc_height = 500
    gamewindow = pygame.display.set_mode((sc_width,sc_height))
    pygame.display.set_caption("ruchi's first game")
    #color
    white = (255,255,255)
    black = (0,0,0)
    #game variable
    exit_game = False
    game_over = False
    sn_x = 455
    sn_y = 200
    sn_vel_x = 1
    sn_vel_y = 1
    init_vel = 6
    sn_size = 15
    score = 0
    foodsize = 10
    fps = 35
    font = pygame.font.SysFont("timesnewroman",40)
    sn_list = []
    sn_length = 1
    # change of variable
    foodx = 55
    foody = 55
    red = (255,0,0)

    def plot_sn(gamewindow,color,sn_list,sn_size):
        for x,y in sn_list:
            pygame.draw.rect(gamewindow,color,[x,y,sn_size,sn_size])
    def text_scr(text,color,x,y):
        screen_text = font.render(text,True,color)
        gamewindow.blit(screen_text,[x,y])
    with open ("hiscore.txt",'r') as f:
                hiscore = f.read()
    clock = pygame.time.Clock()
    #gameloop
    while not exit_game:
        if game_over:
            with open ("hiscore.txt",'w') as f:
                f.write(str(hiscore))

            gamewindow.fill(white)
            text_scr("GAME OVER!!!",red,sc_width/5,sc_height/2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        sn_vel_x = init_vel
                        sn_vel_y = 0
                    if event.key == pygame.K_LEFT:
                        sn_vel_x = - init_vel
                        sn_vel_y = 0
                    if event.key == pygame.K_UP:
                        sn_vel_y = - init_vel
                        sn_vel_x = 0
                    if event.key == pygame.K_DOWN:
                        sn_vel_y = init_vel
                        sn_vel_x = 0
                    if event.key == pygame.K_r:
                        score += 100

            sn_x += sn_vel_x
            sn_y += sn_vel_y

            if abs(sn_x-foodx)<15 and abs(sn_y-foody)<15:
                score+=20
                
                foodx = random.randint(5,sc_width-5)
                foody = random.randint(5,sc_height)-5
                a = random.randint(0,255)
                b = random.randint(0,255)
                c = random.randint(0,255)
                red = (a,b,c)
                foodsize = random.randint(11,20)
                sn_length += 5

              
            gamewindow.fill(black)
            text_scr("Score:"+ str(score) + "  Highscore:" + str(hiscore),red,5,5)
            pygame.draw.rect(gamewindow,red,(foodx,foody,foodsize,foodsize))

            if score>int(hiscore):
                    hiscore = score 
            head = []
            head.append(sn_x)
            head.append(sn_y)
            sn_list.append(head)
            if len(sn_list)>sn_length:
                del sn_list[0]
            if head in sn_list[:-1]:
                game_over = True    
            if sn_x<0 or sn_x>sc_width or sn_y<0 or sn_y>sc_height :
                game_over = True

            plot_sn(gamewindow,white,sn_list,sn_size) 
            
        pygame.display.update()
        clock.tick(fps)
        

    pygame.quit()
    quit()















