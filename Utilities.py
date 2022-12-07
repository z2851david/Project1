import pygame
import matplotlib
matplotlib.use('module://pygame_matplotlib.backend_pygame')
import matplotlib.pyplot as plt
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.toggle import Toggle

class Graph():

    def __init__(self):
        self.fig_st, self.ax_st = plt.subplots(figsize=(450, 300), dpi=1, facecolor="#46aefc")
        self.fig_vv, self.ax_vv = plt.subplots(figsize=(450, 300), dpi=1, facecolor="#46aefc")
        self.fig_vd, self.ax_vd = plt.subplots(figsize=(450, 300), dpi=1, facecolor="#46aefc")
        self.fig_dt, self.ax_dt = plt.subplots(figsize=(450, 300), dpi=1, facecolor="#46aefc")
        self.fig_ha, self.ax_ha = plt.subplots(figsize=(450, 300), dpi=1, facecolor="#46aefc")
        self.fig_ra, self.ax_ra = plt.subplots(figsize=(450, 300), dpi=1, facecolor="#46aefc")



    def plot_vertical_displacement(self,setting_obj):
        for n in range(len(setting_obj.vertical_displacement_list)):
            self.ax_vd.plot(setting_obj.time_list[n],setting_obj.vertical_displacement_list[n],color=setting_obj.colors[n])
            self.ax_vd.set_ylabel("Displacement/m",c="red")
            self.ax_vd.set_xlabel("Time/s",c="red")
            self.ax_vd.xaxis.set_label_coords(1,-0.01)
            self.ax_vd.yaxis.set_label_coords(0.05,1)



    def plot_vertical_velocity(self,setting_obj):
        for n in range(len(setting_obj.vertical_velocity_list)):
            self.ax_vv.plot(setting_obj.time_list[n],setting_obj.vertical_velocity_list[n],color=setting_obj.colors[n])
            self.ax_vv.set_ylabel("vertical velocity/ms^-1",c="red")
            self.ax_vv.set_xlabel("Time/s",c="red")
            self.ax_vv.xaxis.set_label_coords(1,-0.01)
            self.ax_vv.yaxis.set_label_coords(0.05,1)

    def plot_displacement(self,setting_obj):
        for n in range(len(setting_obj.displacement_list)):
            self.ax_dt.plot(setting_obj.time_list[n],setting_obj.displacement_list[n],color=setting_obj.colors[n])
            self.ax_dt.set_ylabel("displacement/m",c="red")
            self.ax_dt.set_xlabel("time/s",c="red")
            self.ax_dt.xaxis.set_label_coords(1,-0.01)
            self.ax_dt.yaxis.set_label_coords(0.05,1)
    def plot_speed(self,setting_obj):
        for n in range(len(setting_obj.speed_list)):
            self.ax_st.plot(setting_obj.time_list[n],setting_obj.speed_list[n],color=setting_obj.colors[n])
            self.ax_st.set_ylabel("speed/ms^-1",c="red")
            self.ax_st.set_xlabel("time/s",c="red")
            self.ax_st.xaxis.set_label_coords(1,-0.01)
            self.ax_st.yaxis.set_label_coords(0.05,1)
    def plot_height_angle(self,setting_obj):
        for n in range(len(setting_obj.angle_list)):
            self.ax_ha.plot(setting_obj.angle_list[n],setting_obj.vertical_displacement_list[n],color=setting_obj.colors[n])
            self.ax_ha.set_ylabel("vertical displacement/m",c="red")
            self.ax_ha.set_xlabel("theta/rad",c="red")
            self.ax_ha.xaxis.set_label_coords(1,-0.01)
            self.ax_ha.yaxis.set_label_coords(0.05,1)
    def plot_range_angle(self,setting_obj):
        for n in range(len(setting_obj.angle_list)):
            self.ax_ra.plot(setting_obj.angle_list[n],setting_obj.horizontal_displacement_list[n],color=setting_obj.colors[n])
            self.ax_ra.set_ylabel("horizontal displacement/m",c="red")
            self.ax_ra.set_xlabel("theta/rad",c="red")
            self.ax_ra.xaxis.set_label_coords(1,-0.01)
            self.ax_ra.yaxis.set_label_coords(0.05,1)



    def clear(self):
        self.ax_vd.cla()
        self.ax_vv.cla()
        self.ax_dt.cla()
        self.ax_st.cla()
        self.ax_ha.cla()
        self.ax_ra.cla()


    def create_graph_vd(self,WIN,setting_obj):
        if setting_obj.vd_logic_counter1 == 0:
            setting_obj.vd_logic_counter1 += 1
            setting_obj.vd_logic_counter2 = 0
        WIN.blit(self.fig_vd,(setting_obj.setting_side_width*0.001,-20))
        self.fig_vd.canvas.draw()


    def create_graph_vv(self,WIN,setting_obj):
        if setting_obj.vv_logic_counter1 == 0:
            setting_obj.vv_logic_counter1 += 1
            setting_obj.vv_logic_counter2 = 0
        WIN.blit(self.fig_vv,(setting_obj.setting_side_width*0.001,-20))
        self.fig_vv.canvas.draw()

    def create_graph_dt(self,WIN,setting_obj):
        if setting_obj.dt_logic_counter1 == 0:
            setting_obj.dt_logic_counter1 += 1
            setting_obj.dt_logic_counter1 = 0
        WIN.blit(self.fig_dt,(setting_obj.setting_side_width*0.31,-20))
        self.fig_dt.canvas.draw()

    def create_graph_st(self,WIN,setting_obj):
        if setting_obj.st_logic_counter1 == 0:
            setting_obj.st_logic_counter1 += 1
            setting_obj.st_logic_counter2 = 0
        WIN.blit(self.fig_st,(setting_obj.setting_side_width*0.31,-20))
        self.fig_st.canvas.draw()

    def create_graph_ha(self,WIN,setting_obj):
        if setting_obj.ha_logic_counter1 == 0:
            setting_obj.ha_logic_counter1 += 1
            setting_obj.ha_logic_counter2 = 0
        WIN.blit(self.fig_ha,(setting_obj.setting_side_width*0.65,-20))
        self.fig_ha.canvas.draw()

    def create_graph_ra(self,WIN,setting_obj):
        if setting_obj.ra_logic_counter1 == 0:
            setting_obj.ra_logic_counter1 += 1
            setting_obj.ra_logic_counter2 = 0
        WIN.blit(self.fig_ra,(setting_obj.setting_side_width*0.65,-20))
        self.fig_ra.canvas.draw()






