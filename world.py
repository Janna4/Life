"""
Programmer: Janna Schmidt
Start Date: 2/3/2020
Updated: 2/20/2020
"""

from cell import Cell
import random
import toolbox

class World(object):

    rules = {'Default Rules': {'liveNeeds': '23', 'birthNeeds': '3'},
             'Loner': {'liveNeeds': '0', 'birthNeeds': '3'},
             'Perma Death': {'liveNeeds': '23', 'birthNeeds': '9'},
             'diamond': {'liveNeeds': '0', 'birthNeeds': '23'}}


    rule = 'Default Rules'

    liveNeeds = rules[rule]['liveNeeds']
    birthNeeds = rules[rule]['birthNeeds']



    @classmethod
    def set_rules(cls, rules, liveNeeds = None, birthNeeds = None):
        """
        Changes the way next generation works
        :param rules: this is a string holding the new rules
        :return: None
        """
        legalValues = cls.rules.keys()
        if rules in legalValues:
            cls.rule = rules
            cls.liveNeeds = cls.rules[rules]['liveNeeds']
            cls.birthNeeds = cls.rules[rules]['birthNeeds']
        elif rules == "choice":
            cls.rule = None
            cls.liveNeeds = str(liveNeeds)
            cls.birthNeeds = str(birthNeeds)
        else:
            raise ValueError(f'DisplaySet must be in {legalValues}.')

    def __init__(self, rows, columns, speed):
        self._rows = rows
        self._columns = columns
        self._gridA = self.create_grid()
        self._gridB = None
        self._gridC = None
        self._gridD = None
        self._generationsDone = 1
        self._speed = speed
        self._rules = '23-3'
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
        for row in self._gridA:
            for cell in row:
                string += cell.__str__()
            string += '\n'
        dimensions = f'{self._rows} by {self._columns}'
        percentAlive = self.find_living()
        liveNeeds = ''
        birthNeeds = ''
        #
        # Puts the rules into a more readable format
        #
        rules = self._rules.split('-')
        for number in rules[0]:
            liveNeeds += number
            if number != rules[0][-1]:
                liveNeeds += ' or '
        for number in rules[1]:
            birthNeeds += number
            if number != rules[1][-1]:
                birthNeeds += ' or '
        string += (f'''\nDimensions: {dimensions}    Percent Living: {percentAlive}   Generation #: {self._generationsDone}   Geometry: Dish    
Speed: 1 gen every {self._speed} seconds    Rules: Cells live with {liveNeeds} neighbors and cells are born with {birthNeeds} neighbors''')
        return string

    def get_rows(self):
        return self._rows

    def get_columns(self):
        return self._columns

    def get_grid(self):
        return self._gridA

    def get_pastGrid(self):
        return self._gridB

    def set_speed(self, seconds):
        self._speed = seconds

    def find_living(self):
        """
        Returns a string showing the percent of living cells
        :return: the percent of cells living
        """
        amountAlive = 0
        numberOfCells = self._columns * self._rows

        for row in self._gridA:
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
        for row in self._gridA:
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
        for rowNumber in range(self._rows):
            row = []
            for columnNumber in range(self._columns):
                row.append(Cell(rowNumber, columnNumber))
            grid.append(row)
        return grid

    def create_neighbors(self):
        """
        Loop through the grid and assign the neighbors to each cell.
        :return: None
        """
        for row in self._gridA:
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
                # 9. lower right corner
                #
                row = cell.get_row()
                column = cell.get_column()
                #print(f'({row},{column})')
                # top row
                if row == 0:
                    # 1. upper left corner
                    if column == 0:
                        #print('upper left')
                        cell.add_neighbor(self._gridA[row][column + 1])
                        cell.add_neighbor(self._gridA[row + 1][column])
                        cell.add_neighbor(self._gridA[row + 1][column + 1])
                    # 2. rest of the top row
                    elif column < (self._columns - 1):
                        #print('upper')
                        cell.add_neighbor(self._gridA[row][column - 1])
                        cell.add_neighbor(self._gridA[row][column + 1])
                        cell.add_neighbor(self._gridA[row + 1][column - 1])
                        cell.add_neighbor(self._gridA[row + 1][column])
                        cell.add_neighbor(self._gridA[row + 1][column + 1])
                    # upper right corner
                    else:
                        #print('upper right')
                        cell.add_neighbor(self._gridA[row][column - 1])
                        cell.add_neighbor(self._gridA[row + 1][column - 1])
                        cell.add_neighbor(self._gridA[row + 1][column])
                # middle row
                elif row < (self._rows - 1):
                    #1. middle left
                    if column == 0:
                        #print('middle left')
                        cell.add_neighbor(self._gridA[row - 1][column])
                        cell.add_neighbor(self._gridA[row - 1][column + 1])
                        cell.add_neighbor(self._gridA[row][column + 1])
                        cell.add_neighbor(self._gridA[row + 1][column])
                        cell.add_neighbor(self._gridA[row + 1][column + 1])
                    #2. the rest of the middle row (8 neighbors)
                    elif column < (self._columns - 1):
                        #print('middle')
                        cell.add_neighbor(self._gridA[row - 1][column - 1])
                        cell.add_neighbor(self._gridA[row - 1][column])
                        cell.add_neighbor(self._gridA[row - 1][column + 1])
                        cell.add_neighbor(self._gridA[row][column - 1])
                        cell.add_neighbor(self._gridA[row][column + 1])
                        cell.add_neighbor(self._gridA[row + 1][column - 1])
                        cell.add_neighbor(self._gridA[row + 1][column])
                        cell.add_neighbor(self._gridA[row + 1][column + 1])
                    #3. middle right
                    else:
                        #print('middle right')
                        cell.add_neighbor(self._gridA[row - 1][column])
                        cell.add_neighbor(self._gridA[row - 1][column - 1])
                        cell.add_neighbor(self._gridA[row][column - 1])
                        cell.add_neighbor(self._gridA[row + 1][column])
                        cell.add_neighbor(self._gridA[row + 1][column - 1])
                # bottom row
                else:
                    # 1. lower left corner
                    if column == 0:
                        #print('lower left')
                        cell.add_neighbor(self._gridA[row][column + 1])
                        cell.add_neighbor(self._gridA[row - 1][column])
                        cell.add_neighbor(self._gridA[row - 1][column + 1])
                    # 2. rest of the bottom row
                    elif column < (self._columns - 1):
                        #print('lower')
                        cell.add_neighbor(self._gridA[row][column - 1])
                        cell.add_neighbor(self._gridA[row][column + 1])
                        cell.add_neighbor(self._gridA[row - 1][column - 1])
                        cell.add_neighbor(self._gridA[row - 1][column])
                        cell.add_neighbor(self._gridA[row - 1][column + 1])
                    # lower right corner
                    else:
                        #print('lower right')
                        cell.add_neighbor(self._gridA[row][column - 1])
                        cell.add_neighbor(self._gridA[row - 1][column - 1])
                        cell.add_neighbor(self._gridA[row - 1][column])

    def set_cell(self, row, column, living):
        """
        Change the state of the cell at self.__grid[row][column] to the
         value of living
        :param row: this is the number for the row the cell is in
        :param column: this is the number for the column the cell is in
        :param living: this is a boolean. If its true, the cell will be alive. If this is false, the cell will be dead
        :return: None
        """
        self._gridA[row][column].set_living(living)

    def next_generation(self):
        """
        Changes the grid to the next generation after following the
        propagation rules.
        :return: None
        """
        newGrid = self.create_grid()
        liveRules = ''
        for character in World.liveNeeds:
            liveRules += character
        comeAliveRules = ''
        for character in World.birthNeeds:
            comeAliveRules += character
        for row in self._gridA:
            for cell in row:
                if cell.get_living() == True:
                    if str(cell.living_neighbors()) in liveRules:
                        newGrid[cell.get_row()][cell.get_column()].set_living(True)
                else:
                    if str(cell.living_neighbors()) in comeAliveRules:
                        newGrid[cell.get_row()][cell.get_column()].set_living(True)
        self._gridD = self._gridC
        self._gridC = self._gridB
        self._gridB = self._gridA
        self._gridA = newGrid
        self.create_neighbors()
        self._generationsDone += 1

    def repetition_check(self):
        """
        Checks to see if the current grid has reached a steady state
        :return: a boolean
        """
        repetition = False
        if str(self._gridA) == str(self._gridB):
            repetition = True
        if str(self._gridA) == str(self._gridC):
            repetition = True
        if str(self._gridA) == str(self._gridD):
            repetition = True
        return repetition

    def rewind(self):
        """
        Cycles all the grids back 1 generation (and sets the farthest back generation to None)
        :return: None
        """
        self._gridA = self._gridB
        self._gridB = self._gridC
        self._gridC = self._gridD
        self._gridD = None