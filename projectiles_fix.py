#--------------test values( wont be imported)-------------------#


import math
import pygame

WIDTH,HEIGHT=800,400


#------------------test values---------------------------------#

class Projectile:

    def __init__(self,radius, centre, vel, angle, y_pos, x_pos,):
        self.g=-9.80665  #accepted value of gravitational acceleration
        self.y_pos = y_pos   #y position every iteration
        self.x_pos = x_pos   #x position every iteration
        self.stop_motion=False    #if the object is still moving vertically
        self.vel_before_motion=vel   #the initial velocity before starting motion
        self.initial_angle = math.radians(angle)   #initial angle before starting motion
        self.radius=radius    #sets the radius of he projectile
        self.centre=centre    #sets the center of the projectile
        self.mass=5.0         #sets mass of projectile
        self.area=(((self.radius/50)**2)*math.pi*4)/2
        self.vertical_acceleration =self.g
        self.horizontal_acceleration=0
        self.vertical_vel=0
        self.delta_theta=self.initial_angle
        self.horizontal_vel = vel * math.cos(self.initial_angle)
        self.old_vel = vel * math.sin(self.initial_angle)
        self.current_velocity=math.sqrt((self.vertical_vel**2)+(self.horizontal_vel**2))

        self.drag_coefficient=0.0
        self.drag=0
    def set_vel(self,initial_vel,angle):
        self.initial_vel=initial_vel
        self.initial_angle=math.radians(angle)
        self.horizontal_vel = self.initial_vel * math.cos(self.initial_angle)
        self.old_vel = self.initial_vel * math.sin(self.initial_angle)
    def set_acceleration(self,setting_obj):
        self.drag=(((self.current_velocity)**2)*self.drag_coefficient*self.area)/2 #formula calculating drag from area and velocity
        horizontal_drag = -(math.cos(self.delta_theta) * self.drag)  #horizontal component of force
        self.horizontal_acceleration = (horizontal_drag / self.mass)  #calculate horizontal acceleration from drag and mass
        vertical_drag=-(math.sin(self.delta_theta)*self.drag)    #vertical component of drag
        self.vertical_acceleration= (self.g + (vertical_drag/self.mass))  #vertical acceleration added to gravitational acceleration
    def update_velocity_theta(self,setting_obj):
        self.current_velocity=math.sqrt((self.vertical_vel**2)+(self.horizontal_vel**2)) #uses pythagorean theorem to find velocity
        if setting_obj.setting_motion=="vertical":
            self.delta_theta=math.asin(self.vertical_vel/self.current_velocity)
        else:
          self.delta_theta=math.atan(self.vertical_vel/self.horizontal_vel)  #uses arc tan function to find angle from components






    def __del__(self):
        return



    def motion(self,setting_object):

        if self.stop_motion==False:
            self.vertical_vel = (self.vertical_acceleration*setting_object.delta_time) + self.old_vel
            self.horizontal_vel = self.horizontal_vel + (self.horizontal_acceleration * setting_object.delta_time)
        self.old_vel=self.vertical_vel
        return self.vertical_vel,self.horizontal_vel




def initiate_circle(setting_motion,setting_obj):

    if setting_motion=="vertical":  #if motion is vertical, set ball at the top of the screen
        red_circle=Projectile(20, [setting_obj.setting_tab_width // 2, 0], 0, 0, 20, setting_obj.setting_tab_start_point // 2)
    elif setting_motion=="horizontal":   #if motion is horizontal, set ball at the bottom-right of the screen
        red_circle=Projectile(20,[20,setting_obj.window_height//1.3],30,45,setting_obj.window_height//1.3-20,20)
    return red_circle   #return object to main function



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

  #  if not setting_obj.bounce:

    if red_circle.y_pos > setting_obj.window_height//1.3-red_circle.radius:  # if ball goes over border
        red_circle.y_pos = setting_obj.window_height//1.3-red_circle.radius #go back same amount
        red_circle.vertical_vel=0
        red_circle.horizontal_vel=0
        red_circle.stop_motion=True

    if red_circle.x_pos >= setting_obj.setting_tab_start_point:
        red_circle.x_pos= setting_obj.setting_tab_start_point - red_circle.radius # if ball goes over right-border
        red_circle.horizontal_vel=0

    if setting_obj.bounce:
        if not red_circle.stop_motion:

            if red_circle.y_pos >= setting_obj.window_height//1.3-red_circle.radius:
                red_circle.y_pos = setting_obj.window_height//1.3-red_circle.radius
                red_circle.vertical_vel+=1
                if red_circle.vertical_vel> -4:
                    red_circle.vertical_vel=0
                    red_circle.horizontal_vel=0
                    red_circle.stop_motion=True
                red_circle.old_vel=-red_circle.vertical_vel

            if red_circle.x_pos >= setting_obj.setting_tab_start_point:
                red_circle.horizontal_vel = -red_circle.horizontal_vel  # if ball goes over right-border

            if red_circle.x_pos<= 0:
                red_circle.horizontal_vel=-red_circle.horizontal_vel


    pygame.draw.circle(WIN,"red",(red_circle.x_pos,red_circle.y_pos),red_circle.radius,0)

