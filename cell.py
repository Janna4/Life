"""
Programmer: Janna Schmidt
Start Date: 2/3/2020
Updated: 2/20/2020
"""

class Cell(object):

    displaySets = {'basic': {'liveChar': 'O', 'deadChar': '.'},
                   'squares': {'liveChar': '\u2B1B', 'deadChar': '\u2B1C'},
                   'soccer': {'liveChar': '\u26BD', 'deadChar': '\u2B1C'},
                   'at sign': {'liveChar': '@', 'deadChar': ' '},
                   'circles': {'liveChar': '\u26AB', 'deadChar': '\u26AA'} }

    displaySet = 'basic'

    liveChar = displaySets[displaySet]['liveChar']
    deadChar = displaySets[displaySet]['deadChar']

    @classmethod
    def set_display(cls, displaySet, liveChar = None, deadChar = None):
        """
        Sets the default way cells will appear
        :param displaySet: this is the name of the set the user wants to use
        :param liveChar: this is the living character the user wants to use if they are choosing their own characters
        :param deadChar: this is the dead character the user wants to use if they are choosing their own characters
        :return: None
        """
        legalValues = cls.displaySets.keys()
        if displaySet in legalValues:
            cls.displaySet = displaySet
            cls.liveChar = cls.displaySets[displaySet]['liveChar']
            cls.deadChar = cls.displaySets[displaySet]['deadChar']
        elif displaySet == 'choice':
            cls.displaySet = displaySet
            cls.liveChar = liveChar
            cls.deadChar = deadChar
        else:
            raise ValueError(f'DisplaySet must be in {legalValues}.')


    def __init__(self, row, column):
        """
        Given a row and a column, creates a cell that knows its row,
           column, living (all cells start off with living as False), and
           neighbors (all cells start off with an empty list for neighbors).
        :param row: this is the row number a cell starts in (the program counts from 0)
        :param column: this is the column number a cell starts in (the program counts from 0)
        """
        self.__row = row
        self.__column = column
        self.living = False
        self.__neighbors = []
        self.__style = 'default'


    def __str__(self):
        """
        Returns either the liveChar or the deadChar for the Cell class
           depending on the state of the cell.
        :return: the cells living character of the cells dead character
        """
        if self.__style == 'default':
            if self.living:
                return Cell.liveChar
            else:
                return Cell.deadChar

    def get_living(self):
        return self.living

    def set_living(self, state):
        """
        Sets whether the cell is alive or dead.
        :param state: this should be a boolean. If state is true, the cell is alive, if state is false, this cell is dead
        :return: a boolean
        """
        if isinstance(state, bool):
            self.living = state
        else:
            raise TypeError('state must be boolean.')

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column

    def add_neighbor(self, cell):
        """
        Adds a neighbor to this cells list of neighbors
        :param cell: this is a different cell
        :return: None
        """
        self.__neighbors.append(cell)

    def living_neighbors(self):
        """
        Finds the number of living neighbors a cell has
        :return: the number of live neighbors
        """
        neighborCount = 0
        for neighbor in self.__neighbors:
            if neighbor.get_living() == True:
                neighborCount += 1
        return neighborCount

    def __repr__(self):
        #
        # Here's a handy way to use if..else that we haven't talked about.
        #
        state = 'alive' if self.living else 'dead'
        return f'Cell({self.__row},{self.__column}) [{state}]'

    def debug(self):
        """
        This out some extra information about a cell
        :return: None
        """
        neighbors = len(self.__neighbors)
        string = self.__repr__() + f' neighbors: {self.living_neighbors()}/{neighbors}'
        for neighbor in self.__neighbors:
            string += '\n     ' + neighbor.__repr__()
        print(string)