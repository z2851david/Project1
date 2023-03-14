#--------------test values( wont be imported)-------------------#



import math
import pygame

WIDTH,HEIGHT=800,400


#------------------test values---------------------------------#

class Projectile:

    def __init__(self,vel,angle, y_pos, x_pos):
        self.g=-9.80665
        self.vertical_acceleration =self.g # accepted value of gravitational acceleration
        self.horizontal_acceleration=0
        self.vel_before_motion=vel
        self.vertical_vel=0
        self.initial_angle = math.radians(angle)
        self.delta_theta=self.initial_angle
        self.horizontal_vel = vel * math.cos(self.initial_angle)
        self.old_vel = vel * math.sin(self.initial_angle)
        self.current_velocity=math.sqrt((self.vertical_vel**2)+(self.horizontal_vel**2))
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.stop_y_motion=False
        self.drag_coefficient=0.0
        self.drag=0
    def set_vel(self,initial_vel,angle):
        self.initial_vel=initial_vel
        self.initial_angle=math.radians(angle)
        self.horizontal_vel = self.initial_vel * math.cos(self.initial_angle)
        self.old_vel = self.initial_vel * math.sin(self.initial_angle)
    def set_acceleration(self,setting_obj):
        self.drag=(((self.current_velocity)**2)*self.drag_coefficient*self.area)/2
        if setting_obj.setting_motion=="vertical":
            self.horizontal_acceleration=0
        else:
            horizontal_drag = -(math.cos(self.delta_theta) * self.drag)
            self.horizontal_acceleration = (horizontal_drag / self.mass)
        vertical_drag=-(math.sin(self.delta_theta)*self.drag)
        self.vertical_acceleration= (self.g + (vertical_drag/self.mass))
        print(math.cos(self.delta_theta))
    def update_velocity_theta(self,setting_obj):
        self.current_velocity=math.sqrt((self.vertical_vel**2)+(self.horizontal_vel**2))
        if setting_obj.setting_motion=="vertical":
            self.delta_theta=math.asin(self.vertical_vel/self.current_velocity)
        else:
            self.delta_theta=math.atan(self.vertical_vel/self.horizontal_vel)






    def __del__(self):
        return



    def motion(self,setting_object):

        if self.stop_y_motion==False:
            self.vertical_vel = (self.vertical_acceleration*setting_object.delta_time) + self.old_vel
            self.horizontal_vel = self.horizontal_vel + (self.horizontal_acceleration * setting_object.delta_time)
        self.old_vel=self.vertical_vel
        return self.vertical_vel,self.horizontal_vel


class Ball(Projectile):
    def __init__(self,radius,center,initial_vel,initial_angle,y_pos,x_pos):
        super().__init__(initial_vel,initial_angle,y_pos,x_pos)
        self.radius=radius
        self.center=center
        self.mass=5.0
        self.area=(((self.radius/50)**2)*math.pi*4)/2


def initiate_circle(setting_motion,setting_obj):

    if setting_motion=="vertical":
        red_circle=Ball(20,[setting_obj.vertical_width/2,0],0,0,10,setting_obj.setting_side_width//2)
    elif setting_motion=="horizontal":
        red_circle=Ball(20,[20,setting_obj.window_height//1.3],35,60,setting_obj.window_height//1.3-20,50)
    return red_circle



def move_circle(red_circle,WIN,setting_obj):
    if setting_obj.setting_motion=="horizontal":
        if red_circle.horizontal_vel>0 and red_circle.vertical_vel!=0:
            red_circle.update_velocity_theta(setting_obj)
            red_circle.set_acceleration(setting_obj)
    elif setting_obj.setting_motion=="vertical":
        if red_circle.vertical_vel!=0:
            red_circle.update_velocity_theta(setting_obj)
            red_circle.set_acceleration(setting_obj)
    vertical_velocity,horizontal_velocity=red_circle.motion(setting_obj)
    red_circle.y_pos=red_circle.y_pos-(vertical_velocity*setting_obj.delta_time)*setting_obj.scale
    red_circle.x_pos=red_circle.x_pos+(horizontal_velocity *setting_obj.delta_time)*setting_obj.scale

    if not setting_obj.bounce:

        if red_circle.y_pos > setting_obj.window_height//1.3-red_circle.radius:  # if ball goes over border
            red_circle.y_pos = setting_obj.window_height//1.3-red_circle.radius #go back same amount
            red_circle.vertical_vel=0
            red_circle.horizontal_vel=0
            red_circle.stop_y_motion=True

        if red_circle.x_pos >= setting_obj.setting_side_width:
            red_circle.x_pos=setting_obj.setting_side_width-red_circle.radius # if ball goes over right-border
            red_circle.horizontal_vel=0

    if setting_obj.bounce:
        if not red_circle.stop_y_motion:

            if red_circle.y_pos >= setting_obj.window_height//1.3-red_circle.radius:
                red_circle.y_pos = setting_obj.window_height//1.3-red_circle.radius
                red_circle.vertical_vel+=1
                if red_circle.vertical_vel> -4:
                    red_circle.vertical_vel=0
                    red_circle.horizontal_vel=0
                    red_circle.stop_y_motion=True
                red_circle.old_vel=-red_circle.vertical_vel

            if red_circle.x_pos >= setting_obj.setting_side_width:
                red_circle.horizontal_vel = -red_circle.horizontal_vel  # if ball goes over right-border

            if red_circle.x_pos<= 0:
                red_circle.horizontal_vel=-red_circle.horizontal_vel


    pygame.draw.circle(WIN,"red",(red_circle.x_pos,red_circle.y_pos),red_circle.radius,0)
