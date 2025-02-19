import pygame
import sys
import time
import random
 
# step1 : set screen, fps
# step2 : show dino, jump dino
# step3 : show tree, move tree
 
pygame.init()
pygame.display.set_caption('Fish Hunting Adventure')
# 1. 창 크기 지정
MAX_WIDTH = 1000
MAX_HEIGHT = 500

SEAGREEN = (46, 139, 87)
game_over_image = pygame.image.load('img/game_over.jpg')  #게임 오버 이미지 로드
game_over_image = pygame.transform.scale(game_over_image, (MAX_WIDTH, MAX_HEIGHT))  # 이미지 크기 조정

# ADD: 배경음악 로드
pygame.mixer.music.load('sound/bgm.ogg')
miss_sound = pygame.mixer.Sound('sound/miss.ogg')
 
def game_start(screen):
    start_menu = pygame.image.load('img/start_menu.jpg')  # Load start menu image
    start_menu = pygame.transform.scale(start_menu, (MAX_WIDTH, MAX_HEIGHT))
    screen.blit(start_menu, (0, 0))
    pygame.display.update()

    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    pygame.mixer.music.play(-1)
                    waiting_for_key = False

def main():
    # set screen, fps
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # dino
    # 2. 펭귄 이미지 로드
    imgPeng1 = pygame.image.load('img/peng1_1.png') # 히트박스 크기 조절 이미지
    imgPeng2 = pygame.image.load('img/peng2_1.png') # 히트박스 크기 조절 이미지
    imgPeng3 = pygame.image.load('img/peng_jump_1.png') # 히트박스 크기 조절 이미지
    # 3. 펭귄 이미지 스케일 조정
    imgPeng1 = pygame.transform.scale(imgPeng1, (90, 90))
    imgPeng2 = pygame.transform.scale(imgPeng2, (90, 90))
    imgPeng3 = pygame.transform.scale(imgPeng3, (90, 90))
    peng_height = imgPeng1.get_size()[1] # 100
    peng_bottom = MAX_HEIGHT - peng_height # 400
    peng_x = 50
    peng_y = peng_bottom
    jump_top = 215
    leg_swap = True
    is_bottom = True
    is_go_up = False
 
    # tree
    imgSeal = pygame.image.load('img/seal_1.png') # 바다사자 이미지 로드
    imgSeagull = pygame.image.load('img/seagull_1.png') # 갈매기 이미지 로드
    imgSeal = pygame.transform.scale(imgSeal, (80, 80)) # 바다사자 이미지 스케일 조정
    imgSeagull = pygame.transform.scale(imgSeagull, (70, 40)) # 갈매기 이미지 스케일 조정
    seal_height = imgSeal.get_size()[1]
    seagull_height = imgSeagull.get_size()[1]
    seal_x = MAX_WIDTH
    seal_y = MAX_HEIGHT - seal_height
    seagull_x = MAX_WIDTH
    seagull_y = MAX_HEIGHT - seagull_height - 60
    

    # 점수 : fish 이미지 로드
    imgFish = pygame.image.load('img/fish.png')
    imgFish = pygame.transform.scale(imgFish, (100, 100))  # 물고기 이미지 크기 조정
    fish_x = MAX_WIDTH
    fish_y = random.randint(50, MAX_HEIGHT - 7)  # 물고기의 초기 위치를 랜덤하게 설정
    score = 0       # 점수 초기화

    # dino-space
    peng_char = imgPeng1.get_rect()
    seal_char = imgSeal.get_rect()
    fish_char = imgFish.get_rect()

    game_over_flag = False
    game_start(screen)






    while True:
        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 8. 키다운 이벤트 중 위쪽 방향키로 점프하도록 변경
                if event.key == pygame.K_UP:
                    if is_bottom and not game_over_flag:
                        is_go_up = True
                        is_bottom = False
 
        # peng move
        # 8. 속도, 질량을 이용하여 점프에 적용
        velocity = 3.8
        mass = 2
        if is_go_up:
            if velocity > 0:
                F = (0.5 * mass * (velocity * velocity))

            peng_y -= round(F)
            velocity -= 1
        
        elif not is_go_up and not is_bottom:
            F = -(0.5 * mass * (velocity * velocity))
            peng_y -= round(F)
            velocity -= 1
 
        # peng top and bottom check
        if is_go_up and peng_y <= jump_top:
            is_go_up = False
 
        if not is_bottom and peng_y >= peng_bottom:
            is_bottom = True
            peng_y = peng_bottom
 
        # seal move
        seal_x -= 12.0
        if seal_x <= 0:
            seal_x = MAX_WIDTH

        # seal move
        seagull_x -= 12.0
        if seagull_x <= 0:
            seagull_x = MAX_WIDTH

        # ADD: game_over: tree와 dino가 겹칠 시 게임 종료
        peng_char.left = peng_x
        peng_char.top = peng_y
        seal_char.left = seal_x
        seal_char.top = seal_y

        if peng_char.colliderect(seal_char): 
            time.sleep(0.5)
            pygame.mixer.music.stop()  # 배경음악 정지
            screen.fill(SEAGREEN)
            background = pygame.image.load("./img/main_background.jpg")
            background = pygame.transform.scale(background, (MAX_WIDTH, MAX_HEIGHT))
            screen.blit(background, (0, 0))
            screen.blit(game_over_image, (0, 0))  # 게임 오버 이미지를 먼저 그림
            pygame.display.update()
            miss_sound.play()
            time.sleep(2)
            pygame.quit()
            sys.exit()
            game_over_flag = True
    

        # 6. 배경 이미지 추가
        background = pygame.image.load("./img/main_background.jpg")
        background = pygame.transform.scale(background, (MAX_WIDTH, MAX_HEIGHT))
        screen.blit(background, (0, 0))

        # draw tree
        screen.blit(imgSeal, (seal_x, seal_y))
        screen.blit(imgSeagull, (seagull_x, seagull_y))
 
        # draw dino
        # 7. 점프시 펭귄 점프 이미지로 변경
        if is_go_up == True: # 점프인 경우
            screen.blit(imgPeng3, (peng_x, peng_y))
        else : # 나머지 경우
            if leg_swap:
                screen.blit(imgPeng1, (peng_x, peng_y))
                leg_swap = False
            else:
                screen.blit(imgPeng2, (peng_x, peng_y))
                leg_swap = True

        

        # fish move
        fish_x -= 10.0
        if fish_x < -50:  # 물고기가 화면 왼쪽 끝에 도달하면
            fish_x = MAX_WIDTH
            fish_y = random.randint(50, MAX_HEIGHT - 7)  # 물고기 위치 재설정

        # ADD: fish와 peng_char가 겹칠 시 fish 재배치 및 score 증가
        fish_char.left = fish_x
        fish_char.top = fish_y
        if peng_char.colliderect(fish_char):
            fish_x = MAX_WIDTH
            fish_y = random.randint(50, MAX_HEIGHT - 7)
            score += 1  # 점수 증가

        # draw fish
        screen.blit(imgFish, (fish_x, fish_y))

        # Display score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))      # 점수 텍스트
        screen.blit(score_text, (10, 10))       # 화면에 점수 표시


        
        # update
        pygame.display.update()
        fps.tick(40)
 
if __name__ == '__main__':
    main()