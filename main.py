import pygame
import math

def main_body():
    pygame.init()
    WIDTH,HEIGHT=1000,900
    RED=pygame.Color(255,0,0)
    flags=pygame.SCALED
    running=True
    FPS=60
    class Projectile:
        def __init__(self,object_name,initial_vel):
            self.object_name=object_name
            self.initial_vel=initial_vel


    while running:
        pygame.time.Clock().tick(framerate=FPS)
        WIN=pygame.display.set_mode((WIDTH, HEIGHT),flags)
        pygame.draw.polygon(WIN,RED,points=[(100,600),(300,500),(800,800)],width=1)
        pygame.display.flip()



        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                quit()


if __name__=="__main__":
    main_body()