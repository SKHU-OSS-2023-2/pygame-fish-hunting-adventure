import pygame, sys
# from button import Button

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('물고기 사냥 대작전')

#배경 이미지 설정
main_img = pygame.image.load("pygame-fish-hunting-adventure/img/start_menu.jpg")
main_img = pygame.transform.scale(main_img, (1280, 720))
#버튼 이미지 설정
button_img = pygame.image.load("pygame-fish-hunting-adventure/img/start_button.png")
button_img = pygame.transform.scale(button_img, (300, 100)) 

button_rect = button_img.get_rect()
button_rect.center = (620, 400)

MAX_WIDTH = 300
MAX_HEIGHT = 350

def quitgame():
    pygame.quit()
    sys.exit()

def play_game():
    start_img = pygame.image.load("pygame-fish-hunting-adventure/img/main_background.png")
    start_img = pygame.transform.scale(start_img, (1280, 720))

    player_img1 = pygame.image.load("pygame-fish-hunting-adventure/img/player_run1.png")
    player_img2 = pygame.image.load("pygame-fish-hunting-adventure/img/player_run2.png")
    pen_height = player_img1.get_size()[1]
    pen_bottom = MAX_HEIGHT - pen_height
    pen_x = 30
    pen_y = pen_bottom
    jump_top = 200
    leg_swap = True
    is_bottom = True
    is_go_up = False

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 게임 화면 그리기
        SCREEN.blit(start_img, (0, 0))
        if leg_swap:
            SCREEN.blit(player_img1, (pen_x, pen_y))
        else:
            SCREEN.blit(player_img2, (pen_x, pen_y))

        pygame.display.update()

        # 다음 프레임을 위해 시간 지연# 초당 60프레임으로 제한




def introScreen():
    intro =True
    while  intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    intro = False

SCREEN.blit(main_img,(-2,-2))   
SCREEN.blit(button_img, button_rect.topleft)  
pygame.display.update()

introScreen()

