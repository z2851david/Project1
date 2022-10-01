import pygame
import pygame_widgets
from pygame_widgets.button import Button



def init_buttons(WIN,setting_obj,red_circle):
    start_stop_button = Button(WIN, setting_obj.setting_side_width + 20,
                          setting_obj.window_height - 150, 120, 100, text="Start/Stop",
                          onClick=lambda: start_stop_button_func(setting_obj),
                          fontSize=50)




    exit_button = Button(WIN, setting_obj.setting_side_width + 320,
        setting_obj.window_height - 150, 120, 100, text="Exit", onClick=lambda: quit(),
        fontSize=50)

    menu_button = Button(WIN, setting_obj.setting_side_width + 470,
        setting_obj.window_height - 150, 120, 100, text="Menu", onClick=lambda: menu_button_func(setting_obj) ,
        fontSize=50)

    restart_button = Button(WIN, setting_obj.setting_side_width + 170,
                            setting_obj.window_height - 150, 120, 100,
                            text="Reset", onClick=lambda: restart_button_func(setting_obj, red_circle),
                            fontSize=50)





def start_stop_button_func(setting_obj):
    if setting_obj.is_run==False:
        setting_obj.is_run=True
    elif setting_obj.is_run_after==True and setting_obj.is_run==True:
        setting_obj.is_run_after=False
    elif setting_obj.is_run_after==False:
        setting_obj.is_run_after=True





def restart_button_func(setting_obj,red_circle):
    setting_obj.reset_obj = True
    setting_obj.is_run = False
    setting_obj.is_run_after=True
    red_circle.__del__()








def menu_button_func(setting_obj):
    setting_obj.menu1_on=True


def display_information_text(red_circle,WIN):
    font = pygame.font.Font("freesansbold.ttf", 14)
    text = font.render(f"vertical velocity={int(red_circle.old_vel)}", True, "black")
    textrect = text.get_rect()
    text2 = font.render(f"horizontal veocity={int(red_circle.horizontal_vel)}", True, "black")
    textrect2 = text.get_rect()
    textrect.center = (red_circle.x_pos, red_circle.y_pos-40)
    textrect2.center=(red_circle.x_pos,red_circle.y_pos-20)
    WIN.blit(text, textrect)
    WIN.blit(text2,textrect2)





if __name__=="__main__":
    pass
