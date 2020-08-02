#Sudoku Solver - an algorithm designed to efficiently solve a sudoku board

class SudokuBoard:
    def __init__(self, values: "dict"):
        """Initialize the board by setting the values in each item of the sudoku"""
        #Create an empty 9x9 2D array, each array item is an empty list
        self.board = [[[] for _ in range(9)] for i in range(9)]

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
        startingCol = 0 if gridNum == 1 or gridNum == 4 or gridNum == 7 else None
        startingCol = 3 if gridNum == 2 or gridNum == 5 or gridNum == 8 else 6
        grid = []
        for i in range(3):
            row = self.board[startingRow + i][startingCol: startingCol + 3]
            grid.append(row)
        return grid
    
newBoard = SudokuBoard(values = {})
