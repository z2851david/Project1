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
        self.final_vel=0
        self.angle = math.radians(angle)
        self.horizontal_vel = self.initial_vel * math.cos(self.angle)
        self.vertical_vel = self.initial_vel * math.sin(self.angle)
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.stop_y_motion=False
    def set_vel(self,initial_vel,angle):
        self.initial_vel=initial_vel
        self.angle=math.radians(angle)
        self.horizontal_vel = self.initial_vel * math.cos(self.angle)
        self.vertical_vel = self.initial_vel * math.sin(self.angle)



    def horizontal_motion(self,FPS,SCALE):
        horizontal_displacement = (self.horizontal_vel / FPS) * SCALE
        if self.stop_y_motion==False:
            self.final_vel = (-self.G * 1 / FPS) + (self.vertical_vel)  # suvat equation for final velocity
        vertical_displacement = (self.vertical_vel * 1 / FPS) + ((-self.G) / 2 * (1 / FPS) * (1 / FPS))
        vertical_displacement = vertical_displacement * SCALE  # distance to move objects across a tick/millisecond
        self.vertical_vel = self.final_vel
        return vertical_displacement,horizontal_displacement


class Ball(Projectile):
    def __init__(self,radius,center,initial_vel,initial_angle,y_pos,x_pos):
        super().__init__(initial_vel,initial_angle,y_pos,x_pos)
        self.radius=radius
        self.center=center
def initiate_circle(setting_motion):

    if setting_motion=="vertical":
        red_circle=Ball(10,[WIDTH/2,0],0,0,10,WIDTH//2)
    elif setting_motion=="horizontal":
        red_circle=Ball(10,[10,HEIGHT-10],22,22,HEIGHT-10,10)
    return red_circle




def move_circle(red_circle,FPS,SCALE,WIN):
    vertical_displacement,horizontal_displacement=red_circle.horizontal_motion(FPS,SCALE)
    red_circle.y_pos=red_circle.y_pos-vertical_displacement
    red_circle.x_pos=red_circle.x_pos+horizontal_displacement

    if red_circle.x_pos>= WIDTH:
        red_circle.horizontal_vel=-red_circle.horizontal_vel  #if ball goes over right-border

    if red_circle.y_pos + red_circle.radius > HEIGHT:  # if ball goes over border
        red_circle.y_pos = red_circle.y_pos + vertical_displacement #go back same amount
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


        red_circle.vertical_vel+=vertical_displacement
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

