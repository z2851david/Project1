import pygame
import matplotlib
matplotlib.use('module://pygame_matplotlib.backend_pygame')
import matplotlib.pyplot as plt
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.toggle import Toggle

class Graph():

    def plot_displacement(self,setting_obj):
        for n in range(len(setting_obj.displacement_list)):
            self.ax.plot(setting_obj.time_list[n],setting_obj.displacement_list[n],color=setting_obj.colors[n])
            self.ax.set_ylabel("Displacement/m",c="red")
            self.ax.set_xlabel("Time/s",c="red")
            self.ax.xaxis.set_label_coords(1,-0.01)
            self.ax.yaxis.set_label_coords(0.05,1)



    def plot_velocity(self,setting_obj):
        for n in range(len(setting_obj.velocity_list)):
            self.ax.plot(setting_obj.time_list[n],setting_obj.velocity_list[n],color=setting_obj.colors[n])
            self.ax.set_ylabel("velocity/ms^-1",c="red")
            self.ax.set_xlabel("Time/s",c="red")
            self.ax.xaxis.set_label_coords(1,-0.01)
            self.ax.yaxis.set_label_coords(0.05,1)  
    def clear(self):
        self.ax.cla()
    def create_graph(self,WIN,setting_obj):
        if setting_obj.graph_logic_counter2 == 0:
            setting_obj.graph_logic_counter2 += 1
            setting_obj.graph_logic_counter3 = 0
            self.fig,self.ax=plt.subplots(figsize=(450,300),dpi=1,facecolor="#46aefc")
        WIN.blit(self.fig,(setting_obj.setting_side_width*0.5,-20))
        self.fig.canvas.draw()


    def close_graph(self):
        plt.clf()


def init_buttons(WIN,setting_obj,red_circle,displacement_time_graph):
    start_stop_button = Button(WIN, setting_obj.setting_side_width + setting_obj.vertical_width*0.01,
                          setting_obj.window_height *0.85, 80, 80, text="Start/Stop",
                          onClick=lambda: start_stop_button_func(setting_obj),
                          fontSize=24)
    displacement_graph_toggle = Toggle(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.5),
                          int(setting_obj.window_height*0.435),30,24,startOn=False)

    velocity_graph_toggle=Toggle(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.67),
                                 int(setting_obj.window_height*0.435),30,24,startOn=False)


    multiple_graphs_toggle=Toggle(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.55),
                                  int(setting_obj.window_height*0.634),30,24,startOn=False)


    menu_button = Button(WIN, setting_obj.setting_side_width + setting_obj.vertical_width*0.43,
        setting_obj.window_height *0.85, 80, 80, text="Menu", onClick=lambda: menu_button_func(setting_obj),
        fontSize=24)

    exit_button = Button(WIN, setting_obj.setting_side_width + setting_obj.vertical_width*0.64,
        setting_obj.window_height * 0.85, 80, 80, text="Exit", onClick=lambda: quit(),
        fontSize=24)

    restart_button = Button(WIN, setting_obj.setting_side_width + setting_obj.vertical_width*0.22,
                            setting_obj.window_height*0.85, 80, 80,
                            text="Reset", onClick=lambda: restart_button_func(setting_obj, red_circle,
                                                                              displacement_time_graph),
                            fontSize=24)
    return displacement_graph_toggle,velocity_graph_toggle,multiple_graphs_toggle

def init_sliders(WIN,setting_obj):
    vel_slider = Slider(WIN, int(setting_obj.setting_side_width + setting_obj.vertical_width * 0.32),
                        int(setting_obj.window_height * 0.2334),
                        setting_obj.vertical_width * 0.37, 20
                        , min=0, max=35, step=1,
                        initial=0)
    output = TextBox(WIN, setting_obj.setting_side_width + setting_obj.vertical_width*0.74,
                     setting_obj.window_height * 0.224
                     , 40, 40)
    output.disable()
    angle_slider = Slider(WIN, int(setting_obj.setting_side_width + setting_obj.vertical_width * 0.32),
                          int(setting_obj.window_height * 0.34), setting_obj.vertical_width * 0.37,
                          20,
                          min=0, max=90, step=1,
                          initial=0)
    output2 = TextBox(WIN, setting_obj.setting_side_width + setting_obj.vertical_width * 0.74,
                      int(setting_obj.window_height * 0.33), 40
                      , 40)
    output2.disable()

    zoom_slider = Slider(WIN, int(setting_obj.setting_side_width + setting_obj.vertical_width * 0.32),
                           int(setting_obj.window_height * 0.525),setting_obj.vertical_width*0.37,20,
                         min=0,max=15,step=1,initial=0)
    output3=TextBox(WIN,setting_obj.setting_side_width+setting_obj.vertical_width*0.74,
                    int(setting_obj.window_height*0.51),40,40)
    output3.disable()

    pillar_slider=Slider(WIN,int(setting_obj.setting_side_width+setting_obj.vertical_width*0.32),
                         int(setting_obj.window_height*0.74),setting_obj.vertical_width*0.37,20,
                         min=0,max=30,step=1,initial=0)
    output4=TextBox(WIN,setting_obj.setting_side_width+setting_obj.vertical_width*0.74,
                    int(setting_obj.window_height*0.725),40,40)
    output4.disable()


    return vel_slider,output,angle_slider,output2,zoom_slider,output3,pillar_slider,output4






