import pygame

class Button:

    # button constructor
    def __init__(self, x, y, height, width, text, idle_color, hover_color, action):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text
        self.idle_color = idle_color
        self.hover_color = hover_color
        self.action = action

    ## function to draw the button
    def draw(self, screen):

        font_path = r"C:\Users\peluc\OneDrive\Documentos\Progamação e TI\Trabalhos e Codigos da Faculdade\Inteligencia Artificial\Codigos\Projeto1\Projeto_IA_DEF\Projeto-IA\font\Cinzel\Cinzel-VariableFont_wght.ttf"
        font = pygame.font.Font(font_path, 36)

        mouse = pygame.mouse.get_pos()

        ## if hovered, change color
        if self.is_hovered(mouse):
            pygame.draw.rect(screen, self.hover_color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.idle_color, (self.x, self.y, self.width, self.height))

        # print the text inside the button
        text_surface = font.render(self.text, True, (212, 155, 55))
        shadow = font.render(self.text, True, (50, 50, 50))
        text_x = self.x + (self.width - text_surface.get_width()) // 2
        text_y = self.y + (self.height - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))
        screen.blit(shadow, (text_x + 2, text_y + 2))

    ## function to check if its hovered 
    def is_hovered(self, mouse_pos):
        """Verifica se o mouse está sobre o botão."""
        return self.x + self.width > mouse_pos[0] > self.x and self.y + self.height > mouse_pos[1] > self.y 
    
    ## function to check if a button got clicked 
    def check_click(self, event):
        """Verifica se o botão foi clicado."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clique esquerdo
            if self.is_hovered(pygame.mouse.get_pos()):
                return self.action
        return None