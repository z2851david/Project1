import pygame
import login_page

def menu1(WIN,setting_obj,font):
    pygame.init()
    WIN.fill("black")
    text = font.render("Welcome to the simulation", True, "turquoise")
    textrect = text.get_rect()
    textrect.center = (setting_obj.window_width // 2, setting_obj.window_height// 6)
    text2=font.render("Start",True,"turquoise")
    text2rect=text2.get_rect()
    text2rect.center=(setting_obj.window_width//2,setting_obj.window_height//2.7)
    text3=font.render("Exit",True,"turquoise")
    text3rect=text3.get_rect()
    text3rect.center=(setting_obj.window_width//2,setting_obj.window_height//1.7)



    while not setting_obj.close_main1:
        mouse=pygame.mouse.get_pos()
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                quit()
            if (setting_obj.window_width //2)-(text2.get_width()//2 ) <= mouse[0] <= (setting_obj.window_width //2)+(text2.get_width()//2) and\
                (setting_obj.window_height //2.7)-(text2.get_height()//2)<= mouse[1] <=(setting_obj.window_height //2.7)+(text2.get_height()//2):

                pygame.draw.rect(WIN,"white",text2rect)
                if events.type==pygame.MOUSEBUTTONDOWN:
                     login_page.main_page(setting_obj)


            else:
                pygame.draw.rect(WIN,"black",text2rect)


            if (setting_obj.window_width //2)-(text3.get_width()//2 ) <= mouse[0] <= (setting_obj.window_width //2)+(text3.get_width()//2) and\
                (setting_obj.window_height //1.7)-(text3.get_height()//2)<= mouse[1] <=(setting_obj.window_height //1.7)+(text3.get_height()//2):

                pygame.draw.rect(WIN,"red",text3rect)
                if events.type==pygame.MOUSEBUTTONDOWN:
                    quit()
            else:
                pygame.draw.rect(WIN,"black",text3rect)

        WIN.blit(text,textrect)
        WIN.blit(text2,text2rect)
        WIN.blit(text3,text3rect)
        pygame.display.update()




def menu2(WIN,setting_obj,font):
    WIN.fill("black")
    text = font.render("Choose a projectile", True, "turquoise")
    textrect=text.get_rect()
    textrect.center=(setting_obj.window_width //2,setting_obj.window_height //5)
    text2=font.render("Horizontal",True,"turquoise")
    text2rect=text2.get_rect()
    text2rect.center=(setting_obj.window_width //2,setting_obj.window_height //1.7)
    text3=font.render("Go back",True,"turquoise")
    text3rect=text3.get_rect()
    text3rect.center=(setting_obj.window_width //2,setting_obj.window_height //1.2)
    text4=font.render("Vertical",True,"turquoise")
    text4rect=text4.get_rect()
    text4rect.center=(setting_obj.window_width //2,setting_obj.window_height //2.6)


    while True:
        mouse = pygame.mouse.get_pos()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                quit()
            if (setting_obj.window_width // 2) - (text2.get_width() // 2) <= mouse[0] <= (setting_obj.window_width // 2) + (text2.get_width() // 2) and \
                    (setting_obj.window_height // 1.7) - (text2.get_height() // 2) <= mouse[1] <= (setting_obj.window_height // 1.7) + (text2.get_height() // 2):

                pygame.draw.rect(WIN, "white", text2rect)
                if events.type == pygame.MOUSEBUTTONDOWN:
                    setting_motion = "horizontal"
                    setting_obj.menu2_on=False
                    setting_obj.menu1_on=False
                    return setting_motion
            else:
                pygame.draw.rect(WIN, "black", text2rect)


            if (setting_obj.window_width //2)-(text3.get_width()//2 ) <= mouse[0] <= (setting_obj.window_width //2)+(text3.get_width()//2) and\
                (setting_obj.window_height //1.2)-(text3.get_height()//2)<= mouse[1] <=(setting_obj.window_height //1.2)+(text3.get_height()//2):

                pygame.draw.rect(WIN,"red",text3rect)
                if events.type==pygame.MOUSEBUTTONDOWN:
                    setting_motion=""
                    setting_obj.menu1_on=True
                    setting_obj.menu2_on=False
                    setting_obj.close_main1=False
                    return setting_motion
            else:
                pygame.draw.rect(WIN,"black",text3rect)


            if (setting_obj.window_width // 2) - (text4.get_width() // 2) <= mouse[0] <= (setting_obj.window_width // 2) + (text4.get_width() // 2) and \
                    (setting_obj.window_height // 2.6) - (text4.get_height() // 2) <= mouse[1] <= (setting_obj.window_height // 2.6) + (text4.get_height() // 2):

                pygame.draw.rect(WIN, "white", text4rect)
                if events.type == pygame.MOUSEBUTTONDOWN:
                    setting_motion = "vertical"
                    setting_obj.menu2_on=False
                    setting_obj.menu1_on=False
                    return setting_motion
            else:
                pygame.draw.rect(WIN, "black", text4rect)


        WIN.blit(text, textrect)
        WIN.blit(text2, text2rect)
        WIN.blit(text3,text3rect)
        WIN.blit(text4,text4rect)
        pygame.display.update()

