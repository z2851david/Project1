#--------------test values( wont be imported)-------------------#



import math
import pygame

WIDTH,HEIGHT=800,400


#------------------test values---------------------------------#

class Projectile:
    G = 9.80665  # accepted value of gravitational acceleration

    def __init__(self,vel,angle, y_pos, x_pos):
        self.initial_vel=vel
        self.vel_before_motion=self.initial_vel
        self.vertical_vel=0
        self.angle = math.radians(angle)
        self.horizontal_vel = self.initial_vel * math.cos(self.angle)
        self.old_vel = self.initial_vel * math.sin(self.angle)
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.stop_y_motion=False
    def set_vel(self,initial_vel,angle):
        self.initial_vel=initial_vel
        self.angle=math.radians(angle)
        self.horizontal_vel = self.initial_vel * math.cos(self.angle)
        self.old_vel = self.initial_vel * math.sin(self.angle)

    def __del__(self):
        return



    def motion(self,setting_object):
        self.horizontal_vel = self.horizontal_vel
        if self.stop_y_motion==False:
            self.vertical_vel = (-self.G*setting_object.delta_time) + (self.old_vel)
        self.old_vel=self.vertical_vel
        return self.vertical_vel,self.horizontal_vel


class Ball(Projectile):
    def __init__(self,radius,center,initial_vel,initial_angle,y_pos,x_pos):
        super().__init__(initial_vel,initial_angle,y_pos,x_pos)
        self.radius=radius
        self.center=center
def initiate_circle(setting_motion,setting_obj):

    if setting_motion=="vertical":
        red_circle=Ball(20,[setting_obj.vertical_width/2,0],0,0,10,setting_obj.setting_side_width//2)
    elif setting_motion=="horizontal":
        red_circle=Ball(20,[20,setting_obj.window_height//1.3],35,60,setting_obj.window_height//1.3-20,50)
    return red_circle



def move_circle(red_circle,WIN,setting_obj):
    vertical_velocity,horizontal_velocity=red_circle.motion(setting_obj)
    red_circle.y_pos=red_circle.y_pos-(vertical_velocity*setting_obj.delta_time)*setting_obj.scale
    red_circle.x_pos=red_circle.x_pos+(horizontal_velocity *setting_obj.delta_time)*setting_obj.scale

    if red_circle.y_pos > setting_obj.window_height//1.3-red_circle.radius:  # if ball goes over border
        red_circle.y_pos = setting_obj.window_height//1.3-red_circle.radius #go back same amount
        red_circle.vertical_vel=0
        red_circle.horizontal_vel=0
        red_circle.stop_y_motion=True

    #if red_circle.x_pos >= setting_obj.setting_side_width:
        #red_circle.x_pos=setting_obj.setting_side_width-red_circle.radius # if ball goes over right-border
        #red_circle.horizontal_vel=0

    if setting_obj.bounce==True:

        if red_circle.x_pos >= setting_obj.setting_side_width:
            red_circle.horizontal_vel = -red_circle.horizontal_vel  # if ball goes over right-border

            if red_circle.horizontal_vel>0 and red_circle.stop_y_motion!=True:
                red_circle.horizontal_vel-=3
                if red_circle.horizontal_vel<0:
                    red_circle.horizontal_vel=0

            if red_circle.horizontal_vel>0 and red_circle.stop_y_motion==True:

                red_circle.horizontal_vel-=0.01
                if red_circle.horizontal_vel<0:
                    red_circle.horizontal_vel=0

            if red_circle.horizontal_vel<0 and red_circle.stop_y_motion!=True:
                red_circle.horizontal_vel+=3
                if red_circle.horizontal_vel>0:
                    red_circle.horizontal_vel=0

            if red_circle.horizontal_vel<0 and red_circle.stop_y_motion==True:
                red_circle.horizontal_vel+=0.01
                if red_circle.horizontal_vel>0:
                    red_circle.horizontal_vel=0


            red_circle.vertical_vel+=vertical_velocity
            red_circle.vertical_vel+=3
            red_circle.vertical_vel = -red_circle.vertical_vel
            if red_circle.vertical_vel == -abs(red_circle.vertical_vel):  #if vertical velocity is negative
                red_circle.stop_y_motion=True
                red_circle.vertical_vel=0
                pygame.draw.circle(WIN, "red", (red_circle.x_pos, red_circle.y_pos), red_circle.radius, 0)

            if red_circle.x_pos<= 0:
                red_circle.horizontal_vel=-red_circle.horizontal_vel


    else:
        pygame.draw.circle(WIN,"red",(red_circle.x_pos,red_circle.y_pos),red_circle.radius,0)


