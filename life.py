"""
Programmer: Janna Schmidt
Program: Life
Start Date: 2/6/2020
Updated: 2/20/2020
"""

from cell import Cell
from world import World
from world_torus import World_Torus
import toolbox
import lifeTest
from time import sleep
import os

class Life(object):

    def __init__(self, rows = 5, columns = 5):
        self.__rows = rows
        self.__columns = columns
        self.__currentWorld = None
        self.__percentLiving = 33
        self.__waitTime = 0
        self.__pastWorlds = []
        self.main()

    def __str__(self):
        pass

    def set_rows(self, rows):
        self.__rows = rows

    def set_columns(self, columns):
        self.__columns = columns

    def set_waitTime(self, parameter):
        """
        Sets the number of seconds in between running each generation
        :param parameter: This is any additional information the user thought this procedure should know
        :return:
        """
        print("Changing simulation speed...")
        if toolbox.is_number(parameter):
            delay = float(parameter)
        else:
            prompt = 'Seconds of delay between generations?'
            delay = toolbox.get_number(prompt)
        self.__waitTime = delay
        self.__currentWorld.set_speed(delay)

    def change_living_odds(self, parameter):
        """
        Changes the odds of whether or not a cell will be alive in a new world.
        :param parameter: this is any extra information the user sent into this procedure
        :return: None
        """
        if toolbox.is_number(parameter) and 0 <= float(parameter) <= 100:
            fillrate = float(parameter)
        else:
            prompt = 'What percent of cells should be alive?'
            fillrate = toolbox.get_integer_between(0, 100, prompt)
        print('Changing Odds...')
        self.__percentLiving = fillrate
        self.create_world()

    def new_size(self, parameter):
        """
        Make a new world of a new size.
        :param parameter: this is any extra information the user sent into this procedure
        :return: None
        """
        if parameter and len(parameter) > 2:
            rows, columns = parameter.split('x', 2)
            if toolbox.is_integer(rows) and toolbox.is_integer(columns):
                print("Changing size...")
                self.__rows = int(rows)
                self.__columns = int(columns)
        else:
            print("Changing size...")
            prompt = 'How many rows of cells?'
            self.__rows = toolbox.get_integer_between(2, 40, prompt)
            prompt = 'How many cells in each row?'
            self.__columns = toolbox.get_integer_between(2, 120, prompt)
        self.create_world()

    def main(self):
        """
        Main event loop for the game.
        :return: None
        """
        print('='*77)
        print(f"{'Life':^77}")
        print('='*77)
        self.help()
        input()
        self.create_world()
        #
        # This command is just a place holder
        #
        command = 'Hello'
        while command != 'quit':
            if command == 'help':
                self.help()
            elif command == "create-world":
                self.create_world()
                print("Finished!")
            elif command == "new-size":
                self.new_size(parameter)
                print("Finished!")
            elif command == "advance-life":
                if parameter != None and toolbox.is_integer(parameter):
                    parameter = int(parameter)
                else:
                    parameter = 1
                self.advance_life(parameter)
                print("Finished!")
            elif command == "new-odds":
                self.change_living_odds(parameter)
                print("Finished!")
            elif command == "new-speed":
                self.set_waitTime(parameter)
                print("Finished!")
            elif command == "fast-forward":
                if parameter != None:
                    parameter = int(parameter)
                else:
                    parameter = toolbox.get_integer("How many generations do you want to skip past? ")
                print("Skipping generations", end = "")
                for times in range(0, parameter):
                    print(".", end = '')
                    self.advance_life()
                print("\n")
                print(self.__currentWorld)
                print("Finished!")
            elif command == "display-acorn":
                print("Displaying World...")
                self.display_acorn()
                print("Finished!")
            elif command == "display-l":
                print("Displaying World...")
                self.long_l_world()
                print("Finished!")
            elif command == 'change-design':
                print("Changing display...")
                self.change_display(parameter)
                print("Finished!")
            elif command == 'save-world':
                print("Saving world...")
                self.save_world()
            elif command == 'load-world':
                print("Loading World...")
                self.load_world(parameter)
                print("Finished!")

            if command == 'settings':
                self.show_settings_menu()
                command, parameter = self.get_setting_command()
            else:
                self.show_menu()
                command, parameter = self.get_command()

    def repetition_check(self):
        """
        Check to see if the simulation has stopped changing
        :return: a boolean
        """
        repetition = self.__currentWorld.repetition_check()
        return repetition

    def show_menu(self):
        """
        Displays the menu.
        :return: None
        """
        print('[H]elp   [C]reate World  [A]dvance Life  [F]ast-forward  [P] Save World  [#] Load world  [S]ettings  [Q]uit  Display: Aco[r]n    [L]ong L')

    def show_settings_menu(self):
        """
        Displays the menu for changing settings
        :return: None
        """
        print('[S]ize   [O]dds    [Q]uickness   [D]esign   ')

    def get_command(self):
        """
        Gets a valid command from the user.
        :return: the name of the chosen command and any extra information the prgram should know for running the command
        """

        commands = {'?': 'help',
                    'h': 'help',
                    'c': 'create-world',
                    'a': 'advance-life',
                    ' ': 'advance-life',
                    'f': 'fast-forward',
                    'r': 'display-acorn',
                    'l': 'display-l',
                    's': 'settings',
                    'p': 'save-world',
                    '#': 'load-world',
                    'q':'quit'}

        validCommands = commands.keys()

        userInput = '&'
        parameter = None
        while userInput[0].lower() not in validCommands:
            userInput = input(' ')
            if userInput == '':
                userInput = ' '
                parameter = 1
        command = commands[userInput[0].lower()]
        if len(userInput) > 1:
            parameter = userInput[1:].strip()
        return command, parameter

    def get_setting_command(self):
        """
        Gets a valid settings command from the user.
        :return: the name of the chosen command and any extra information the prgram should know for running the command
        """

        commands = {'?': 'help',
                    'h': 'help',
                    's': 'new-size',
                    'd': 'change-design',
                    'o': 'new-odds',
                    'q': 'new-speed'}

        validCommands = commands.keys()

        userInput = '&'
        parameter = None
        while userInput[0].lower() not in validCommands:
            userInput = input(' ')
            if userInput == '':
                userInput = ' '
                parameter = 1
        command = commands[userInput[0].lower()]
        if len(userInput) > 1:
            parameter = userInput[1:].strip()
        return command, parameter

    def help(self):
        """
        Shows the instructions.
        :return: None
        """
        #todo! Update
        print('-'*77)
        print("""This is a game that simulates the lives of a bunch of cells in one world. Xs 
are living cells and dots are dead cells. The rules of the game are  simple, 
if a  live cell has two or three living neighbors, it stays alive. Otherwise 
it dies. If a dead cell has 3 living neighbors, it will come alive.""")
        print('-'*77)
        print("""If you would like to see the instructions again later, simply enter h or ?
when asked for a command. To make a new world, enter c. To see 1 more 
generation, hit enter once. To see many generations at once, enter a. If you
want to change the way new worlds are sized, enter s. If you  want to change
the odds of a cell being alive in a new world, enter o. To stop this program, 
enter q.

Press enter to continue""")
        print('-' * 77)

    def create_world(self):
        """
        Create a random world using the current size.
        :return: None
        """
        print("Creating World...")
        w1 = World_Torus(self.__rows, self.__columns, self.__waitTime)
        w1.random_fill(self.__percentLiving)
        self.__currentWorld = w1
        print(w1)

    def advance_life(self, parameter):
        """
        Goes through a certain number of generations in the current world
        :param parameter: This is the number of generations that the simulation should go through
        :return: None
        """
        if self.__currentWorld != None:
            print("Advancing Time...")
            for times in range(0, parameter):
                self.__currentWorld.next_generation()
                print(self.__currentWorld)
                if self.repetition_check():
                    print("The world has reached a steady state.")
                    print("Ending simulation")
                    break
                sleep(self.__waitTime)
        else:
            print('You have to make a world to run the next generation.')

    def change_display(self, parameter):
        """
        Change the live and dead characters for the cells.
        :param parameter: This is any extra information that the user sent into this command
        :return: None
        """
        if toolbox.is_integer(parameter) and \
                1 <= int(parameter) <= (len(Cell.displaySets.keys()) + 1):
            setNumber = int(parameter)
            for number, set in enumerate(Cell.displaySets):
                pass
            numberOfSets = number + 2
        else:
            print('**************************************')
            for number, set in enumerate(Cell.displaySets):
                liveChar = Cell.displaySets[set]['liveChar']
                deadChar = Cell.displaySets[set]['deadChar']
                print(f'{number + 1}: living cells: {liveChar} dead cells: {deadChar}')
            print(f'{number + 2}: Choose your own set')
            print('**************************************')
            prompt = 'What character set would you like to use?'
            setNumber = toolbox.get_integer_between(1, number + 2, prompt)
            numberOfSets = number + 2

        if setNumber == (numberOfSets):
            #
            #todo doesnt work with unicode characters
            #
            liveChar = input("What would you like the live cells to look like? ")
            while liveChar == None:
                print("The living cells cannot be nothing")
                liveChar = input("What would you like the live cells to look like? ")
            deadChar = input("What would you like the dead cells to look like? ")
            while deadChar == None:
                print("The dead cells cannot be nothing")
                deadChar = input("What would you like the dead cells to look like? ")
            Cell.set_display('choice', liveChar, deadChar)
        else:
            setString = list(Cell.displaySets.keys())[setNumber - 1]
            Cell.set_display(setString)
        print(self.__currentWorld)

    def display_acorn(self):
        """
        Create a blank world and put this pattern in the middle:
         .........
         ..x......
         ....x....
         .xx..xxx.
         .........
        :return: None
        """
        #todo this and l will not work right with too small o world
        if self.__rows < 8:
            self.__rows = 8
        if self.__columns < 11:
            self.__columns = 11
        rows = self.__rows
        columns = self.__rows
        self.__currentWorld = World(rows, columns, self.__waitTime)

        middleRow = int(rows / 2)
        middleColumn = int(columns / 2)

        self.__currentWorld.set_cell(middleRow - 1, middleColumn - 2, True)
        self.__currentWorld.set_cell(middleRow - 0, middleColumn - 0, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn - 3, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn - 2, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn + 1, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn + 2, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn + 3, True)
        print(self.__currentWorld)

    def long_l_world(self):
        """
        Create a blank world and put this pattern in the middle:
        ....
        .x..
        .x..
        .x..
        .xx.
        ....
        :return: None
        """
        if self.__rows < 7:
            self.__rows = 7
        if self.__rows < 6:
            self.__columns = 6
        rows = self.__rows
        columns = self.__rows
        self.__currentWorld = World(rows, columns, self.__waitTime)

        middleRow = int(rows / 2)
        middleColumn = int(columns / 2)

        self.__currentWorld.set_cell(middleRow - 2, middleColumn, True)
        self.__currentWorld.set_cell(middleRow - 1, middleColumn, True)
        self.__currentWorld.set_cell(middleRow - 0, middleColumn, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn, True)
        self.__currentWorld.set_cell(middleRow + 1, middleColumn + 1, True)
        print(self.__currentWorld)

    def save_world(self):
        """
        Saves a world into a file.
        :return: None
        """
        #todo send in parameters and check userinput for filename legality (somewhere else)
        #todo send these into a worlds folder
        #todo set display back to what the user had after this
        myPath = 'worlds'
        self.change_display(1)
        filename = input('What would you like to call the file you save this world in? ')
        filename += '.txt.lifeWorlds'
        filename = os.path.join(myPath, filename)
        with open(filename, 'w') as outputFile:
            print("Writing file...")
            for row in self.__currentWorld.get_grid():
                for cell in row:
                    outputFile.write(cell.__str__())
                outputFile.write(f'\n')
        self.__pastWorlds.append(filename)
        print("Done saving", filename)

    def load_world(self, fileNumber):
        """
        Opens a world previously saved in this program.
        :param fileNumber: this is the number of the file the user wants to open
        :return: None
        """
        #
        #todo there a re probabaly better ways to do this
        #
        numberOfFiles = 0
        allFiles = os.listdir('worlds')
        for file in allFiles:
            numberOfFiles += 1

        if toolbox.is_integer(fileNumber):
            fileNumber = int(fileNumber)
            if 0 < fileNumber <= numberOfFiles:
                print("This file does not exist")
                print("selecting default file...")
                print()
                fileNumber = 1
        else:
            counter = 1
            for file in allFiles:
                print(counter, file)
                counter +=1

            fileNumber = toolbox.get_integer("Which file would you like to open? ")

            while fileNumber > numberOfFiles:
                print(f"File number must be between 1 and {numberOfFiles}")
                fileNumber = toolbox.get_integer("Which file would you like to open? ")

        filename = allFiles[fileNumber - 1]

        filename = os.path.join('worlds', filename)

        #
        # Finds the old worlds size for consistency
        #
        rows = 0
        columns = 0
        with open(filename, 'r') as oldFile:
            for row in oldFile:
                columns = 0
                rows += 1
                for cell in row:
                    columns += 1

        columns -= 1
        self.__currentWorld = World(rows, columns, self.__waitTime)

        columnNumber = 0
        rowNumber = 0
        with open(filename, 'r') as oldFile:
            for row in oldFile:
                for cell in row:
                    if cell == 'O':
                        self.__currentWorld.set_cell(rowNumber, columnNumber, True)
                    columnNumber += 1
                rowNumber += 1
                columnNumber = 0

        print("Here is the old world")
        print(self.__currentWorld)

if __name__ == "__main__":
    #lifeTest.test1()
    #lifeTest.test2()
    #lifeTest.test3()
    #lifeTest.test4()
    #lifeTest.test5()

    life = Life()
