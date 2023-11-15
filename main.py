import pygame
import sys
 
# step1 : set screen, fps
# step2 : show dino, jump dino
# step3 : show tree, move tree
 
pygame.init()
pygame.display.set_caption('Fish Hunting Adventure')
# 1. 창 크기 지정
MAX_WIDTH = 1000
MAX_HEIGHT = 500
 
def main():
    # set screen, fps
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # dino
    # 2. 펭귄 이미지 로드
    imgDino1 = pygame.image.load('img/peng1.png')
    imgDino2 = pygame.image.load('img/peng2.png')
    imgDino3 = pygame.image.load('img/peng_jump.png')
    # 3. 펭귄 이미지 스케일 조정
    imgDino1 = pygame.transform.scale(imgDino1, (100, 100))
    imgDino2 = pygame.transform.scale(imgDino2, (100, 100))
    imgDino3 = pygame.transform.scale(imgDino3, (100, 100))
    dino_height = imgDino1.get_size()[1] # 100
    dino_bottom = MAX_HEIGHT - dino_height # 400
    dino_x = 50
    dino_y = dino_bottom
    jump_top = 220
    leg_swap = True
    is_bottom = True
    is_go_up = False
 
    # tree
    # 4. 바다사자 이미지 로드
    imgTree = pygame.image.load('img/seal.png')
    # 5. 바다사자 이미지 스케일 조정
    imgTree = pygame.transform.scale(imgTree, (80, 80))
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height

    # dino-space
    dino_char = imgDino1.get_rect()
    tree_char = imgTree.get_rect()

    while True:
        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if is_bottom:
                    is_go_up = True
                    is_bottom = False
 
        # dino move
        if is_go_up:
            dino_y -= 10.0
        elif not is_go_up and not is_bottom:
            dino_y += 10.0
 
        # dino top and bottom check
        if is_go_up and dino_y <= jump_top:
            is_go_up = False
 
        if not is_bottom and dino_y >= dino_bottom:
            is_bottom = True
            dino_y = dino_bottom
 
        # tree move
        tree_x -= 12.0
        if tree_x <= 0:
            tree_x = MAX_WIDTH

        # ADD: game_over: tree와 dino가 겹칠 시 게임 종료
        dino_char.left = dino_x
        dino_char.top = dino_y
        tree_char.left = tree_x
        tree_char.top = tree_y

        if dino_char.colliderect(tree_char): 
            time.sleep(0.5)
            screen.fill(SEAGREEN)
            screen.blit(game_over, (280, 200))
            time.sleep(1)

        # 6. 배경 이미지 추가
        background = pygame.image.load("./img/main_background.jpg")
        background = pygame.transform.scale(background, (MAX_WIDTH, MAX_HEIGHT))
        screen.blit(background, (0, 0))

        # draw tree
        screen.blit(imgTree, (tree_x, tree_y))
 
        # draw dino
        # 7. 점프시 펭귄 점프 이미지로 변경
        if is_go_up == True: # 점프인 경우
            screen.blit(imgDino3, (dino_x, dino_y))
        else : # 나머지 경우
            if leg_swap:
                screen.blit(imgDino1, (dino_x, dino_y))
                leg_swap = False
            else:
                screen.blit(imgDino2, (dino_x, dino_y))
                leg_swap = True
        
        # update
        pygame.display.update()
        fps.tick(35)
 
 
if __name__ == '__main__':
    main()