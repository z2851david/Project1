import pygame
#-----------------------test values---------------------#
WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
#----------------------test values----------------------#

def menu1(WIN,WIDTH,HEIGHT,font):
    WIN.fill("gray")
    text = font.render("Choose a motion", True, "green")
    textrect = text.get_rect()
    textrect.center = (WIDTH // 2, HEIGHT // 6)
    text2=font.render("Vertical",True,"green")
    text2rect=text2.get_rect()
    text2rect.center=(WIDTH//2,HEIGHT//2.7)
    text3=font.render("Exit",True,"red")
    text3rect=text3.get_rect()
    text3rect.center=(WIDTH//2,HEIGHT/1.3)
    text4=font.render("Horizontal",True,"purple")
    text4rect=text4.get_rect()
    text4rect.center=(WIDTH//2,HEIGHT/1.8)


    while True:
        mouse=pygame.mouse.get_pos()
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                quit()
            if (WIDTH//2)-(text2.get_width()//2 ) <= mouse[0] <= (WIDTH//2)+(text2.get_width()//2) and\
                (HEIGHT//2.7)-(text2.get_height()//2)<= mouse[1] <=(HEIGHT//2.7)+(text2.get_height()//2):

                pygame.draw.rect(WIN,"black",text2rect)
                if events.type==pygame.MOUSEBUTTONDOWN:
                    setting_motion="vertical"
                    menu1_on=False
                    menu2_on=True
                    return setting_motion,menu1_on,menu2_on
            else:
                pygame.draw.rect(WIN,"gray",text2rect)


            if (WIDTH//2)-(text3.get_width()//2 ) <= mouse[0] <= (WIDTH//2)+(text3.get_width()//2) and\
                (HEIGHT//1.3)-(text3.get_height()//2)<= mouse[1] <=(HEIGHT//1.3)+(text3.get_height()//2):

                pygame.draw.rect(WIN,"black",text3rect)
                if events.type==pygame.MOUSEBUTTONDOWN:
                    quit()
            else:
                pygame.draw.rect(WIN,"gray",text3rect)

            if (WIDTH // 2) - (text4.get_width() // 2) <= mouse[0] <= (WIDTH // 2) + (text4.get_width() // 2) and \
                    (HEIGHT // 1.8) - (text4.get_height() // 2) <= mouse[1] <= (HEIGHT // 1.8) + (
                    text4.get_height() // 2):

                pygame.draw.rect(WIN, "black", text4rect)
                if events.type == pygame.MOUSEBUTTONDOWN:
                    setting_motion="horizontal"
                    menu1_on=False
                    menu2_on=True
                    return setting_motion,menu1_on,menu2_on
            else:
                pygame.draw.rect(WIN, "gray", text4rect)

        WIN.blit(text,textrect)
        WIN.blit(text2,text2rect)
        WIN.blit(text3,text3rect)
        WIN.blit(text4,text4rect)
        pygame.display.update()




def menu2(WIN,WIDTH,HEIGHT,font):
    WIN.fill("gray")
    text = font.render("Choose a projectile", True, "blue")
    textrect=text.get_rect()
    textrect.center=(WIDTH//2,HEIGHT//5)
    text2=font.render("Circle",True,"blue")
    text2rect=text2.get_rect()
    text2rect.center=(WIDTH//2,HEIGHT//2)
    text3=font.render("Go back",True,"red")
    text3rect=text3.get_rect()
    text3rect.center=(WIDTH//2,HEIGHT/1.2)


    while True:
        mouse = pygame.mouse.get_pos()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                quit()
            if (WIDTH // 2) - (text2.get_width() // 2) <= mouse[0] <= (WIDTH // 2) + (text2.get_width() // 2) and \
                    (HEIGHT // 2) - (text2.get_height() // 2) <= mouse[1] <= (HEIGHT // 2) + (text2.get_height() // 2):

                pygame.draw.rect(WIN, "black", text2rect)
                if events.type == pygame.MOUSEBUTTONDOWN:
                    setting_projectile = "circle"
                    menu2_on=False
                    menu1_on=False
                    return setting_projectile,menu1_on,menu2_on
            else:
                pygame.draw.rect(WIN, "gray", text2rect)


            if (WIDTH//2)-(text3.get_width()//2 ) <= mouse[0] <= (WIDTH//2)+(text3.get_width()//2) and\
                (HEIGHT//1.2)-(text3.get_height()//2)<= mouse[1] <=(HEIGHT//1.2)+(text3.get_height()//2):

                pygame.draw.rect(WIN,"black",text3rect)
                if events.type==pygame.MOUSEBUTTONDOWN:
                    setting_projectile=""
                    menu1_on=True
                    menu2_on=False
                    return setting_projectile,menu1_on,menu2_on
            else:
                pygame.draw.rect(WIN,"gray",text3rect)

        WIN.blit(text, textrect)
        WIN.blit(text2, text2rect)
        WIN.blit(text3,text3rect)
        pygame.display.update()

if __name__=="__main__":
    menu2(WIN,WIDTH,HEIGHT)
