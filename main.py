import pygame
from projectiles import initiate_circle,move_circle
from start_menu import menu1,menu2
from buttons import start_button,settings_button,stop_button,restart_button,display_information_text


class Settings():
    def __init__(self):
        self.setting_projectile = ""
        self.setting_motion = ""
        self.menu1_on = True
        self.menu2_on = False
        self.is_run = False
        self.is_run_after = True
        self.reset_obj=True



def main_body():
    setting_obj=Settings()
    font = pygame.font.Font("freesansbold.ttf", 28)
    cursor=pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.mouse.set_cursor(cursor)
    WIDTH,HEIGHT=400,400     #dimensions of Surface
    running=True #condition for game loop
    global FPS
    FPS=1000  #program runs FPS amount of time in a second, one tick=1 millisecond
    WIN=pygame.display.set_mode((WIDTH,HEIGHT))
    global SCALE
    SCALE=20 #pixels for 1 meter
    clock = pygame.time.Clock()






    while running:     #main game loop
        while setting_obj.menu1_on == True or setting_obj.menu2_on == True:
            if setting_obj.menu1_on == True:
                pygame.display.set_mode((WIDTH, HEIGHT))
                setting_obj.setting_motion, setting_obj.menu1_on, setting_obj.menu2_on = menu1(WIN, WIDTH, HEIGHT, font)
            if setting_obj.menu2_on == True:
                pygame.display.set_mode((WIDTH, HEIGHT))
                setting_obj.setting_projectile, setting_obj.menu1_on, setting_obj.menu2_on = menu2(WIN, WIDTH, HEIGHT,
                                                                                                   font)
        if setting_obj.setting_projectile == "circle" and setting_obj.reset_obj==True:
            red_circle = initiate_circle(setting_obj.setting_motion)
            setting_obj.reset_obj=False

        WIDTH=800
        clock.tick(FPS)
        WIN = pygame.display.set_mode((WIDTH, HEIGHT),flags=pygame.SHOWN)
        WIN.fill("gray")

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
        if setting_obj.setting_projectile=="circle":
            if setting_obj.is_run==False:
                if setting_obj.setting_motion=="vertical":
                    pygame.draw.circle(WIN, "red", (red_circle.x_pos,red_circle.y_pos), red_circle.radius, 0)  # set the ball on the border
                    display_information_text(red_circle)

                elif setting_obj.setting_motion=="horizontal":
                    pygame.draw.circle(WIN,"red",(red_circle.x_pos,red_circle.y_pos),red_circle.radius,0)
                    display_information_text(red_circle)
                setting_obj.is_run=start_button(WIN,event)
                settings_button(WIN, event,red_circle,setting_obj)


            elif setting_obj.is_run==True and setting_obj.is_run_after==True:
                if setting_obj.setting_motion=="vertical":
                    move_circle(red_circle,FPS,SCALE,WIN)
                    display_information_text(red_circle)

                elif setting_obj.setting_motion=="horizontal":
                    move_circle(red_circle,FPS,SCALE,WIN)
                    display_information_text(red_circle)
                setting_obj.is_run_after=stop_button(WIN,event)
                if setting_obj.is_run_after==None:
                    setting_obj.is_run_after=True

            if setting_obj.is_run_after==False:
                pygame.draw.circle(WIN,"red",(red_circle.x_pos,red_circle.y_pos),red_circle.radius,0)
                display_information_text(red_circle)
                setting_obj.is_run_after=restart_button(WIN,event)
                settings_button(WIN, event,red_circle,setting_obj)
                if setting_obj.is_run_after==None:
                    setting_obj.is_run_after=False


        pygame.display.flip()




if __name__=="__main__":
    main_body()
