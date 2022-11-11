import matplotlib.pyplot as plt
import pygame,time,pygame_widgets
from projectiles import initiate_circle, move_circle
from start_menu import menu1, menu2
from Utilities import display_information_text,init_buttons,set_background,init_sliders,Graph







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
        self.setting_side_width=self.window_width-(self.window_width//3.5)
        self.vertical_width=self.window_width//3
        self.bounce=False
        self.delta_time=0
        self.scale=10
        self.base_scale=10
        self.FPS=60
        self.initalise_counter=0
        self.coord_list=[[],[]]
        self.displacement_list=[[]]
        self.graph_list_n=0
        self.time_list=[[]]
        self.velocity_list=[[]]
        self.graph_logic_counter2 = 0
        self.graph_logic_counter3 = 0
        self.displacement_time_counter=0
        self.draw_multiple_graphs=True
        self.pillar_height=0
        self.colors=["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd",
                     "#8c564b","#e377c2","#7f7f7f","#bcbd22","#17becf"]
        self.lines_counter=0
        self.lines_height=0
        self.lines_displacement=0
        self.lines_displacement_list=[]
        self.lines_height_list=[]
def main_body():
    setting_obj = Settings()
    setting_obj.window_width = 400
    setting_obj.window_height = 400
    font = pygame.font.Font("freesansbold.ttf", 26)
    font2 = pygame.font.Font("freesansbold.ttf", 24)
    font3=pygame.font.Font("freesansbold.ttf", 14)
    font4=pygame.font.Font("freesansbold.ttf",46)
    font5=pygame.font.Font("freesansbold.ttf",10)
    cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.mouse.set_cursor(cursor)
    slider_counter=0
    running = True  # condition for game loop
    WIN = pygame.display.set_mode((setting_obj.window_width, setting_obj.window_height))
    prev_time=time.time()
    clock = pygame.time.Clock()
    secondary_timer=14
    record_timer=4
    displacement_time_prev_time=time.time()
    graphs=Graph()


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
            setting_obj.initial_y=red_circle.y_pos
            setting_obj.reset_obj = False


        # ===================================Background==============================================================#
        clock.tick(setting_obj.FPS)
        if setting_obj.is_run_after:
            secondary_timer+=1
            record_timer+=1
        now_time=time.time()
        setting_obj.delta_time=now_time-prev_time
        prev_time=now_time
        WIN = pygame.display.set_mode((setting_obj.window_width, setting_obj.window_height),
                                      flags=pygame.SHOWN | pygame.FULLSCREEN)
        WIN.fill("#46aefc")

        if setting_obj.initalise_counter==0:
            displacement_graph_toggle,velocity_graph_toggle,multiple_graphs_toggle,axes_toggle\
                =init_buttons(WIN, setting_obj,red_circle,graphs)
            setting_obj.initalise_counter+=1
        if slider_counter==0:
            vel_slider,output,angle_slider,output2,zoom_slider,output3,pillar_slider,output4\
                =init_sliders(WIN,setting_obj)
            slider_counter = 1

        # =====================================Object is stationary==================================================#
        if secondary_timer == 15:
            secondary_timer = 0
            if setting_obj.is_run and not red_circle.stop_y_motion:
                setting_obj.coord_list[0].append(red_circle.x_pos)
                setting_obj.coord_list[1].append(red_circle.y_pos)
        if record_timer==5:
            record_timer=0
            if setting_obj.is_run:
               if not red_circle.stop_y_motion:
                   y_pos = setting_obj.initial_y - red_circle.y_pos
                   setting_obj.displacement_list[setting_obj.graph_list_n].append(y_pos / setting_obj.scale)
                   displacement_time_now_time = time.time()
                   displacement_time_delta_time = displacement_time_now_time - displacement_time_prev_time
                   setting_obj.time_list[setting_obj.graph_list_n].append(displacement_time_delta_time)
                   setting_obj.velocity_list[setting_obj.graph_list_n].append(red_circle.vertical_vel)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()




        if setting_obj.setting_projectile == "circle":
            if setting_obj.is_run == False:
                red_circle.set_vel(vel_slider.getValue(), angle_slider.getValue())
                if setting_obj.setting_motion == "vertical":
                    pygame.draw.circle(WIN, "red", (red_circle.x_pos, red_circle.y_pos), red_circle.radius,
                                       0)  # set the ball on the border


                elif setting_obj.setting_motion == "horizontal":
                    red_circle.y_pos = setting_obj.window_height // 1.3 - setting_obj.pillar_height * setting_obj.base_scale - \
                                       red_circle.radius
                    pygame.draw.circle(WIN, "red", (red_circle.x_pos, red_circle.y_pos), red_circle.radius, 0)





            # ===================================Move object==========================================================#
            elif setting_obj.is_run == True and setting_obj.is_run_after == True:
                if setting_obj.displacement_time_counter==0:
                    displacement_time_prev_time=time.time()
                    setting_obj.displacement_time_counter+=1
                move_circle(red_circle, WIN, setting_obj)


            if setting_obj.is_run_after == False:
                pygame.draw.circle(WIN, "red", (red_circle.x_pos, red_circle.y_pos), red_circle.radius, 0)


            #====================================Settings tab=========================================================#
        for n in range(len(setting_obj.coord_list[0])):
            pygame.draw.circle(WIN, "red", (setting_obj.coord_list[0][n],
                                            setting_obj.coord_list[1][n]), 5, 0)

        if displacement_graph_toggle.getValue()==True and not velocity_graph_toggle.getValue():
            graphs.create_graph(WIN,setting_obj)
            graphs.plot_displacement(setting_obj)

        if velocity_graph_toggle.getValue() and not displacement_graph_toggle.getValue():
            graphs.create_graph(WIN,setting_obj)
            graphs.plot_velocity(setting_obj)

        if not displacement_graph_toggle.getValue() and not velocity_graph_toggle.getValue():
            if setting_obj.graph_logic_counter3==0:
                plt.close("all")
                setting_obj.graph_logic_counter3+=1
                setting_obj.graph_logic_counter2=0
        if zoom_slider.getValue()==0:
            setting_obj.scale=setting_obj.base_scale
        else:
            setting_obj.scale=setting_obj.base_scale*zoom_slider.getValue()

        if multiple_graphs_toggle.getValue():
            setting_obj.draw_multiple_graphs=True
        else:
            setting_obj.draw_multiple_graphs=False
        setting_obj.pillar_height=pillar_slider.getValue()
        pillar_rect = pygame.Rect(40, setting_obj.window_height//1.3-
                                  (setting_obj.pillar_height*setting_obj.base_scale),
                                   red_circle.radius, setting_obj.pillar_height*setting_obj.base_scale)

        pygame.draw.rect(WIN,"brown",pillar_rect)
        set_background(setting_obj, WIN, font4, font3, font2)

        if axes_toggle.getValue() and setting_obj.setting_motion=="horizontal":
            if red_circle.vertical_vel>=0 and not red_circle.stop_y_motion\
                and not red_circle.y_pos-20<=0:
                setting_obj.lines_height=red_circle.y_pos
            if not setting_obj.is_run:
                y_ax=pygame.rect.Rect(30,setting_obj.window_height//1.3,10,0)
            else:
                y_ax=pygame.rect.Rect(30,setting_obj.lines_height,10,
                                        setting_obj.window_height//1.3-setting_obj.lines_height+1)
            pygame.draw.rect(WIN,"black",y_ax,5,0)
            if red_circle.stop_y_motion:
                if setting_obj.window_height//1.3-setting_obj.lines_height < 100:
                    height_iterator = round(setting_obj.window_height//1.3-setting_obj.lines_height / 10)
                else:
                    height_iterator = round(setting_obj.window_height//1.3-setting_obj.lines_height / 100)
                for n in range(height_iterator):
                    temp_height = ((setting_obj.window_height//1.3-setting_obj.lines_height)/height_iterator) * n
                    sub_y_ax = pygame.rect.Rect(20,setting_obj.window_height//1.3-temp_height, 14, 5)
                    pygame.draw.rect(WIN, "black", sub_y_ax, 5, 0)
                    y_axis_ticks = font5.render(f"{round(temp_height/ setting_obj.scale)}", True, "black")
                    y_axis_ticks_rect = y_axis_ticks.get_rect()
                    y_axis_ticks_rect.center = (10, setting_obj.window_height//1.3-temp_height)
                    WIN.blit(y_axis_ticks, y_axis_ticks_rect)

        if axes_toggle.getValue() and setting_obj.setting_motion=="horizontal":
            if red_circle.horizontal_vel>=0 and not red_circle.stop_y_motion\
                    and not red_circle.x_pos+50>=setting_obj.setting_side_width:
                setting_obj.lines_displacement=red_circle.x_pos
            if not setting_obj.is_run:
                setting_obj.lines_displacement = 0
            if red_circle.stop_y_motion:
                if setting_obj.lines_displacement<100:
                    displacement_iterator=round(setting_obj.lines_displacement/10)
                else:
                    displacement_iterator=round(setting_obj.lines_displacement / 100)
                for n in range(displacement_iterator+1):
                    temp_displacement=(setting_obj.lines_displacement/displacement_iterator)*n
                    sub_x_ax=pygame.rect.Rect(temp_displacement+30
                                                ,setting_obj.window_height//1.3,6,20)
                    pygame.draw.rect(WIN, "black", sub_x_ax, 5, 0)
                    x_axis_ticks=font5.render(f"{round(temp_displacement/setting_obj.scale)}",True,"black")
                    x_axis_ticks_rect=x_axis_ticks.get_rect()
                    x_axis_ticks_rect.center=(temp_displacement+35,setting_obj.window_height//1.3+27)
                    WIN.blit(x_axis_ticks,x_axis_ticks_rect)

            x_ax=pygame.rect.Rect(30,setting_obj.window_height//1.3,setting_obj.lines_displacement,10)
            pygame.draw.rect(WIN,"black",x_ax,5,0)
        display_information_text(red_circle, WIN,setting_obj)
        output.setText(vel_slider.getValue())
        output2.setText(angle_slider.getValue())
        output3.setText(zoom_slider.getValue())
        output4.setText(pillar_slider.getValue())
        pygame_widgets.update(pygame.event.get())
        pygame.display.flip()



if __name__ == "__main__":
    main_body()
