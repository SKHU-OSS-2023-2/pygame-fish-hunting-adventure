import pygame
import sys
 
# step1 : set screen, fps
# step2 : show dino, jump dino
# step3 : show tree, move tree
 
pygame.init()
pygame.display.set_caption('Jumping dino')
MAX_WIDTH = 800
MAX_HEIGHT = 400
 
def main():
    # set screen, fps
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # dino
    imgDino1 = pygame.image.load('img/dino1.png')
    imgDino2 = pygame.image.load('img/dino2.png')
    dino_height = imgDino1.get_size()[1]
    dino_bottom = MAX_HEIGHT - dino_height
    dino_x = 50
    dino_y = dino_bottom
    jump_top = 200
    leg_swap = True
    is_bottom = True
    is_go_up = False

    # dino-space
    dino_char = imgDino1.get_rect()
    tree_char = imgTree.get_rect()
 
    # tree
    imgTree = pygame.image.load('img/tree.png')
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height

 
    while True:
        screen.fill((255, 255, 255))
 
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
    
        # draw tree
        screen.blit(imgTree, (tree_x, tree_y))
 
        # draw dino
        if leg_swap:
            screen.blit(imgDino1, (dino_x, dino_y))
            leg_swap = False
        else:
            screen.blit(imgDino2, (dino_x, dino_y))
            leg_swap = True
 
        # update
        pygame.display.update()
        fps.tick(30)
 
 
if __name__ == '__main__':
    main()