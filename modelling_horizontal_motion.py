import pygame
#----------------test values--------------=
class Projectile:
    G = 9.80665  # accepted value of gravitational acceleration

    def __init__(self,initial_vel,initial_angle,y_pos,x_pos):
        self.initial_vel = initial_vel
        self.initial_angle=initial_angle
        self.y_pos=y_pos
        self.x_pos=x_pos


    def vertical_motion(self):
        final_vel = (self.G * 1) + self.initial_vel  # suvat equation for final velocity
        self.initial_vel = final_vel  # final velocity for next iteration
        displacement = (final_vel / FPS) * SCALE  # distance to move objects,divided equally across a second,-
        return displacement  # -depending on the scale
    def horizontal_motion(self):
        if self.initial_angle==0:
            horizontal_vel=self.initial_vel*1
            vertical_vel=(self.G*1)+self.initial_vel
            self.initial_vel=vertical_vel
            horizontal_displacement=(horizontal_vel/FPS)*SCALE
            vertical_displacement=(vertical_vel/FPS)*SCALE
            return horizontal_displacement,vertical_displacement
FPS=60
G=9.80665
SCALE=5
WIDTH, HEIGHT = 400, 400  # dimensions of Surface
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#--------------test values-----------------#