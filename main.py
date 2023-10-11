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
