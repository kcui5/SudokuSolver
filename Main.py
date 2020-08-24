#Sudoku Solver - an algorithm designed to efficiently solve a sudoku board

class SudokuBoard:
    def __init__(self, values: "dict"):
        """Initialize the board by setting the values in each item of the sudoku"""
        #Create an empty 9x9 2D array, each array item is an empty list
        self.board = [[[] for _ in range(9)] for i in range(9)]

        if values:
            #If given values, populate the board with those values
            for item in values:
                digit = int(values[item])
                row = int(item[0])
                col = int(item[1])
                self.board[row][col] = digit
        else:
            #If not given values, ask for manual input or random generation
            validInput = False
            while not validInput:
                mORr = input("Enter 'M' for manual input or 'R' for a random board: ")
                if mORr == "M" or mORr == "R":
                    validInput = True
            if mORr == "M":
                for r in range(9):
                    for c in range(9):
                        num = input(f"Row {r + 1}, Column {c + 1}: ")
                        if num:
                            self.board[r][c].append(int(num))
                            num = None
            elif mORr == "R":
                pass
            else:
                print("Board could not be populated")

        print("Initialized Board:")
        self.printSudoku()

    def printSudoku(self):
        """Prints the entire sudoku"""
        for _ in range(9):
            print(self.board[_])
        return None

    def getRow(self, rowNum):
        #Returns rowNum-th row of the sudoku (numbered starting from 0)
        return self.board[rowNum]

    def getCol(self, colNum):
        #Returns colNum-th column of the sudoku (numbered starting from 0)
        col = []
        for y in range(9):
            col.append(self.board[y][colNum])
        return col

    def getGrid(self, gridNum):
        #Returns gridNum-th grid (3 by 3) of the sudoku numbered:
        #/1//2//3/
        #/4//5//6/
        #/7//8//9/
        startingRow = 3 * ((gridNum - 1) // 3)
        if gridNum == 1 or gridNum == 4 or gridNum == 7:
            startingCol = 0
        elif gridNum == 2 or gridNum == 5 or gridNum == 8:
            startingCol = 3
        else:
            startingCol = 6
        grid = []
        for i in range(3):
            row = self.board[startingRow + i][startingCol: startingCol + 3]
            grid.append(row)
        return grid

    def getGridNum(self, row, col):
        #Returns the grid number of the given row and column numbers
        #(To be used by getGrid())
        gridNum = 0
        if row < 3:
            if col < 3:
                gridNum = 1
            elif col < 6:
                gridNum = 2
            elif col < 9:
                gridNum = 3
        elif row < 6:
            if col < 3:
                gridNum = 4
            elif col < 6:
                gridNum = 5
            elif col < 9:
                gridNum = 6
        elif row < 9:
            if col < 3:
                gridNum = 7
            elif col < 6:
                gridNum = 8
            elif col < 9:
                gridNum = 9
        return gridNum

class Solver:
    def __init__(self, board):
        self.solvingBoard = board

    def findPossibleValues(self, row, col):
        #Finds a list of possible values for the entry at row, col
        possibles = []
        notPossibles = []
        rowList = self.solvingBoard.getRow(row)
        for innerRowItem in rowList:
            if type(innerRowItem) == int:
                if not innerRowItem in notPossibles:
                    notPossibles.append(innerRowItem)
        colList = self.solvingBoard.getCol(col)
        for innerColItem in colList:
            if type(innerColItem) == int:
                if not innerColItem in notPossibles:
                    notPossibles.append(innerColItem)
        gridNum = self.solvingBoard.getGridNum(row, col)
        gridList = self.solvingBoard.getGrid(gridNum)
        for gridRow in gridList:
            for gridItem in gridRow:
                if type(gridItem) == int:
                    if not gridItem in notPossibles:
                        notPossibles.append(gridItem)
        for i in range(1, 10):
            if not i in notPossibles:
                possibles.append(i)
        return possibles

    def solveBoardOnce(self):
        #Loops through the entire board once and attempts to solve each entry
        newChange = False
        for r in range(9):
            for c in range(9):
                if type(self.solvingBoard.board[r][c]) == list:
                    entry = self.findPossibleValues(r, c)
                    if len(entry) == 1:
                        self.solvingBoard.board[r][c] = entry[0]
                        newChange = True
        return newChange

    def solve(self):
        while self.solveBoardOnce():
            pass
        return self.solvingBoard

class Validator:
    def __init__(self, board):
        self.validatingBoard = board

    def validate(self):
        #Validate rows
        for i in range(9):
            try:
                rowNums = []
                for num in self.validatingBoard.getRow(i):
                    if num in range(1, 10) and not num in rowNums:
                        rowNums.append(num)
                    else:
                        return False
            except (TypeError):
                return False
        #Validate columns
        for i in range(9):
            try:
                colNums = []
                for num in self.validatingBoard.getCol(i):
                    if num in range(1, 10) and not num in colNums:
                        colNums.append(num)
                    else:
                        return False
            except (TypeError):
                return False
        #Validate grids
        for i in range(1, 10):
            grid = self.validatingBoard.getGrid(i)
            for row in grid:
                try:
                    gridNums = []
                    for num in row:
                        if num in range(1, 10) and not num in gridNums:
                            gridNums.append(num)
                        else:
                            return False
                except (TypeError):
                    return False
        return True

values = {}
#Update sudoku board values from text file if the text file has contents
with open("DifficultBoard.txt", "r") as boardFile:
    #Making values a dict variable is unecessary but I want the practice
    writtenBoard = boardFile.readlines()
    rowNum = 0
    colNum = 0
    for line in writtenBoard:
        line = line[:-1]
        for char in line:
            if not int(char) == 0:
                values.update({f"{rowNum}{colNum}": char})
            colNum += 1
        colNum = 0
        rowNum += 1

newBoard = SudokuBoard(values)
solvingBoard = Solver(newBoard)
solvedBoard = solvingBoard.solve()
print("Solved Board:")
solvedBoard.printSudoku()

validatedBoard = Validator(solvedBoard)
if validatedBoard.validate():
    print("The Sudoku has been solved!")
else:
    print("The Sudoku has not been solved!")