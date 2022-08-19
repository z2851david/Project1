import pygame

#----------test values----------------#
WIDTH, HEIGHT = 400, 400
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


#--------test values------------------#

def start_button(WIN,event):
        font=pygame.font.Font("freesansbold.ttf",18)
        text=font.render("Start",True,"orange",)
        textrect=text.get_rect()
        textrect.center=(WIDTH//1.12,HEIGHT//1.1)

        mouse = pygame.mouse.get_pos()

        if (WIDTH // 1.12) - (text.get_width() // 2) <= mouse[0] <= (WIDTH // 1.12) + (text.get_width() // 2) and \
                (HEIGHT // 1.1) - (text.get_height() // 2) <= mouse[1] <= (HEIGHT // 1.1) + (text.get_height() // 2):

            pygame.draw.rect(WIN, "white", textrect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                is_run=True
                return is_run
        else:
            pygame.draw.rect(WIN, "black", textrect)
        is_run=False
        WIN.blit(text,textrect)
        return is_run


if __name__=="__main__":
    start_button(WIN)