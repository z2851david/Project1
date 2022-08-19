#--------------test values( wont be imported)-------------------#




import pygame
FPS=60
G=9.80665
SCALE=5
WIDTH, HEIGHT = 400, 400  # dimensions of Surface
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


#------------------test values---------------------------------#

class Projectile:
    G = 9.80665  # accepted value of gravitational acceleration

    def __init__(self, initial_vertical_vel,initial_horizontal_vel,initial_angle, y_pos, x_pos):
        self.initial_vertical_vel = initial_vertical_vel
        self.initial_horizontal_vel=initial_horizontal_vel
        self.initial_angle = initial_angle
        self.y_pos = y_pos
        self.x_pos = x_pos

    def vertical_motion(self):
        final_vel = (self.G * 1) + self.initial_vel  # suvat equation for final velocity
        self.initial_vel = final_vel  # final velocity for next iteration
        displacement = (final_vel / FPS) * SCALE  # distance to move objects,divided equally across a second,-
        return displacement  # -depending on the scale

    def horizontal_motion(self):
        if self.initial_angle == 0:
            horizontal_vel = self.initial_horizontal_vel * 1
            vertical_vel = (self.G * 1) + self.initial_vertical_vel
            self.initial_vel = vertical_vel
            horizontal_displacement = (horizontal_vel / FPS) * SCALE
            vertical_displacement = (vertical_vel / FPS) * SCALE
            return  vertical_displacement,horizontal_displacement


class Ball(Projectile):
    def __init__(self,radius,center,initial_vel,initial_angle,y_pos,x_pos,):
        super().__init__(initial_vel,initial_angle,y_pos,x_pos)
        self.radius=radius
        self.center=[WIDTH/2,self.y_pos+self.radius]

def initiate_circle(setting_motion):
    if setting_motion=="vertical":
        red_circle=Ball(10,[WIDTH/2,0],0,0,0,0)
    elif setting_motion=="horizontal":
        red_circle=Ball(10,[0,HEIGHT/2],0,0,0,0)
    return red_circle

def move_circle_vertically(red_circle):
    displacement = red_circle.vertical_motion()
    red_circle.y_pos= red_circle.y_pos + displacement
    if red_circle.y_pos >= HEIGHT:  # if ball goes over border
        pygame.draw.circle(WIN, "red", (red_circle.center[0], HEIGHT - red_circle.radius), red_circle.radius, 0)  # set the ball on the border
    else:
        pygame.draw.circle(WIN, "red", (red_circle.center[0], red_circle.y_pos), red_circle.radius, 0)  # otherwise continue motion

def move_circle_horizontally(red_circle):
    vertical_displacement,horizontal_displacement=red_circle.horizontal_motion()
    red_circle.y_pos=red_circle.y_pos+vertical_displacement
    red_circle.x_pos=red_circle.x_pos+horizontal_displacement
    if red_circle.y_pos>= HEIGHT:
        pygame.draw.circle(WIN,"red",(red_circle.x_pos,HEIGHT-red_circle.radius),red_circle.radius,0)
    elif red_circle.x_pos>= WIDTH:
        pygame.draw.circle(WIN,"red",(WIDTH-red_circle.radius,red_circle.y_pos),red_circle.radius,0)
    else:
        pygame.draw.circle(WIN,"red",(red_circle.x_pos,red_circle.y_pos),red_circle.radius,0)



if __name__=="__main__":
    pass