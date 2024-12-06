import maze as mz
import agent as ag
import pygame
import sys
import buttons as bt
import os
import mainfunc as mf
import BidirectionalSearch as bs

## global variables
STATE = 'menu'
HEIGHT = 700
WIDTH = 800
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
GOLD = (212, 175, 55)

grid = [ 
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,1,1,1,1,1,1,0],
    [0,1,0,1,0,1,0,0,0,0,1,0],
    [0,0,0,1,0,1,1,1,1,0,1,0],
    [0,1,1,1,1,0,0,0,1,0,1,2],
    [0,0,0,0,1,0,1,0,1,0,1,0],       ##list containing the labirinth - 0 = walls, 1 = available path, 2 = starting_position
    [0,1,1,0,1,0,1,0,1,0,1,0],
    [0,0,1,0,1,0,1,0,1,0,1,0],
    [0,1,1,1,1,1,1,1,1,0,1,0],
    [0,0,0,0,0,0,1,0,0,0,1,0],
    [1,1,1,1,1,1,1,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]
]

maze = mz.Maze(grid)  ## Maze Object

# font variables
font_path = r"C:\Users\peluc\OneDrive\Documentos\Progamação e TI\Trabalhos e Codigos da Faculdade\Inteligencia Artificial\Codigos\Projeto1\Projeto_IA_DEF\Projeto-IA\font\Cinzel\Cinzel-VariableFont_wght.ttf"
font = pygame.font.Font(font_path, 70)

## init of the basic variabels for the interface
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
pygame.display.set_caption('Projeto Inteligencia Artificial')

## loading the background images
background_img = pygame.image.load(os.path.join('images', 'tomb_raider2.png'))
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))


## buttons will be placed on the lower half of the screen with a space of 10 pixels between each button
buttons_menu = [
    bt.Button(((WIDTH - 500) / 2), 360, 70, 500, 'Busca Em Largura', GOLD, GREEN, 'Busca Em Largura'),
    bt.Button(((WIDTH - 500) / 2), 440, 70, 500, 'Busca em Profundidade', GOLD, GREEN, 'Busca em Profundidade'),
    bt.Button(((WIDTH - 500) / 2), 520, 70, 500, 'Busca Bidirecional', GOLD, GREEN, 'Busca Bidirecional')
]

## button to go back to the menu after the maze is printeds
goback_button = bt.Button((((WIDTH - 500) / 2) + 50), 5, 40, 400, 'Voltar Para o Menu', GOLD, GREEN, 'menu')

while running:

    ## pygame.QUIT event means the user click X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ## if in menu, print menu and await for a button to be pressed
    if STATE == 'menu': 
        mf.print_menu(screen, background_img, font, buttons_menu, GOLD, font_path)
        for button in buttons_menu:
            action = button.check_click(event)
            if action:
                STATE = action

    ## if Busca em Largura get pressed, perform the wide search and print the maze
    if STATE == 'Busca Em Largura':          #y  x
            agent = ag.Agent('wide search', [4, 11])
            path_taken = agent.run(maze, [10, 0])
            print(path_taken)
            agent.set_numSteps(len(path_taken))
            print('Num Passos: ', agent.numSteps)
            STATE = maze.draw_maze(screen, path_taken, goback_button, event, GOLD, WHITE, GREEN)
           
    ## if Busca em Profundidade get pressed, perform the deep search and print the maze
    if STATE == 'Busca em Profundidade':
            agent = ag.Agent('deep search', [4, 11])
            path_taken = agent.run(maze, [10, 0])
            print(path_taken)
            agent.set_numSteps(len(path_taken))
            print('Num Passos: ', agent.numSteps)
            STATE = maze.draw_maze(screen, path_taken, goback_button, event, GOLD, WHITE, GREEN)
            
    ## if Busca Bidirecional get pressed, perform the bidirectional search and print the maze
    if STATE == 'Busca Bidirecional':
            agent = ag.Agent('bidirectional search', (4, 11))
            path_taken = agent.run(maze, (10, 0))
            print(path_taken)
            agent.set_numSteps(len(path_taken))
            print('Num Passos: ', len(path_taken))
            STATE = maze.draw_maze(screen, path_taken, goback_button, event, GOLD, WHITE, GREEN)
            
            

pygame.quit()