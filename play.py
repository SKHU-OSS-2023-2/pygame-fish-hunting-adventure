import pygame
import random
import sys
pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 500

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
STORY_SCREEN = pygame.image.load('img/story_screen.jpg')
START_BACKGROUND = pygame.image.load("./img/start_menu.jpg")
DEATH_SCREEN = pygame.image.load("./img/game_over.jpg")

RUNNING = [pygame.image.load("./img/peng_run_1.png"),
           pygame.image.load("./img/peng_run_2.png")]
JUMPING = pygame.image.load("./img/peng_jump.png")
DUCKING = pygame.image.load("./img/peng_duck.png")

SEAL = pygame.image.load("./img/seal.png")
SEAGULL = pygame.image.load("./img/seagull.png")
FISH = pygame.image.load("./img/fish.png")

BG = pygame.image.load("./img/main_background.png")
BGDARK = [pygame.image.load("./img/background/darker_ver1.png"),
        pygame.image.load("./img/background/darker_ver2.png")]
START_SOUND = pygame.mixer.Sound('sound/bgm.ogg')
MISS_SOUND = pygame.mixer.Sound('sound/miss.ogg')
COIN_SOUND = pygame.mixer.Sound('sound/candy.ogg')

class Peng:
    X_POS = 80
    Y_POS = 350
    Y_POS_DUCK = 370
    JUMP_VEL = 8

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.peng_duck = False
        self.peng_run = True
        self.peng_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.peng_rect = self.image.get_rect()
        self.peng_rect.x = self.X_POS
        self.peng_rect.y = self.Y_POS

    def update(self, userInput):
        if self.peng_duck:
            self.duck()
        if self.peng_run:
            self.run()
        if self.peng_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.peng_jump:
            self.peng_duck = False
            self.peng_run = False
            self.peng_jump = True
        elif userInput[pygame.K_DOWN] and not self.peng_jump:
            self.peng_duck = True
            self.peng_run = False
            self.peng_jump = False
        elif not (self.peng_jump or userInput[pygame.K_DOWN]):
            self.peng_duck = False
            self.peng_run = True
            self.peng_jump = False

    def duck(self):
        self.image = self.duck_img
        self.peng_rect = self.image.get_rect()
        self.peng_rect.x = self.X_POS
        self.peng_rect.y = self.Y_POS_DUCK

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.peng_rect = self.image.get_rect()
        self.peng_rect.x = self.X_POS
        self.peng_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.peng_jump:
            self.peng_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.peng_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.peng_rect.x, self.peng_rect.y))

class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

class Seal(Obstacle):
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 350

class SeaGull(Obstacle):
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 280
        self.index = 0
    
    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image, self.rect)
        self.index += 1

class Fish(Obstacle):
    def __init__(self, image):
        super().__init__(image)
        y_pos_fish = [170, 350]
        self.rect.y = random.choice(y_pos_fish)
        self.index = 0


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, current_bg
    run = True
    clock = pygame.time.Clock()
    player = Peng()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    scores = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0
    current_bg = 0  # 현재 배경 추적 변수
    pygame.mixer.music.load('sound/bgm.ogg')
    pygame.mixer.music.play(-1)
    # START_SOUND.play(-1)

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        textPoint = font.render("Points: " + str(points), True, (0, 0, 0))
        textScore = font.render("Score: " + str(scores), True, (0, 0, 0))
        textPointRect = textPoint.get_rect()
        textScoreRect = textScore.get_rect()
        textPointRect.center = (1000, 40)
        textScoreRect.center = (1000, 80)
        SCREEN.blit(textPoint, textPointRect)
        SCREEN.blit(textScore, textScoreRect)

    def background():
        global x_pos_bg, y_pos_bg, current_bg
        image_width = BG.get_width()

        # 현재 화면 초기화
        if current_bg == 0:
            SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        else:
            darkbg = BGDARK[current_bg - 1]
            SCREEN.blit(darkbg, (x_pos_bg, y_pos_bg))
            SCREEN.blit(darkbg, (image_width + x_pos_bg, y_pos_bg))
        
        # 화면 연속적으로 그려주기
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed - 17

        # 300점마다 화면 전환
        global points
        if points % 300 == 0 and points != 0:
            current_bg = (current_bg + 1) % (len(BGDARK) + 1)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        userInput = pygame.key.get_pressed()

        background()
        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 30) <= 9:
                obstacles.append(Seal(SEAL))
            elif random.randint(0, 30) <= 14:
                obstacles.append(SeaGull(SEAGULL))
            elif random.randint(0, 30) <= 29:
                obstacles.append(Fish(FISH))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.peng_rect.colliderect(obstacle.rect):
                if(obstacle.image == FISH):
                    obstacles.remove(obstacle)
                    scores += 1
                    COIN_SOUND.play()
                else:
                    pygame.mixer.music.stop()
                    pygame.time.delay(1000)
                    death_count += 1
                    menu(death_count)

        score()

        clock.tick(30)
        pygame.display.update()
    pygame.mixer.music.stop()


def menu(death_count):
    global points
    run = True 
    if death_count > 0:
        # START_SOUND.stop()
        MISS_SOUND.play()
        SCREEN.blit(DEATH_SCREEN,(0,0)) 
        pygame.display.update()
        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # r 키를 누르면 처음 메인 화면으로 돌아감
                        waiting_for_key = False
                        main()
    elif death_count == 0:
        while run:
            SCREEN.blit(START_BACKGROUND,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        SCREEN.blit(STORY_SCREEN,(0,0))
                        pygame.display.update()
                        waiting_for_key = True
                        while waiting_for_key:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_s:
                                            main()
            

menu(death_count=0)