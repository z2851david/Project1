import pygame
import tkinter
from tkinter import ttk,messagebox
import math
#----------test values----------------#
WIDTH, HEIGHT = 400, 400
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


#--------test values------------------#

def start_button(WIN,event):
        font=pygame.font.Font("freesansbold.ttf",18)
        text=font.render("Start",True,"orange",)
        textrect=text.get_rect()
        textrect.center=(WIDTH//0.57,HEIGHT//1.1)

        mouse = pygame.mouse.get_pos()

        if (WIDTH // 0.57) - (text.get_width() // 2) <= mouse[0] <= (WIDTH // 0.57) + (text.get_width() // 2) and \
                (HEIGHT // 1.1) - (text.get_height() // 2) <= mouse[1] <= (HEIGHT // 1.1) + (text.get_height() // 2):

            pygame.draw.rect(WIN, "black", textrect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                is_run=True
                return is_run
        else:
            pygame.draw.rect(WIN, "gray", textrect)
        is_run=False
        WIN.blit(text,textrect)
        return is_run

def stop_button(WIN,event):
    font = pygame.font.Font("freesansbold.ttf", 18)
    text = font.render("Stop", True, "orange", )
    textrect = text.get_rect()
    textrect.center = (WIDTH // 0.57, HEIGHT // 1.1)

    mouse = pygame.mouse.get_pos()

    if (WIDTH // 0.57) - (text.get_width() // 2) <= mouse[0] <= (WIDTH // 0.57) + (text.get_width() // 2) and \
            (HEIGHT // 1.1) - (text.get_height() // 2) <= mouse[1] <= (HEIGHT // 1.1) + (text.get_height() // 2):

        pygame.draw.rect(WIN, "black", textrect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            return False

    else:
        pygame.draw.rect(WIN, "gray", textrect)

    WIN.blit(text, textrect)

def restart_button(WIN,event):
    font = pygame.font.Font("freesansbold.ttf", 18)
    text = font.render("Start", True, "orange", )
    textrect = text.get_rect()
    textrect.center = (WIDTH // 0.57, HEIGHT // 1.2)

    mouse = pygame.mouse.get_pos()


    if (WIDTH // 0.57) - (text.get_width() // 2) <= mouse[0] <= (WIDTH // 0.57) + (text.get_width() // 2) and \
            (HEIGHT // 1.2) - (text.get_height() // 2) <= mouse[1] <= (HEIGHT // 1.2) + (text.get_height() // 2):

        pygame.draw.rect(WIN, "black", textrect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            return True

    else:
        pygame.draw.rect(WIN, "gray", textrect)

    WIN.blit(text, textrect)

def settings_button(WIN,event,red_circle,setting_obj):
    font = pygame.font.Font("freesansbold.ttf", 18)
    text = font.render("Settings", True, "orange", )
    textrect = text.get_rect()
    textrect.center = (WIDTH // 2, HEIGHT // 1.1)

    mouse = pygame.mouse.get_pos()

    if (WIDTH // 2) - (text.get_width() // 2) <= mouse[0] <= (WIDTH // 2) + (text.get_width() // 2) and \
            (HEIGHT // 1.1) - (text.get_height() // 2) <= mouse[1] <= (HEIGHT // 1.1) + (text.get_height() // 2):

        pygame.draw.rect(WIN, "black", textrect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.display.set_mode((WIDTH,HEIGHT),flags=pygame.HIDDEN)
            tkinter_window(red_circle,setting_obj)

    else:
        pygame.draw.rect(WIN, "gray", textrect)

    WIN.blit(text, textrect)

def tkinter_window(red_circle,setting_obj):
    WIDTH,HEIGHT=400,400
    menu=tkinter.Tk()
    menu.config(bg="gray")
    screen_size=pygame.display.get_desktop_sizes()
    center_x=int(screen_size[0][0]/2-WIDTH/2)
    center_y=int(screen_size[0][1]/2-HEIGHT/2)


    menu.geometry(f"{WIDTH}x{HEIGHT}+{center_x}+{center_y}")
    menu.title("Menu")
    menu.resizable(0,0)
    menu.rowconfigure(1,weight=0)
    menu.rowconfigure(2,weight=0)
    menu.rowconfigure(3,weight=1)





    label_title=tkinter.Label(menu,text="Settings",background="gray",font=("TkDefaultFont",22),pady=20,padx=50)
    label_title.grid(column=1,row=0,columnspan=3)

    label_vel=tkinter.Label(menu,text="Velocity",background="gray",font=("TkDefaultFont",14),pady=40,padx=10)
    label_vel.grid(column=0,row=1,sticky="NW",rowspan=2)

    text=tkinter.StringVar()
    entry_vel=tkinter.Entry(menu,background="gray",width=15,textvariable=text)
    entry_vel.grid(column=1,row=1,pady=45,sticky="NW",padx=10)


    label_angle=tkinter.Label(menu,text="Angle",background="gray",font=("TkDefaultFont",14),pady=10,padx=10)
    label_angle.grid(column=0,row=2,sticky="W")

    text2=tkinter.StringVar()
    entry_angle=tkinter.Entry(menu,background="gray",width=15,textvariable=text2)
    entry_angle.grid(column=1,row=2,pady=10,sticky="NW",padx=10)


    button_apply=tkinter.Button(menu,text="Apply",command=lambda :set_options(text,text2,red_circle\
                                                                              ,entry_vel,entry_angle),width=5,height=2)
    button_apply.grid(column=0,row=3,sticky="")

    button_return=tkinter.Button(menu,text="Return",command=lambda:menu.destroy(),width=5,height=2)
    button_return.grid(column=1,row=3,sticky="")

    button_restart=tkinter.Button(menu,text="Restart",command=lambda:reset_obj(setting_obj,red_circle,menu)\
                                  ,width=5,height=2)
    button_restart.grid(column=2,row=3,sticky="")

    button_main_menu=tkinter.Button(menu,text="Main menu",\
                                    command=lambda:go_to_menu(setting_obj,red_circle,menu),\
                                    width=9,height=2)
    button_main_menu.grid(column=3,row=3,sticky="",padx=30)









    menu.mainloop()

def set_options(text,text2,red_circle,entry_vel,entry_angle):
    if is_valid(text,text2):
        value1=int(text.get())
        value2=int(text2.get())
        red_circle.set_vel(value1,value2)
        tkinter.messagebox.showinfo("Done","Settings applied")
        entry_vel.delete(0,"end")
        entry_angle.delete(0,"end")


def is_valid(text,text2):
    text=text.get()
    text2=text2.get()
    if text.isalpha() or text2.isalpha():
        tkinter.messagebox.showerror("Invalid value","You cannot enter text")
        return False
    elif int(text)<0 or int(text2)<0:
        tkinter.messagebox.showerror("Invalid value","Values cannot be smaller than 0")
        return False
    elif int(text)>50:
        tkinter.messagebox.showerror("Invalid value","Velocity cannot be bigger than 50")
        return False
    elif int(text2)>180:
        tkinter.messagebox.showerror("Invalid value","Angle cannot be bigger than 180")
        return False
    else:
        return True




def go_to_menu(setting_obj,red_circle,menu):
    del red_circle
    setting_obj.is_run = False
    setting_obj.is_run_after = True
    setting_obj.reset_obj=True
    setting_obj.menu1_on=True
    menu.destroy()


def reset_obj(setting_obj,red_circle,menu):
    del red_circle
    setting_obj.is_run = False
    setting_obj.is_run_after = True
    setting_obj.reset_obj=True
    menu.destroy()



def display_information_text(red_circle):
    font = pygame.font.Font("freesansbold.ttf", 14)
    text = font.render(f"vertical velocity={int(red_circle.vertical_vel)}", True, "black")
    textrect = text.get_rect()
    text2 = font.render(f"horizontal veocity={int(red_circle.horizontal_vel)}", True, "black")
    textrect2 = text.get_rect()
    textrect.center = (red_circle.x_pos, red_circle.y_pos-40)
    textrect2.center=(red_circle.x_pos,red_circle.y_pos-20)
    WIN.blit(text, textrect)
    WIN.blit(text2,textrect2)





if __name__=="__main__":
    tkinter_window(red_circle=0)
