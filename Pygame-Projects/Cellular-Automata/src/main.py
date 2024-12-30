'''
RULES:
1. LIVE_CELL WITH 2 OR 3 NEIGHBOURS SURVIVES.
2. DEAD_CELL WITH 3 LIVE NEIGHBOURS BECOMES ALIVE.
3. ALL OTHER CELLS DIE OR REMAIN DEAD.
'''

import pygame

pygame.init()

from cell_list import return_cell_list
from text import Text

class App:
    def __init__(self):
        self.width, self.height = 900, 496
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Conway's Game of Life")
        self.color = (64, 64, 64)

        self.cell_list = return_cell_list(500, self.height, 15)
        self.population = 0

        self.pause_state = True
        self.pause_text = Text(540, 10, "Paused")

        self.alive_text = Text(540, 40, f"Population: {self.population}")

    def get_alive_neighbours(self, CELL):

        Row = None
        Col = None
        neighbours = []

        for idx, row in enumerate(self.cell_list):
            for indx, cell in enumerate(row):
                if cell == CELL:
                    Row = idx
                    Col = indx

        '''
        ITERATES OVER EVERY POSSIBLE RELATIVE POSITION OF A CELL'S NEIGHBOUR,
        AND ADDS THEM TO ROW, AND COL, AND IF THEY ARE IN BOUNDS, APPENDS THEM.
        '''

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for rel_row, rel_col in directions:
            n_row, n_col = Row + rel_row, Col + rel_col

            if 0 <= n_row < len(self.cell_list) and 0 <= n_col < len(self.cell_list):
                neighbours.append(self.cell_list[n_row][n_col])

        live = 0
        for cell in neighbours:
            if cell.dead == False:
                live += 1

        return live
    
    def make_changes(self):

        new_state = [[cell.dead for cell in row] for row in self.cell_list]

        for i, row in enumerate(self.cell_list):
            for j, cell in enumerate(row):

                alive_neighbours = self.get_alive_neighbours(cell)

                if cell.dead == False and (alive_neighbours == 2 or alive_neighbours == 3):
                    new_state[i][j] = False
                elif cell.dead and (alive_neighbours == 3):
                    new_state[i][j] = False
                else:
                    new_state[i][j] = True

        for i, row in enumerate(self.cell_list):
            for j, cell in enumerate(row):
                cell.dead = new_state[i][j]             

    def get_total_alive(self):

        num = 0

        for row in self.cell_list:
            for cell in row:
                if not cell.dead:
                    num += 1

        return num
    
    def update_population(self):

        self.population = self.get_total_alive()
        self.alive_text.value = f"Population: {self.population}"
                 
    def main_function(self):

        Running = True
        while Running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if self.pause_state:

                        for row in self.cell_list:
                            for cell in row:
                                if cell.rect.collidepoint(pos):
                                    cell.dead = not cell.dead

                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_SPACE:
                        self.pause_state = not self.pause_state

                        if self.pause_state == False:
                            self.pause_text.value = "Not Paused"
                        else:
                            self.pause_text.value = "Paused"

            self.update_population()
            self.draw()
            
    def draw(self):

        self.win.fill(self.color)

        for row in self.cell_list:
            for cell in row:
                cell.draw(self.win)

        if not self.pause_state:
            self.make_changes()

        self.pause_text.draw(self.win)
        self.alive_text.draw(self.win)

        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    App().main_function()