import math
import matplotlib.pyplot as plt
import pygame,time,pygame_widgets
from projectiles import initiate_circle, move_circle
from start_menu import menu1, menu2
from Utilities import display_information_text,init_buttons,set_background,init_sliders,Graph









class Settings():
    def __init__(self):
        self.setting_motion = ""
        self.menu1_on = True
        self.menu2_on = False
        self.is_run = False
        self.is_run_after = True
        self.reset_obj = True
        self.close_main1=False
        self.window_size = pygame.display.get_desktop_sizes()
        self.window_width = self.window_size[0][0]
        self.window_height = self.window_size[0][1]
        self.horizontal_width = (self.window_width // 3)*2
        self.setting_side_width=self.window_width-(self.window_width//3.5)
        self.vertical_width=self.window_width//3
        self.bounce=False
        self.delta_time=0
        self.scale=5
        self.base_scale=18
        self.FPS=60
        self.initalise_counter=0
        self.trail_scale=1.2
        self.coord_list=[[],[]]
        self.vertical_displacement_list=[[]]
        self.horizontal_displacement_list=[[]]
        self.displacement_list=[[]]
        self.graph_list_n=0
        self.time_list=[[]]
        self.angle_list=[[]]
        self.vertical_velocity_list=[[]]
        self.speed_list=[[]]
        self.vd_logic_counter1 = 0
        self.vd_logic_counter2 = 0
        self.vv_logic_counter1=0
        self.vv_logic_counter2=0
        self.dt_logic_counter1=0
        self.dt_logic_counter2=0
        self.st_logic_counter1=0
        self.st_logic_counter2=0
        self.ha_logic_counter1=0
        self.ha_logic_counter2=0
        self.ra_logic_counter1=0
        self.ra_logic_counter2=0
        self.displacement_time_counter=0
        self.draw_multiple_graphs=True
        self.pillar_height=0
        self.time_gap=0
        self.colors=["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd",
                     "#8c564b","#e377c2","#7f7f7f","#bcbd22","#17becf"]
        self.lines_counter=0
        self.lines_height=0
        self.lines_displacement=0
        self.lines_displacement_list=[]
        self.lines_height_list=[]


def main_body():
    pygame.init()
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
    trail_timer=9
    trail_base=10
    trail_max=trail_base
    time_gap_counter=0
    time_gap_counter2=1
    displacement_time_prev_time=time.time()
    graphs=Graph()



    while running:  # main game loop
        # ============================================Main Menu=======================================================#
        while setting_obj.menu1_on == True or setting_obj.menu2_on == True:

            if setting_obj.menu1_on == True:
                setting_obj.window_width = 400
                setting_obj.window_height = 400
                pygame.display.set_mode((setting_obj.window_width, setting_obj.window_height))
                menu1(WIN, setting_obj, font)

            if setting_obj.menu2_on == True:
                pygame.display.set_mode((setting_obj.window_width, setting_obj.window_height))
                setting_obj.setting_motion= menu2(WIN, setting_obj, font)

       #=======================================Initialise circle=====================================================#
        setting_obj.window_width = setting_obj.window_size[0][0]
        setting_obj.window_height = setting_obj.window_size[0][1]
        if setting_obj.reset_obj == True:
            red_circle = initiate_circle(setting_obj.setting_motion,setting_obj)
            setting_obj.initial_y=red_circle.y_pos
            setting_obj.initial_x=red_circle.x_pos
            setting_obj.reset_obj = False


        # ===================================Background==============================================================#
        clock.tick(setting_obj.FPS)
        if setting_obj.is_run_after:
            trail_timer+=1

        now_time=time.time()
        setting_obj.delta_time=now_time-prev_time
        prev_time=now_time
        WIN = pygame.display.set_mode((setting_obj.window_width, setting_obj.window_height),
                                      flags=pygame.SHOWN | pygame.FULLSCREEN)
        WIN.fill("#46aefc")

        if setting_obj.initalise_counter==0:
            vertical_displacement_graph_toggle,vertical_velocity_graph_toggle,multiple_graphs_toggle,axes_toggle,\
                displacement_graph_toggle,speed_graph_toggle,height_graph_toggle,range_graph_toggle,bounce_toggle\
                =init_buttons(WIN, setting_obj,red_circle,graphs)
            setting_obj.initalise_counter+=1
        if slider_counter==0:
            vel_slider,output,angle_slider,output2,zoom_slider,output3,pillar_slider,output4,friction_slider,output5\
                =init_sliders(WIN,setting_obj)
            slider_counter = 1



#=============================================RECORD DATA FOR GRAPHS==================================================#
        if trail_timer == trail_max:
            trail_timer = 0
            if setting_obj.is_run and not red_circle.stop_y_motion:
                setting_obj.coord_list[0].append(red_circle.x_pos)
                setting_obj.coord_list[1].append(red_circle.y_pos)

        if setting_obj.is_run:
            if not red_circle.stop_y_motion and setting_obj.is_run_after:
                height= (setting_obj.initial_y - red_circle.y_pos)/setting_obj.base_scale
                length=red_circle.x_pos/setting_obj.base_scale
                graph_displacement=math.sqrt((length**2)+(height**2))
                setting_obj.vertical_displacement_list[setting_obj.graph_list_n].append(height / setting_obj.scale)
                setting_obj.horizontal_displacement_list[setting_obj.graph_list_n].append(length/setting_obj.scale)
                setting_obj.angle_list[setting_obj.graph_list_n].append(red_circle.delta_theta)
                displacement_time_now_time = time.time()
                displacement_time_delta_time = displacement_time_now_time - displacement_time_prev_time

                setting_obj.time_list[setting_obj.graph_list_n].append(
                    displacement_time_delta_time-setting_obj.time_gap)
                setting_obj.vertical_velocity_list[setting_obj.graph_list_n].append(red_circle.vertical_vel)
                setting_obj.displacement_list[setting_obj.graph_list_n].append(graph_displacement)
                setting_obj.speed_list[setting_obj.graph_list_n].append(red_circle.current_velocity)


#===================================================================================================================]



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()



        if setting_obj.is_run == False:
            red_circle.set_vel(vel_slider.getValue(), angle_slider.getValue())
            red_circle.drag_coefficient=friction_slider.getValue()

            if setting_obj.setting_motion == "vertical":
                pygame.draw.circle(WIN, "red", (red_circle.x_pos, red_circle.y_pos), red_circle.radius,
                                       0)  # set the ball on the border



            elif setting_obj.setting_motion == "horizontal":
                red_circle.y_pos = setting_obj.window_height // 1.3 - setting_obj.pillar_height * setting_obj.base_scale - \
                                       red_circle.radius
                pygame.draw.circle(WIN, "red", (red_circle.x_pos, red_circle.y_pos), red_circle.radius, 0)





#===============================================Move object==========================================================#


        elif setting_obj.is_run == True and setting_obj.is_run_after == True:
            if setting_obj.displacement_time_counter==0:
                isplacement_time_prev_time=time.time()
                setting_obj.displacement_time_counter=1
            move_circle(red_circle, WIN, setting_obj)


        if setting_obj.is_run_after == False:
            pygame.draw.circle(WIN, "red", (red_circle.x_pos, red_circle.y_pos), red_circle.radius, 0)

        if not setting_obj.is_run_after:
            if time_gap_counter==0:
                time_gap_start=time.time()
                time_gap_counter=1
                time_gap_counter2=0
        else:
            if time_gap_counter2==0:
                time_gap_end=time.time()-time_gap_start
                setting_obj.time_gap+=time_gap_end
                time_gap_counter=0
                time_gap_counter2=1

#=====================================DRAW PATH======================================================================#

        for n in range(len(setting_obj.coord_list[0])):
            pygame.draw.circle(WIN, "red", (setting_obj.coord_list[0][n],
                                            setting_obj.coord_list[1][n]), 5, 0)



#=================================================GRAPHS=============================================================#


        if vertical_displacement_graph_toggle.getValue()==True and not vertical_velocity_graph_toggle.getValue():
            graphs.create_graph_vd(WIN,setting_obj)
            graphs.plot_vertical_displacement(setting_obj)
        elif not vertical_displacement_graph_toggle.getValue():
            if setting_obj.vd_logic_counter2==0:
                plt.close(graphs.fig_vd)
                setting_obj.vd_logic_counter2+=1
                setting_obj.vd_logic_counter1=0



        if vertical_velocity_graph_toggle.getValue() and not vertical_displacement_graph_toggle.getValue():
            graphs.create_graph_vv(WIN,setting_obj)
            graphs.plot_vertical_velocity(setting_obj)
        elif not vertical_velocity_graph_toggle.getValue():
            if setting_obj.vv_logic_counter2 == 0:
                setting_obj.vv_logic_counter2 += 1
                setting_obj.vv_logic_counter1 = 0
                plt.close(graphs.fig_vv)

        if displacement_graph_toggle.getValue() and not speed_graph_toggle.getValue():
            graphs.create_graph_dt(WIN, setting_obj)
            graphs.plot_displacement(setting_obj)
        elif not displacement_graph_toggle.getValue():
            if setting_obj.dt_logic_counter2 == 0:
                setting_obj.dt_logic_counter2 += 1
                setting_obj.dt_logic_counter1 = 0
                plt.close(graphs.fig_dt)

        if speed_graph_toggle.getValue() and not displacement_graph_toggle.getValue():
            graphs.create_graph_st(WIN, setting_obj)
            graphs.plot_speed(setting_obj)
        elif not speed_graph_toggle.getValue():
            if setting_obj.st_logic_counter2 == 0:
                setting_obj.st_logic_counter2 += 1
                setting_obj.st_logic_counter1 = 0
                plt.close(graphs.fig_st)

        if height_graph_toggle.getValue() and not range_graph_toggle.getValue():
            graphs.create_graph_ha(WIN, setting_obj)
            graphs.plot_height_angle(setting_obj)
        elif not height_graph_toggle.getValue():
            if setting_obj.ha_logic_counter2 == 0:
                setting_obj.ha_logic_counter2 += 1
                setting_obj.ha_logic_counter1 = 0
                plt.close(graphs.fig_ha)

        if range_graph_toggle.getValue() and not height_graph_toggle.getValue():
            graphs.create_graph_ra(WIN, setting_obj)
            graphs.plot_range_angle(setting_obj)
        elif not range_graph_toggle.getValue():
            if setting_obj.ra_logic_counter2 == 0:
                setting_obj.ra_logic_counter2 += 1
                setting_obj.ra_logic_counter1 = 0
                plt.close(graphs.fig_ra)



        ##====================================================================================================================#

        if zoom_slider.getValue()==0:
            setting_obj.scale=setting_obj.base_scale
            trail_max=trail_base
        elif setting_obj.setting_motion=="horizontal":
            setting_obj.scale=setting_obj.base_scale*zoom_slider.getValue()
            trail_max=round(trail_base*(setting_obj.trail_scale/zoom_slider.getValue()),0)
            if trail_timer>trail_max:
                trail_timer=0


        if multiple_graphs_toggle.getValue():
            setting_obj.draw_multiple_graphs=True
        else:
            setting_obj.draw_multiple_graphs=False
        setting_obj.pillar_height=pillar_slider.getValue()
        pillar_rect = pygame.Rect(40, setting_obj.window_height//1.3-
                                  (setting_obj.pillar_height*setting_obj.base_scale),
                                   red_circle.radius, setting_obj.pillar_height*setting_obj.base_scale)
        if setting_obj.setting_motion=="horizontal":
            pygame.draw.rect(WIN,"brown",pillar_rect)
        set_background(setting_obj, WIN, font4, font3, font2)
        if not red_circle.y_pos-20<=0 and red_circle.vertical_vel>=0 and not red_circle.stop_y_motion:
            setting_obj.lines_height = red_circle.y_pos
        if red_circle.horizontal_vel >= 0 and not red_circle.x_pos + 50 >= setting_obj.setting_side_width:
            setting_obj.lines_displacement = red_circle.x_pos

        if axes_toggle.getValue() and setting_obj.setting_motion=="horizontal":

            if not setting_obj.is_run:
                y_ax=pygame.rect.Rect(30,setting_obj.window_height//1.3,10,0)
            else:
                y_ax=pygame.rect.Rect(30,setting_obj.lines_height,10,
                                        setting_obj.window_height//1.3-setting_obj.lines_height+1)
            pygame.draw.rect(WIN,"black",y_ax,5,0)
            if red_circle.stop_y_motion:
                if (setting_obj.window_height//1.3)-setting_obj.lines_height < 100:
                    height_iterator = round(((setting_obj.window_height//1.3)-setting_obj.lines_height)/ 10)
                else:
                    height_iterator = round(((setting_obj.window_height//1.3)-setting_obj.lines_height) / 100)
                for n in range(height_iterator+1):
                    temp_height = ((setting_obj.window_height//1.3-setting_obj.lines_height)/height_iterator) * n
                    sub_y_ax = pygame.rect.Rect(20,setting_obj.window_height//1.3-temp_height, 14, 5)
                    pygame.draw.rect(WIN, "black", sub_y_ax, 5, 0)
                    y_axis_ticks = font5.render(f"{round(temp_height/ setting_obj.scale)}m", True, "black")
                    y_axis_ticks_rect = y_axis_ticks.get_rect()
                    y_axis_ticks_rect.center = (10, setting_obj.window_height//1.3-temp_height)
                    WIN.blit(y_axis_ticks, y_axis_ticks_rect)

        if axes_toggle.getValue() and setting_obj.setting_motion=="horizontal":

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
                    x_axis_ticks=font5.render(f"{round(temp_displacement/setting_obj.scale)}m",True,"black")
                    x_axis_ticks_rect=x_axis_ticks.get_rect()
                    x_axis_ticks_rect.center=(temp_displacement+35,setting_obj.window_height//1.3+27)
                    WIN.blit(x_axis_ticks,x_axis_ticks_rect)

            x_ax=pygame.rect.Rect(30,setting_obj.window_height//1.3,setting_obj.lines_displacement,10)
            pygame.draw.rect(WIN,"black",x_ax,5,0)

        setting_obj.bounce=bounce_toggle.getValue()



        display_information_text(red_circle, WIN,setting_obj)
        output.setText(vel_slider.getValue())
        output2.setText(angle_slider.getValue())
        output3.setText(zoom_slider.getValue())
        output4.setText(pillar_slider.getValue())
        output5.setText(round(friction_slider.getValue(),2))
        pygame_widgets.update(pygame.event.get())
        pygame.display.flip()



if __name__ == "__main__":
    main_body()