def init_buttons(WIN,setting_obj,red_circle,graphs):
    start_stop_button = Button(WIN, setting_obj.setting_side_width + setting_obj.vertical_width*0.01,
                          setting_obj.window_height *0.85, 80, 80, text="Start/Stop",
                          onClick=lambda: start_stop_button_func(setting_obj),
                          fontSize=24)
    vertical_displacement_graph_toggle = Toggle(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.27),
                          int(setting_obj.window_height*0.35),30,24,startOn=False)

    velocity_graph_toggle=Toggle(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.26),
                                 int(setting_obj.window_height*0.435),30,24,startOn=False)

    displacement_graph_toggle=Toggle(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.51),
                          int(setting_obj.window_height*0.3485),30,24,startOn=False)
    speed_graph_toggle=Toggle(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.51),
                          int(setting_obj.window_height*0.4375),30,24,startOn=False)
    height_graph_toggle=Toggle(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.7),
                          int(setting_obj.window_height*0.3485),30,24,startOn=False)
    range_graph_toggle=Toggle(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.7),
                          int(setting_obj.window_height*0.4375),30,24,startOn=False)

    multiple_graphs_toggle=Toggle(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.55),
                                  int(setting_obj.window_height*0.63),30,24,startOn=False)


    menu_button = Button(WIN, setting_obj.setting_side_width + setting_obj.vertical_width*0.43,
        setting_obj.window_height *0.85, 80, 80, text="Menu", onClick=lambda: menu_button_func(setting_obj),
        fontSize=24)

    exit_button = Button(WIN, setting_obj.setting_side_width + setting_obj.vertical_width*0.64,
        setting_obj.window_height * 0.85, 80, 80, text="Exit", onClick=lambda: quit(),
        fontSize=24)

    restart_button = Button(WIN,setting_obj.setting_side_width + setting_obj.vertical_width*0.22,
                            setting_obj.window_height*0.85, 80, 80,
                            text="Reset", onClick=lambda: restart_button_func(setting_obj, red_circle,
                                                                              graphs),
                            fontSize=24)
    axes_toggle=Toggle(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.27),
                       int(setting_obj.window_height*0.79),30,24,startOn=False)
    return vertical_displacement_graph_toggle,velocity_graph_toggle,multiple_graphs_toggle,axes_toggle,\
           displacement_graph_toggle,speed_graph_toggle,height_graph_toggle,range_graph_toggle

