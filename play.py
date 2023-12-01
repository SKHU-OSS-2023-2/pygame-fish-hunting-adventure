import pygame
import random
import sys
pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 500

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load("./img/peng_run_1.png"),
           pygame.image.load("./img/peng_run_2.png")]
JUMPING = pygame.image.load("./img/peng_jump.png")
DUCKING = pygame.image.load("./img/peng_duck.png")

SEAL = pygame.image.load("./img/seal.png")
SEAGULL = pygame.image.load("./img/seagull.png")

BG = pygame.image.load("./img/main_background.png")
BGDARK = [pygame.image.load("./img/background/darker_ver1.png"),
        pygame.image.load("./img/background/darker_ver2.png")]

class Peng:
    X_POS = 80
    Y_POS = 350
    Y_POS_DUCK = 370
    JUMP_VEL = 8.5

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
        self.rect.y = 310
        self.index = 0
    
    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image, self.rect)
        self.index += 1

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, current_bg
    run = True
    clock = pygame.time.Clock()
    player = Peng()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0
    current_bg = 0  # 현재 배경 추적 변수

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

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
            if random.randint(0, 1) == 0:
                obstacles.append(Seal(SEAL))
            elif random.randint(0, 1) == 1:
                obstacles.append(SeaGull(SEAGULL))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.peng_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                death_count += 1
                menu(death_count)

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)