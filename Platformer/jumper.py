import random
import sys
from pygame.locals import *

from sprite_loader import *
from player import Player
from platformer import Platforms


pygame.init()
screen_info = pygame.display.Info()

# set the width and height to the size of the screen
size = (width, height) = (screen_info.current_w, screen_info.current_h)
font = pygame.font.SysFont(None,70)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (204, 0, 255)
text = ''
text_rect = ''

def main():
    global text, text_rect
    p1_sheet = SpriteSheet('images/p1_spritesheet.png')
    p1_file = open('images/p1_spritesheet.txt', 'r')
    p1_actions = {}
    sprite_list = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    game_over = False
    # create a dictionary of all player images
    for line in p1_file:
        line = line.rstrip().split(" ")
        p1_actions[line[0]] = p1_sheet.get_image(int(line[2]), int(line[3]), int(line[4]), int(line[5]))
    # create platforms
    for i in range(height // 100):
        for j in range(width // 420):
            plat = Platforms(random.randint(5, (width-50)//10)*10, 0+120*i, 'images/grassHalf.png', 70, 40)
            platforms.add(plat)
    player = Player(platforms.sprites()[-1].rect.right-35, platforms.sprites()[-1].rect.top-35,p1_actions)
    sprite_list.add(player)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type ==  KEYDOWN:
                if event.key == K_f:
                    pygame.display.set_mode(size, FULLSCREEN)
                if event.key == K_ESCAPE:
                    pygame.display.set_mode(size)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.left()
        if keys[pygame.K_RIGHT]:
            player.right()

        if player.update(platforms):
            game_over = True
        else:
            text = font.render("Score: {}".format(player.progress), True, (255, 0, 0))
            text_rect = text.get_rect()
        screen.fill(color)
        platforms.draw(screen)
        sprite_list.draw(screen)
        screen.blit(text, text_rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
