from world import World

class World_Torus(World):


    def create_neighbors(self):
        """
        Loop through the grid and assign the neighbors to each cell.
        :return: None
        """
        for row in self._grid:
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
                        cell.add_neighbor(self._grid[row][column + 1])
                        cell.add_neighbor(self._grid[row + 1][column])
                        cell.add_neighbor(self._grid[row + 1][column + 1])
                        cell.add_neighbor(self._grid[row][self._columns - 1])
                        cell.add_neighbor(self._grid[row + 1][self._columns - 1])
                        cell.add_neighbor(self._grid[self._rows - 1][column])
                        cell.add_neighbor(self._grid[self._rows - 1][column + 1])
                        cell.add_neighbor(self._grid[self._rows - 1][self._columns - 1])
                    # 2. rest of the top row
                    elif column < (self._columns - 1):
                        #print('upper')
                        cell.add_neighbor(self._grid[row][column - 1])
                        cell.add_neighbor(self._grid[row][column + 1])
                        cell.add_neighbor(self._grid[row + 1][column - 1])
                        cell.add_neighbor(self._grid[row + 1][column])
                        cell.add_neighbor(self._grid[row + 1][column + 1])
                        cell.add_neighbor(self._grid[self._rows - 1][column - 1])
                        cell.add_neighbor(self._grid[self._rows - 1][column])
                        cell.add_neighbor(self._grid[self._rows - 1][column + 1])
                    # upper right corner
                    else:
                        #print('upper right')
                        cell.add_neighbor(self._grid[row][column - 1])
                        cell.add_neighbor(self._grid[row + 1][column - 1])
                        cell.add_neighbor(self._grid[row + 1][column])
                        cell.add_neighbor(self._grid[0][0])
                        cell.add_neighbor(self._grid[1][0])
                        cell.add_neighbor(self._grid[self._rows - 1][self._columns - 1])
                        cell.add_neighbor(self._grid[self._rows - 1][self._columns - 2])
                        cell.add_neighbor(self._grid[0][self._columns - 1])
                # middle row
                elif row < (self._rows - 1):
                    #1. middle left
                    if column == 0:
                        #print('middle left')
                        cell.add_neighbor(self._grid[row - 1][column])
                        cell.add_neighbor(self._grid[row - 1][column + 1])
                        cell.add_neighbor(self._grid[row][column + 1])
                        cell.add_neighbor(self._grid[row + 1][column])
                        cell.add_neighbor(self._grid[row + 1][column + 1])
                        cell.add_neighbor(self._grid[row][self._columns - 1])
                        cell.add_neighbor(self._grid[row - 1][self._columns - 1])
                        cell.add_neighbor(self._grid[row + 1][self._columns - 1])
                    #2. the rest of the middle row (8 neighbors)
                    elif column < (self._columns - 1):
                        #print('middle')
                        cell.add_neighbor(self._grid[row - 1][column - 1])
                        cell.add_neighbor(self._grid[row - 1][column])
                        cell.add_neighbor(self._grid[row - 1][column + 1])
                        cell.add_neighbor(self._grid[row][column - 1])
                        cell.add_neighbor(self._grid[row][column + 1])
                        cell.add_neighbor(self._grid[row + 1][column - 1])
                        cell.add_neighbor(self._grid[row + 1][column])
                        cell.add_neighbor(self._grid[row + 1][column + 1])
                    #3. middle right
                    else:
                        #print('middle right')
                        cell.add_neighbor(self._grid[row - 1][column])
                        cell.add_neighbor(self._grid[row - 1][column - 1])
                        cell.add_neighbor(self._grid[row][column - 1])
                        cell.add_neighbor(self._grid[row + 1][column])
                        cell.add_neighbor(self._grid[row + 1][column - 1])
                        cell.add_neighbor(self._grid[row][0])
                        cell.add_neighbor(self._grid[row - 1][0])
                        cell.add_neighbor(self._grid[row + 1][0])
                # bottom row
                else:
                    # 1. lower left corner
                    if column == 0:
                        #print('lower left')
                        cell.add_neighbor(self._grid[row][column + 1])
                        cell.add_neighbor(self._grid[row - 1][column])
                        cell.add_neighbor(self._grid[row - 1][column + 1])
                        cell.add_neighbor(self._grid[self._rows - 2][self._columns - 1])
                        cell.add_neighbor(self._grid[self._rows - 1][self._columns - 1])
                        cell.add_neighbor(self._grid[0][0])
                        cell.add_neighbor(self._grid[0][1])
                        cell.add_neighbor(self._grid[0][self._columns - 1])
                    # 2. rest of the bottom row
                    elif column < (self._columns - 1):
                        #print('lower')
                        cell.add_neighbor(self._grid[row][column - 1])
                        cell.add_neighbor(self._grid[row][column + 1])
                        cell.add_neighbor(self._grid[row - 1][column - 1])
                        cell.add_neighbor(self._grid[row - 1][column])
                        cell.add_neighbor(self._grid[row - 1][column + 1])
                        cell.add_neighbor(self._grid[0][column - 1])
                        cell.add_neighbor(self._grid[0][column])
                        cell.add_neighbor(self._grid[0][column + 1])
                    # lower right corner
                    else:
                        #print('lower right')
                        cell.add_neighbor(self._grid[row][column - 1])
                        cell.add_neighbor(self._grid[row - 1][column - 1])
                        cell.add_neighbor(self._grid[row - 1][column])
                        cell.add_neighbor(self._grid[0][0])
                        cell.add_neighbor(self._grid[self._rows - 1][0])
                        cell.add_neighbor(self._grid[self._rows - 2][0])
                        cell.add_neighbor(self._grid[0][self._columns - 2])
                        cell.add_neighbor(self._grid[0][self._columns - 1])