def init_sliders(WIN,setting_obj):
    vel_slider = Slider(WIN, int(setting_obj.setting_side_width + setting_obj.vertical_width * 0.32),
                        int(setting_obj.window_height * 0.15),
                        setting_obj.vertical_width * 0.37, 20
                        , min=0, max=35, step=1,
                        initial=0)
    output = TextBox(WIN, setting_obj.setting_side_width + setting_obj.vertical_width*0.74,
                     setting_obj.window_height * 0.14
                     , 40, 40)
    output.disable()
    angle_slider = Slider(WIN, int(setting_obj.setting_side_width + setting_obj.vertical_width * 0.32),
                          int(setting_obj.window_height * 0.215), setting_obj.vertical_width * 0.37,
                          20,
                          min=0, max=90, step=1,
                          initial=0)
    output2 = TextBox(WIN, setting_obj.setting_side_width + setting_obj.vertical_width * 0.74,
                      int(setting_obj.window_height * 0.205), 40
                      , 40)
    output2.disable()

    zoom_slider = Slider(WIN, int(setting_obj.setting_side_width + setting_obj.vertical_width * 0.32),
                           int(setting_obj.window_height * 0.525),setting_obj.vertical_width*0.37,20,
                         min=0,max=15,step=1,initial=0)
    output3=TextBox(WIN,setting_obj.setting_side_width+setting_obj.vertical_width*0.74,
                    int(setting_obj.window_height*0.51),40,40)
    output3.disable()

    pillar_slider=Slider(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.32),
                         int(setting_obj.window_height*0.722),setting_obj.vertical_width*0.37,20,
                         min=0,max=30,step=1,initial=0)
    output4=TextBox(WIN,setting_obj.setting_side_width+setting_obj.vertical_width*0.74,
                    int(setting_obj.window_height*0.71),40,40)
    output4.disable()

    friction_slider=Slider(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.32),
                         int(setting_obj.window_height*0.282),setting_obj.vertical_width*0.37,20,
                         min=0,max=1,step=0.05,initial=0)
    output5=TextBox(WIN,setting_obj.setting_side_width+setting_obj.vertical_width*0.74,
                    int(setting_obj.window_height*0.273),40,40)
    output5.disable()


    return vel_slider,output,angle_slider,output2,zoom_slider,output3,pillar_slider,output4,friction_slider,output5








def start_stop_button_func(setting_obj):
    if setting_obj.is_run==False:
        setting_obj.is_run=True
    elif setting_obj.is_run_after==True and setting_obj.is_run==True:
        setting_obj.is_run_after=False
    elif setting_obj.is_run_after==False:
        setting_obj.is_run_after=True





