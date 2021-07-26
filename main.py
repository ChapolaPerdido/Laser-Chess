from pygame.locals import *
import os

from constants import *


# DIRECTORY MANAGEMENT ------------------------------------------#
main_dir = os.path.dirname(__file__)
img_dir = os.path.join(main_dir, 'sprites')

# WINDOW SETUP ------------------------------------------#
FPS = 60

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Laser Chess')

sprite_sheet = pygame.image.load('sprites/sprite_sheet/Pieces_SpriteSheet.png').convert_alpha()


# MAIN LOOP ------------------------------------------#
def main():

    running = True
    while running:
        clock.tick(FPS)

        # Mouse location ------------------------------------------#
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_loc = [mouse_x, mouse_y]

        # Draw board ------------------------------------------#
        window.blit(board, (BOARD_X0, BOARD_Y0))

        # Event list ------------------------------------------#
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # Mouse Inputs ------------------------------------------#
            if event.type == MOUSEMOTION:
                pass

        pygame.display.flip()

    pygame.quit()


main()
