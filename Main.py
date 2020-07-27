#Sudoku Solver - an algorithm designed to efficiently solve a sudoku board

class SudokuBoard:
    def __init__(self, values: "dict"):
        """Initialize the board by setting the values in each item of the sudoku"""
        #Create an empty 9x9 2D array
        self.board = [None for _ in range(9)]
        row = [[] for _ in range(9)]
        self.board = [row for item in self.board]

        if values:
            #If given values, populate the board with those values
            pass
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

    def getRow(sudoku, rowNum):
        #Returns rowNum row of the sudoku
        row = sudoku[9 * rowNum: 9 * rowNum + 9]
        return row

    def getCol(sudoku, colNum):
        #Returns colNum column of the sudoku
        col = []
        for y in range(9):
            col.append(sudoku[9 * y + colNum])
        return col

    def getGrid(sudoku, gridNum):
        #Returns gridNum grid (3 by 3) of the sudoku
        #Next two lines are likely wrong ***
        grid = []
        for y in range(3 * (gridNum), 3 * (gridNum) + 3):
            for x in range(3 * (gridNum), 3 * (gridNum) + 3):
                pass
        return grid

newBoard = SudokuBoard(values = {})