def restart_button_func(setting_obj,red_circle,graphs):
    setting_obj.reset_obj = True
    setting_obj.is_run = False
    setting_obj.is_run_after=True
    if not setting_obj.draw_multiple_graphs:
        setting_obj.vertical_displacement_list=[[]]
        setting_obj.time_list=[[]]
        setting_obj.vertical_velocity_list=[[]]
        setting_obj.displacement_list=[[]]
        setting_obj.angle_list=[[]]
        setting_obj.horizontal_displacement_list=[[]]
        setting_obj.speed_list=[[]]
        setting_obj.graph_list_n=0

    else:
        setting_obj.vertical_displacement_list.append([])
        setting_obj.horizontal_displacement_list.append([])
        setting_obj.displacement_list.append([])
        setting_obj.vertical_velocity_list.append([])
        setting_obj.angle_list.append([])
        setting_obj.speed_list.append([])
        setting_obj.time_list.append([])
        setting_obj.graph_list_n+=1
    setting_obj.coord_list=[[],[]]
    setting_obj.displacement_time_counter=0
    setting_obj.lines_displacement_list=[]
    setting_obj.lines_height_list=[]
    graphs.clear()
    red_circle.__del__()




def set_background(setting_obj,WIN,font4,font3,font2):
    setting_rect = pygame.Rect(setting_obj.setting_side_width, 0,
                               setting_obj.window_width // 3, setting_obj.window_height)
    grass_rect = pygame.Rect(0, setting_obj.window_height // 1.3, setting_obj.setting_side_width,
                             setting_obj.window_height // 3)
    pygame.draw.rect(WIN, "white", setting_rect, 0)
    pygame.draw.rect(WIN, "green", grass_rect, 0)
    setting_label = font4.render("Settings", True, "black")
    setting_label_rect = setting_label.get_rect()
    setting_label_rect.center = (setting_obj.setting_side_width + setting_obj.vertical_width * 0.45,
                                 setting_obj.window_height * 0.055)
    information_label = font3.render("(Press 'reset' to save changes)", True, "black")
    information_label_rect = information_label.get_rect()
    information_label_rect.center = (setting_obj.setting_side_width + setting_obj.vertical_width * 0.44,
                                     setting_obj.window_height * 0.1)
    vel_label = font2.render("Velocity", True, "black")
    vel_label_rect = vel_label.get_rect()
    vel_label_rect.center = (setting_obj.setting_side_width + setting_obj.vertical_width * 0.14,
                             setting_obj.window_height * 0.16)
    angle_label = font2.render("Angle", True, "black")
    angle_label_rect = angle_label.get_rect()
    angle_label_rect.center = (setting_obj.setting_side_width + setting_obj.vertical_width * 0.12,
                               int(setting_obj.window_height * 0.225))

    graph_label_part1 = font2.render("Toggle", True, "black")
    graph_rect_part1 = graph_label_part1.get_rect()
    graph_rect_part1.center = (setting_obj.setting_side_width + setting_obj.vertical_width * 0.095,
                               int(setting_obj.window_height * 0.4))
    graph_label_part2 = font2.render("Graphs", True, "black")
    graph_rect_part2 = graph_label_part1.get_rect()
    graph_rect_part2.center = (setting_obj.setting_side_width + setting_obj.vertical_width * 0.09,
                               int(setting_obj.window_height * 0.43))
    label_under_toggle1_part1=font3.render("vertical displacement/", True, "black")
    rect_under_toggle1_part1=label_under_toggle1_part1.get_rect()
    rect_under_toggle1_part1.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.3,
                                     setting_obj.window_height * 0.39)
    label_under_toggle1_part2=font3.render("time", True, "black")
    rect_under_toggle1_part2=label_under_toggle1_part2.get_rect()
    rect_under_toggle1_part2.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.29,
                                     setting_obj.window_height * 0.405)
    label_under_toggle2_part1=font3.render("vertical velocity/", True, "black")
    rect_under_toggle2_part1=label_under_toggle2_part1.get_rect()
    rect_under_toggle2_part1.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.28,
                                     setting_obj.window_height * 0.47)
    label_under_toggle2_part2=font3.render("time", True, "black")
    rect_under_toggle2_part2=label_under_toggle2_part2.get_rect()
    rect_under_toggle2_part2.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.29,
                                     setting_obj.window_height * 0.485)

    label_under_toggle3_part1=font3.render("displacement/", True, "black")
    rect_under_toggle3_part1=label_under_toggle3_part1.get_rect()
    rect_under_toggle3_part1.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.53,
                                     setting_obj.window_height * 0.39)
    label_under_toggle3_part2=font3.render("time", True, "black")
    rect_under_toggle3_part2=label_under_toggle3_part2.get_rect()
    rect_under_toggle3_part2.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.53,
                                     setting_obj.window_height * 0.405)

    label_under_toggle4_part1=font3.render("Speed/", True, "black")
    rect_under_toggle4_part1=label_under_toggle4_part1.get_rect()
    rect_under_toggle4_part1.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.53,
                                     setting_obj.window_height * 0.473)
    label_under_toggle4_part2=font3.render("time", True, "black")
    rect_under_toggle4_part2=label_under_toggle4_part2.get_rect()
    rect_under_toggle4_part2.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.53,
                                     setting_obj.window_height * 0.4875)

    label_under_toggle5_part1=font3.render("displacement/", True, "black")
    rect_under_toggle5_part1=label_under_toggle5_part1.get_rect()
    rect_under_toggle5_part1.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.73,
                                     setting_obj.window_height * 0.39)
    label_under_toggle5_part2=font3.render("time", True, "black")
    rect_under_toggle5_part2=label_under_toggle5_part2.get_rect()
    rect_under_toggle5_part2.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.73,
                                     setting_obj.window_height * 0.405)

    label_under_toggle6_part1=font3.render("Speed/", True, "black")
    rect_under_toggle6_part1=label_under_toggle6_part1.get_rect()
    rect_under_toggle6_part1.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.73,
                                     setting_obj.window_height * 0.473)
    label_under_toggle6_part2=font3.render("time", True, "black")
    rect_under_toggle6_part2=label_under_toggle6_part2.get_rect()
    rect_under_toggle6_part2.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.73,
                                     setting_obj.window_height * 0.4875)





    multiple_graphs_label1=font2.render("Show multiple", True, "black")
    multiple_graphs_rect1=multiple_graphs_label1.get_rect()
    multiple_graphs_rect1.center=(setting_obj.setting_side_width+setting_obj.vertical_width*0.23,
                                  setting_obj.window_height*0.62)
    multiple_graphs_label2=font2.render("graphs", True, "black")
    multiple_graphs_rect2=multiple_graphs_label2.get_rect()
    multiple_graphs_rect2.center=(setting_obj.setting_side_width+setting_obj.vertical_width*0.23,
                                  setting_obj.window_height*0.65)

    zoom_label=font2.render("Zoom", True, "black")
    zoom_rect=zoom_label.get_rect()
    zoom_rect.center=(setting_obj.setting_side_width+setting_obj.vertical_width*0.11,
                      setting_obj.window_height*0.54)

    pillar_label=font2.render("Height",True,"black")
    pillar_rect=pillar_label.get_rect()
    pillar_rect.center=(setting_obj.setting_side_width+setting_obj.vertical_width*0.13,
                        setting_obj.window_height*0.735)

    axes_label=font2.render("Axes",True,"black")
    axes_rect=axes_label.get_rect()
    axes_rect.center=(setting_obj.setting_side_width+setting_obj.vertical_width*0.1,
                      setting_obj.window_height*0.805)

    friction1_label=font2.render("friction",True,"black")
    friction1_rect=friction1_label.get_rect()
    friction1_rect.center=(setting_obj.setting_side_width+setting_obj.vertical_width*0.13,
                      setting_obj.window_height*0.275)
    friction2_label=font2.render("coefficient",True,"black")
    friction2_rect=friction2_label.get_rect()
    friction2_rect.center=(setting_obj.setting_side_width+setting_obj.vertical_width*0.13,
                      setting_obj.window_height*0.3)

    WIN.blit(information_label, information_label_rect)
    WIN.blit(angle_label, angle_label_rect)
    WIN.blit(vel_label, vel_label_rect)
    WIN.blit(setting_label, setting_label_rect)
    WIN.blit(graph_label_part1,graph_rect_part1)
    WIN.blit(graph_label_part2,graph_rect_part2)
    WIN.blit(label_under_toggle1_part1,rect_under_toggle1_part1)
    WIN.blit(label_under_toggle1_part2,rect_under_toggle1_part2)
    WIN.blit(label_under_toggle2_part1,rect_under_toggle2_part1)
    WIN.blit(label_under_toggle2_part2,rect_under_toggle2_part2)
    WIN.blit(label_under_toggle3_part1,rect_under_toggle3_part1)
    WIN.blit(label_under_toggle3_part2,rect_under_toggle3_part2)
    WIN.blit(label_under_toggle4_part1,rect_under_toggle4_part1)
    WIN.blit(label_under_toggle4_part2,rect_under_toggle4_part2)
    WIN.blit(label_under_toggle5_part1,rect_under_toggle5_part1)
    WIN.blit(label_under_toggle5_part2,rect_under_toggle5_part2)
    WIN.blit(label_under_toggle6_part1,rect_under_toggle6_part1)
    WIN.blit(label_under_toggle6_part2,rect_under_toggle6_part2)
    WIN.blit(zoom_label,zoom_rect)
    WIN.blit(multiple_graphs_label1,multiple_graphs_rect1)
    WIN.blit(multiple_graphs_label2,multiple_graphs_rect2)
    WIN.blit(pillar_label,pillar_rect)
    WIN.blit(axes_label,axes_rect)
    WIN.blit(friction1_label,friction1_rect)
    WIN.blit(friction2_label,friction2_rect)



