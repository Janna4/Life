"""
Programmer: Janna Schmidt
Start Date: 2/3/2020
Updated: 2/20/2020
"""

from cell import Cell
import random

class World(object):

    def __init__(self, rows, columns, speed):
        self.__rows = rows
        self.__columns = columns
        self.__grid = self.create_grid()
        self.__generationsDone = 1
        self.__speed = speed
        self.create_neighbors()

    def __str__(self):
        """Return a string that represents the current generation. For example,
        a completely dead world (4x5) would look like this, assuming that
        Cell.deadChar is a period:
        .....
        .....
        .....
        .....
        A world (4x5) with one living cell would look like this, assuming
        that Cell.liveChar is an 'X' at position self.__grid[1][3]:
        .....
        ...X.
        .....
        .....
        Of course, you would not check on Cell.deadChar or Cell.liveChar. You
        would rely on the cell to know how it should be printed.
        """
        string = ''
        for row in self.__grid:
            for cell in row:
                string += cell.__str__()
            string += '\n'
        dimensions = f'{self.__rows} by {self.__columns}'
        percentAlive = self.find_living()
        string += (f'\nDimensions: {dimensions}    Percent Living: {percentAlive}   Generation #: {self.__generationsDone}  Speed: 1 gen every {self.__speed} seconds')
        return string

    def get_rows(self):
        return self.__rows

    def get_columns(self):
        return self.__columns

    def get_grid(self):
        return self.__grid

    def set_speed(self, seconds):
        self.__speed = seconds

    def find_living(self):
        """
        Returns a string showing the percent of living cells
        :return: the percent of cells living
        """
        amountAlive = 0
        numberOfCells = self.__columns * self.__rows

        for row in self.__grid:
            for cell in row:
                living = cell.get_living()
                if living:
                    amountAlive += 1

        percentLiving = amountAlive/numberOfCells
        percentLiving = percentLiving*100
        percentLiving = f'{percentLiving:0.2f}'
        return percentLiving

    def random_fill(self, percentLiving = 50):
        """
        Make random cells in a grid alive.
        :param percentLiving: This is the percent of characters the user wants living (as a whole number)
        :return: None
        """
        #todo make sure they send in a legal percent value
        for row in self.__grid:
            for cell in row:
                state = random.randrange(1, 100)
                if state <= percentLiving:
                    cell.set_living(True)

    def create_grid(self):
        """
        Return the grid as a list of lists. There should be one list
        to contain the entire grid and in that list there should be one
        list to contain each row in the generation. Each of the "row lists"
        should contain one object of class Cell for each column in the world.
        :return: a string containing the newly created grid
        """

        grid = []
        for rowNumber in range(self.__rows):
            row = []
            for columnNumber in range(self.__columns):
                row.append(Cell(rowNumber, columnNumber))
            grid.append(row)
        return grid

    def create_neighbors(self):
        """
        Loop through the grid and assign the neighbors to each cell.
        :return: None
        """
        for row in self.__grid:
            for cell in row:
                #
                # There are some nine situations that we have to account for:
                #
                # 1. upper left corner
                # 2. rest of the top row
                # 3. upper right corner
                # 4. far left side
                # 5. normal cells
                # 6. far right side
                # 7. lower left corner
                # 8. rest of bottom row
                # 9. lower right corner (3 neighbors)
                #
                row = cell.get_row()
                column = cell.get_column()
                #print(f'({row},{column})')
                # top row
                if row == 0:
                    # 1. upper left corner
                    if column == 0:
                        #print('upper left')
                        cell.add_neighbor(self.__grid[row][column+1])
                        cell.add_neighbor(self.__grid[row+1][column])
                        cell.add_neighbor(self.__grid[row+1][column+1])
                        cell.add_neighbor(self.__grid[row][self.__columns - 1])
                        cell.add_neighbor(self.__grid[row + 1][self.__columns - 1])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column + 1])
                        cell.add_neighbor(self.__grid[self.__rows - 1][self.__columns - 1])
                    # 2. rest of the top row
                    elif column < (self.__columns - 1):
                        #print('upper')
                        cell.add_neighbor(self.__grid[row][column-1])
                        cell.add_neighbor(self.__grid[row][column+1])
                        cell.add_neighbor(self.__grid[row+1][column-1])
                        cell.add_neighbor(self.__grid[row+1][column])
                        cell.add_neighbor(self.__grid[row+1][column+1])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column - 1])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column])
                        cell.add_neighbor(self.__grid[self.__rows - 1][column + 1])
                    # upper right corner
                    else:
                        #print('upper right')
                        cell.add_neighbor(self.__grid[row][column-1])
                        cell.add_neighbor(self.__grid[row+1][column-1])
                        cell.add_neighbor(self.__grid[row+1][column])
                        cell.add_neighbor(self.__grid[0][0])
                        cell.add_neighbor(self.__grid[1][0])
                        cell.add_neighbor(self.__grid[self.__rows - 1][self.__columns - 1])
                        cell.add_neighbor(self.__grid[self.__rows - 1][self.__columns - 2])
                        cell.add_neighbor(self.__grid[0][self.__columns - 1])
                # middle row
                elif row < (self.__rows - 1):
                    #1. middle left
                    if column == 0:
                        #print('middle left')
                        cell.add_neighbor(self.__grid[row - 1][column])
                        cell.add_neighbor(self.__grid[row - 1][column + 1])
                        cell.add_neighbor(self.__grid[row][column + 1])
                        cell.add_neighbor(self.__grid[row + 1][column])
                        cell.add_neighbor(self.__grid[row + 1][column + 1])
                        cell.add_neighbor(self.__grid[row][self.__columns - 1])
                        cell.add_neighbor(self.__grid[row - 1][self.__columns - 1])
                        cell.add_neighbor(self.__grid[row + 1][self.__columns - 1])
                    #2. the rest of the middle row (8 neighbors)
                    elif column < (self.__columns - 1):
                        #print('middle')
                        cell.add_neighbor(self.__grid[row - 1][column - 1])
                        cell.add_neighbor(self.__grid[row - 1][column])
                        cell.add_neighbor(self.__grid[row - 1][column + 1])
                        cell.add_neighbor(self.__grid[row][column - 1])
                        cell.add_neighbor(self.__grid[row][column + 1])
                        cell.add_neighbor(self.__grid[row + 1][column - 1])
                        cell.add_neighbor(self.__grid[row + 1][column])
                        cell.add_neighbor(self.__grid[row + 1][column + 1])
                    #3. middle right
                    else:
                        #print('middle right')
                        cell.add_neighbor(self.__grid[row - 1][column])
                        cell.add_neighbor(self.__grid[row - 1][column - 1])
                        cell.add_neighbor(self.__grid[row][column - 1])
                        cell.add_neighbor(self.__grid[row + 1][column])
                        cell.add_neighbor(self.__grid[row + 1][column - 1])
                        cell.add_neighbor(self.__grid[row][0])
                        cell.add_neighbor(self.__grid[row - 1][0])
                        cell.add_neighbor(self.__grid[row + 1][0])
                # bottom row
                else:
                    # 1. lower left corner
                    if column == 0:
                        #print('lower left')
                        cell.add_neighbor(self.__grid[row][column + 1])
                        cell.add_neighbor(self.__grid[row - 1][column])
                        cell.add_neighbor(self.__grid[row - 1][column + 1])
                        cell.add_neighbor(self.__grid[self.__rows - 2][self.__columns - 1])
                        cell.add_neighbor(self.__grid[self.__rows - 1][self.__columns - 1])
                        cell.add_neighbor(self.__grid[0][0])
                        cell.add_neighbor(self.__grid[0][1])
                        cell.add_neighbor(self.__grid[0][self.__columns - 1])
                    # 2. rest of the bottom row
                    elif column < (self.__columns - 1):
                        #print('lower')
                        cell.add_neighbor(self.__grid[row][column - 1])
                        cell.add_neighbor(self.__grid[row][column + 1])
                        cell.add_neighbor(self.__grid[row - 1][column - 1])
                        cell.add_neighbor(self.__grid[row - 1][column])
                        cell.add_neighbor(self.__grid[row - 1][column + 1])
                        cell.add_neighbor(self.__grid[0][column - 1])
                        cell.add_neighbor(self.__grid[0][column])
                        cell.add_neighbor(self.__grid[0][column + 1])
                    # lower right corner (3 neighbors)
                    else:
                        #print('lower right')
                        cell.add_neighbor(self.__grid[row][column - 1])
                        cell.add_neighbor(self.__grid[row - 1][column - 1])
                        cell.add_neighbor(self.__grid[row - 1][column])

    def set_cell(self, row, column, living):
        """
        Change the state of the cell at self.__grid[row][column] to the
         value of living
        :param row: this is the number for the row the cell is in
        :param column: this is the number for the column the cell is in
        :param living: this is a boolean. If its true, the cell will be alive. If this is false, the cell will be dead
        :return: None
        """
        self.__grid[row][column].set_living(living)

    def next_generation(self):
        """
        Changes the grid to the next generation after following the
        propagation rules.
        :return: None
        """
        newGrid = self.create_grid()
        for row in self.__grid:
            for cell in row:
                if cell.get_living() == True:
                    if cell.living_neighbors() in [2, 3]:
                        newGrid[cell.get_row()][cell.get_column()].set_living(True)
                else:
                    if cell.living_neighbors() == 3:
                        newGrid[cell.get_row()][cell.get_column()].set_living(True)
        self.__grid = newGrid
        self.create_neighbors()
        self.__generationsDone += 1