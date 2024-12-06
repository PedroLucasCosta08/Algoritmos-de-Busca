import pygame
import sys

pygame.font.init()

def print_menu(screen, background_img, font, buttons, color, font_path):
    ## printing the interface 
    screen.blit(background_img, (0, 0))
    text = font.render('Maze Raider Menu', True, color)
    shadow = font.render('Maze Raider Menu', True, (50, 50, 50)) ## font definition
    screen.blit(text, (800 // 2 - text.get_width() // 2, 60))
    screen.blit(shadow, (800 // 2 - text.get_width() // 2 + 2, 62))
    font = pygame.font.Font(font_path, 70)
    text = font.render('Escolha uma Busca', True, color)
    shadow = font.render('Escolha uma Busca', True, (50, 50, 50))
    screen.blit(text, (800 // 2 - text.get_width() // 2, 280))
    screen.blit(shadow, (800 // 2 - text.get_width() // 2 + 2, 282))

    ## printing the buttons
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()