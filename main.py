iimport pygame,time
from projectiles import initiate_circle, move_circle
from start_menu import menu1, menu2
from buttons import display_information_text,init_buttons
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox



class Settings():
    def __init__(self):
        self.setting_projectile = ""
        self.setting_motion = ""
        self.menu1_on = True
        self.menu2_on = False
        self.is_run = False
        self.is_run_after = True
        self.reset_obj = True
        self.window_size = pygame.display.get_desktop_sizes()
        self.window_width = self.window_size[0][0]
        self.window_height = self.window_size[0][1]
        self.horizontal_width = (self.window_width // 3)*2
        self.setting_side_width=self.window_width-(self.window_width//3)
        self.vertical_width=self.window_width//3
        self.bounce=False
        self.delta_time=0
        self.scale=0
        self.FPS=60
        self.initalise_counter=0
        self.slider_counter=0


def main_body():
    setting_obj = Settings()
    setting_obj.window_width = 400
    setting_obj.window_height = 400
    font = pygame.font.Font("freesansbold.ttf", 28)
    font2 = pygame.font.Font("freesansbold.ttf", 32)
    font3=pygame.font.Font("freesansbold.ttf", 18)
    font4=pygame.font.Font("freesansbold.ttf",50)
    cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.mouse.set_cursor(cursor)
    running = True  # condition for game loop
    global FPS
    FPS =60  # program runs FPS amount of time in a second, one tick=1 millisecond
    WIN = pygame.display.set_mode((setting_obj.window_width, setting_obj.window_height))
    global SCALE
    setting_obj.scale = 10  # pixels for 1 meter
    prev_time=time.time()
    clock = pygame.time.Clock()
    RECORD_EVENT=pygame.USEREVENT
    coord_list=[]


    while running:  # main game loop
        # ============================================Main Menu=======================================================#
        while setting_obj.menu1_on == True or setting_obj.menu2_on == True:

            if setting_obj.menu1_on == True:
                setting_obj.window_width = 400
                setting_obj.window_height = 400
                pygame.display.set_mode((setting_obj.window_width, setting_obj.window_height))
                setting_obj.setting_motion, setting_obj.menu1_on, setting_obj.menu2_on \
                    = menu1(WIN, setting_obj.window_width, setting_obj.window_height, font)

            if setting_obj.menu2_on == True:
                pygame.display.set_mode((setting_obj.window_width, setting_obj.window_height))
                setting_obj.setting_projectile, setting_obj.menu1_on, setting_obj.menu2_on \
                    = menu2(WIN, setting_obj.window_width, setting_obj.window_height,
                            font)

       #=======================================Initialise circle=====================================================#
        setting_obj.window_width = setting_obj.window_size[0][0]
        setting_obj.window_height = setting_obj.window_size[0][1]
        if setting_obj.setting_projectile == "circle" and setting_obj.reset_obj == True:
            red_circle = initiate_circle(setting_obj.setting_motion,setting_obj)
            setting_obj.reset_obj = False

        # ===================================Background==============================================================#
        clock.tick(FPS)
        now_time=time.time()
        setting_obj.delta_time=now_time-prev_time
        prev_time=now_time
        pygame.time.set_timer(pygame.MOUSEBUTTONDOWN,1000)
        WIN = pygame.display.set_mode((setting_obj.window_width, setting_obj.window_height),
                                      flags=pygame.SHOWN | pygame.FULLSCREEN)
        WIN.fill("gray")

        grass = pygame.image.load("grass_img.png")
        setting_rect = pygame.Rect(setting_obj.setting_side_width, 0,
                                   setting_obj.window_width // 3, setting_obj.window_height)
        pygame.draw.rect(WIN, "white", setting_rect, 0)
        WIN.blit(grass, (0, setting_obj.window_height // 1.3))
        setting_label = font4.render("Settings", True, "black")
        setting_label_rect = setting_label.get_rect()
        setting_label_rect.center = (setting_obj.window_width - 320, 70)
        information_label = font3.render("Settings will be saved after reset", True, "black")
        information_label_rect = information_label.get_rect()
        information_label_rect.center = (setting_obj.setting_side_width + 165, 165)
        vel_label = font2.render("Velocity", True, "black")
        vel_label_rect = vel_label.get_rect()
        vel_label_rect.center = (setting_obj.setting_side_width+90, 218)
        angle_label= font2.render("Angle", True, "black")
        angle_label_rect = angle_label.get_rect()
        angle_label_rect.center = (setting_obj.setting_side_width+90, 318)
        WIN.blit(information_label,information_label_rect)
        WIN.blit(angle_label,angle_label_rect)
        WIN.blit(vel_label,vel_label_rect)
        WIN.blit(setting_label,setting_label_rect)
        if setting_obj.initalise_counter==0:
            init_buttons(WIN, setting_obj,red_circle)
            setting_obj.initalise_counter+=1
        if setting_obj.slider_counter==0:
            vel_slider = Slider(WIN, setting_obj.setting_side_width + 200, 200, 200, 30, min=0, max=35, step=1,
                                initial=0)
            output = TextBox(WIN, setting_obj.setting_side_width + 450, 200, 40, 40)
            output.disable()
            angle_slider = Slider(WIN, setting_obj.setting_side_width + 200, 300, 200, 30, min=0, max=90, step=1,
                                  initial=0)
            output2 = TextBox(WIN, setting_obj.setting_side_width + 450, 300, 40, 40)
            output2.disable()
            setting_obj.slider_counter=1
        # =====================================Object is stationary==================================================#



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type==RECORD_EVENT:
                x_coord=red_circle.x_pos
                y_coord=red_circle.y_pos
                coord_list.append([x_coord,y_coord])
                for n in range(len(coord_list)):
                    print(coord_list[n])
        if setting_obj.setting_projectile == "circle":
            if setting_obj.is_run == False:
                red_circle.set_vel(vel_slider.getValue(), angle_slider.getValue())
                if setting_obj.setting_motion == "vertical":
                    pygame.draw.circle(WIN, "red", (red_circle.x_pos, red_circle.y_pos), red_circle.radius,
                                       0)  # set the ball on the border


                elif setting_obj.setting_motion == "horizontal":
                    pygame.draw.circle(WIN, "red", (red_circle.x_pos, red_circle.y_pos), red_circle.radius, 0)





            # ===================================Move object==========================================================#
            elif setting_obj.is_run == True and setting_obj.is_run_after == True:
                for n in coord_list:
                    pygame.draw.circle(WIN,"red",(n[0],n[1]),10,0)
                move_circle(red_circle, WIN, setting_obj)


            if setting_obj.is_run_after == False:
                pygame.draw.circle(WIN, "red", (red_circle.x_pos, red_circle.y_pos), red_circle.radius, 0)

            #====================================Settings tab=========================================================#
            display_information_text(red_circle, WIN)

        output.setText(vel_slider.getValue())
        output2.setText(angle_slider.getValue())
        pygame_widgets.update(pygame.event.get())
        pygame.display.flip()



if __name__ == "__main__":
    main_body()
