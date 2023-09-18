import pygame
from colors import Colors

class Grid:
    def __init__(self) -> None:
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] 
                     for i in range(self.num_rows )]
        self.colors = Colors.get_cell_colors()
        

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=' ')
            print()
    
    def is_inside(self, row, column):
        if row >= 0 and row <self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False
    
    
    """ 
    How pygame draw

    Basic concept:
    1. Display surface -> it is like the blank Canvas, we can only have one per game.

        screen = pygame.display.set_mode((<Width>, <height>))

    2. Surface -> Another type of blank Canvas, We can have many surfaces per game.


    3. Rect -> Rectangles are used for positioning, collision detection and for drawing objects.
        a) Rect(<X position>, <Y position>, <Width>, <Height>)
        b) rect(<surface>, color, Rect)

    """

    
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size + 1, 
                                        row*self.cell_size + 1, 
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)



            







            