def menu_button_func(setting_obj):
    setting_obj.menu1_on=True


def display_information_text(red_circle,WIN,setting_obj):
    font = pygame.font.Font("freesansbold.ttf", 14)
    text = font.render(f"Vertical velocity= {round(red_circle.old_vel,2)} m/s", True, "black")
    textrect = text.get_rect()
    text2 = font.render(f"Horizontal veocity= {round(red_circle.horizontal_vel,2)} m/s", True, "black")
    textrect2 = text.get_rect()
    textrect.center = (setting_obj.setting_side_width*0.75,setting_obj.window_height *0.825)
    textrect2.center=(setting_obj.setting_side_width*0.75,setting_obj.window_height *0.85)
    text3 = font.render(f"Speed= {round(red_circle.current_velocity,2)} m/s", True, "black")
    textrect3 = text3.get_rect()
    textrect3.center=(setting_obj.setting_side_width*0.7265,setting_obj.window_height *0.875)
    text4 = font.render(f"Angle= {round(red_circle.delta_theta,2)} rad", True, "black")
    textrect4 = text4.get_rect()
    textrect4.center=(setting_obj.setting_side_width*0.7265,setting_obj.window_height *0.9)
    text5 = font.render(f"Mass= {round(red_circle.mass,2)} kg", True, "black")
    textrect5 = text5.get_rect()
    textrect5.center=(setting_obj.setting_side_width*0.885,setting_obj.window_height *0.825)
    text6 = font.render(f"Area= {round(red_circle.area,1)} m^2", True, "black")
    textrect6 = text6.get_rect()
    textrect6.center=(setting_obj.setting_side_width*0.885,setting_obj.window_height *0.85)
    text7 = font.render(f"Air density= 1.0 kg/m^3", True, "black")
    textrect7 = text7.get_rect()
    textrect7.center=(setting_obj.setting_side_width*0.91,setting_obj.window_height *0.875)
    text8 = font.render(f"Friction= {round(red_circle.drag,2)} N", True, "black")
    textrect8 = text8.get_rect()
    textrect8.center=(setting_obj.setting_side_width*0.885,setting_obj.window_height *0.9)
    WIN.blit(text, textrect)
    WIN.blit(text2,textrect2)
    WIN.blit(text3,textrect3)
    WIN.blit(text4,textrect4)
    WIN.blit(text5,textrect5)
    WIN.blit(text6,textrect6)
    WIN.blit(text7,textrect7)
    WIN.blit(text8,textrect8)






if __name__=="__main__":
    pass
