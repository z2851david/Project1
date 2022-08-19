import pygame
import tkinter
from projectiles import Ball,initiate_circle,move_circle_vertically,move_circle_horizontally
from start_menu import menu1,menu2
from buttons import start_button




def main_body():
    setting_projectile=""
    setting_motion=""
    menu1_on=True
    menu2_on=False
    is_run=False
    font = pygame.font.Font("freesansbold.ttf", 28)
    cursor=pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.mouse.set_cursor(cursor)
    WIDTH,HEIGHT=400,400     #dimensions of Surface
    running=True #condition for game loop
    global FPS
    FPS=60  #program runs FPS amount of time in a second, one tick=1 millisecond
    WIN=pygame.display.set_mode((WIDTH,HEIGHT))
    global SCALE
    SCALE=5 #pixels for 1 meter
    clock = pygame.time.Clock()


    while menu1_on==True or menu2_on==True:
        if menu1_on==True:
            pygame.display.set_mode((WIDTH,HEIGHT))
            setting_motion,menu1_on,menu2_on=menu1(WIN,WIDTH,HEIGHT,font)
        if menu2_on==True:
            pygame.display.set_mode((WIDTH,HEIGHT))
            setting_projectile,menu1_on,menu2_on=menu2(WIN,WIDTH,HEIGHT,font)
    if setting_projectile=="circle":

        red_circle=initiate_circle(setting_motion)




    while running:     #main game loop
        clock.tick(FPS)
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
        if setting_projectile=="circle":
            if is_run==False:
                if setting_motion=="vertical":
                    pygame.draw.circle(WIN, "red", (red_circle.center[0], 0+ red_circle.radius), red_circle.radius, 0)  # set the ball on the border
                elif setting_motion=="horizontal":
                    pygame.draw.circle(WIN,"red",(0+red_circle.radius,red_circle.center[1]),red_circle.radius,0)
                is_run=start_button(WIN,event)

            elif is_run==True:
                if setting_motion=="vertical":
                    move_circle_vertically(red_circle)
                elif setting_motion=="horizontal":
                    move_circle_horizontally(red_circle)

        pygame.display.flip()




if __name__=="__main__":
    main_body()
