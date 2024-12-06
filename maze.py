import pygame

class Maze: 
    ## constructor
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])

    ## function to check if the position the agent wants to move to is valid
    def valid_or_not(self, y, x):
        return 0 <= x < self.columns and 0 <= y < self.rows and self.grid[y][x] == 1

    def draw_maze(self, screen, path_positions, goback_button, event, GOLD, WHITE, GREEN):
        cell_width = 700 // self.columns
        cell_height = 600 // self.rows

        for row in range(self.rows):
            for colum in range(self.columns):
                if self.grid[row][colum] == 1:
                    color = WHITE  
                elif self.grid[row][colum] == 2:
                    color = GREEN 
                else:
                    color = GOLD 

                x = 50 + colum * cell_width
                y = 50 + row * cell_height

                pygame.draw.rect(screen, color, (x, y, cell_width, cell_height))

                pygame.draw.rect(screen, (200, 200, 200), (x, y, cell_width, cell_height), 1)

        pygame.display.flip()

        clock = pygame.time.Clock()
        for position in path_positions:
            row, colum = position
            x = 50 + colum * cell_width
            y = 50 + row * cell_height

            pygame.draw.rect(screen, GREEN, (x, y, cell_width, cell_height))  

            pygame.draw.rect(screen, (200, 200, 200), (x, y, cell_width, cell_height), 1)

            pygame.display.flip()

            clock.tick(5)   

        while True:
            goback_button.draw(screen)  
            pygame.display.flip()  

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()
                    exit()
                if goback_button.check_click(event):  
                    return goback_button.action

       