def start_stop_button_func(setting_obj):
    if setting_obj.is_run==False:
        setting_obj.is_run=True
    elif setting_obj.is_run_after==True and setting_obj.is_run==True:
        setting_obj.is_run_after=False
    elif setting_obj.is_run_after==False:
        setting_obj.is_run_after=True





def restart_button_func(setting_obj,red_circle,displacement_time_graph):
    setting_obj.reset_obj = True
    setting_obj.is_run = False
    setting_obj.is_run_after=True
    if not setting_obj.draw_multiple_graphs:
        setting_obj.displacement_list=[[]]
        setting_obj.time_list=[[]]
        setting_obj.velocity_list=[[]]
        setting_obj.graph_list_n=0

    else:
        setting_obj.displacement_list.append([])
        setting_obj.time_list.append([])
        setting_obj.velocity_list.append([])
        setting_obj.graph_list_n+=1
    setting_obj.coord_list=[[],[]]
    setting_obj.displacement_time_counter=0
    try:
        displacement_time_graph.clear()
    except:
        pass
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
    setting_label_rect.center = (setting_obj.setting_side_width + setting_obj.vertical_width * 0.5,
                                 setting_obj.window_height * 0.08)
    information_label = font3.render("Press 'reset' to save changes", True, "black")
    information_label_rect = information_label.get_rect()
    information_label_rect.center = (setting_obj.setting_side_width + setting_obj.vertical_width * 0.35,
                                     setting_obj.window_height * 0.18)
    vel_label = font2.render("Velocity", True, "black")
    vel_label_rect = vel_label.get_rect()
    vel_label_rect.center = (setting_obj.setting_side_width + setting_obj.vertical_width * 0.14,
                             setting_obj.window_height * 0.25)
    angle_label = font2.render("Angle", True, "black")
    angle_label_rect = angle_label.get_rect()
    angle_label_rect.center = (setting_obj.setting_side_width + setting_obj.vertical_width * 0.11,
                               int(setting_obj.window_height * 0.355))

    graph_label = font2.render("Toggle Graphs", True, "black")
    graph_rect = angle_label.get_rect()
    graph_rect.center = (setting_obj.setting_side_width + setting_obj.vertical_width * 0.11,
                               int(setting_obj.window_height * 0.45))
    label_under_toggle1=font3.render("(S/t)", True, "black")
    rect_under_toggle1=label_under_toggle1.get_rect()
    rect_under_toggle1.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.53,
                                     setting_obj.window_height * 0.49)
    label_under_toggle2=font3.render("(v/t)", True, "black")
    rect_under_toggle2=label_under_toggle1.get_rect()
    rect_under_toggle2.center=(setting_obj.setting_side_width + setting_obj.vertical_width * 0.705,
                                     setting_obj.window_height * 0.49)

    multiple_graphs_label1=font2.render("Show multiple", True, "black")
    multiple_graphs_rect1=multiple_graphs_label1.get_rect()
    multiple_graphs_rect1.center=(setting_obj.setting_side_width+setting_obj.vertical_width*0.23,
                                  setting_obj.window_height*0.63)
    multiple_graphs_label2=font2.render("graphs", True, "black")
    multiple_graphs_rect2=multiple_graphs_label2.get_rect()
    multiple_graphs_rect2.center=(setting_obj.setting_side_width+setting_obj.vertical_width*0.23,
                                  setting_obj.window_height*0.67)

    zoom_label=font2.render("Zoom", True, "black")
    zoom_rect=zoom_label.get_rect()
    zoom_rect.center=(setting_obj.setting_side_width+setting_obj.vertical_width*0.11,
                      setting_obj.window_height*0.54)

    WIN.blit(information_label, information_label_rect)
    WIN.blit(angle_label, angle_label_rect)
    WIN.blit(vel_label, vel_label_rect)
    WIN.blit(setting_label, setting_label_rect)
    WIN.blit(graph_label,graph_rect)
    WIN.blit(label_under_toggle1,rect_under_toggle1)
    WIN.blit(label_under_toggle2,rect_under_toggle2)
    WIN.blit(zoom_label,zoom_rect)
    WIN.blit(multiple_graphs_label1,multiple_graphs_rect1)
    WIN.blit(multiple_graphs_label2,multiple_graphs_rect2)



def menu_button_func(setting_obj):
    setting_obj.menu1_on=True


def display_information_text(red_circle,WIN,setting_obj):
    font = pygame.font.Font("freesansbold.ttf", 14)
    text = font.render(f"vertical velocity={int(red_circle.old_vel)}", True, "black")
    textrect = text.get_rect()
    text2 = font.render(f"horizontal veocity={int(red_circle.horizontal_vel)}", True, "black")
    textrect2 = text.get_rect()
    textrect.center = (setting_obj.setting_side_width*0.9,setting_obj.window_height *0.79)
    textrect2.center=(setting_obj.setting_side_width*0.9,setting_obj.window_height *0.82)
    WIN.blit(text, textrect)
    WIN.blit(text2,textrect2)





if __name__=="__main__":
    pass
