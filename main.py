import pygame
import math

def main_body():
    pygame.init()
    WIDTH,HEIGHT=1000,900
    RED=pygame.Color(255,0,0)
    flags=pygame.SCALED
    running=True
    FPS=60
    SCALE_T=1000  #1000 ticks for 1 second
    SCALE_M=100  #100 pixels for every 1 meter
    class Projectile:
        G=9.80665 #ms^-2
        def __init__(self,initial_vel):
            self.initial_vel=initial_vel   #ms^-1
        def calc_velocity(self):
            final_vel=math.sqrt((self.initial_vel*self.initial_vel)+2*Projectile.G*(HEIGHT/100))
            print(final_vel)
            return final_vel

    class Circle(Projectile):
        def __init__(self,initial_vel,center):
            super().__init__(initial_vel)
            self.center=center
        def draw_circle(self):
            final_vel=self.calc_velocity()
            final_vel=final_vel
            self.center[1]+=final_vel
            pygame.draw.circle(WIN,"red",self.center,30)


    circle1 = Circle(0, [500, 30])


    while running:
        pygame.time.Clock().tick(FPS)
        WIN=pygame.display.set_mode((WIDTH, HEIGHT),flags)
        circle1.draw_circle()
        pygame.display.flip()




        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                quit()


if __name__=="__main__":
    main_body()
