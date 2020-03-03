#Sudoku Solver

def setSudoku(sudoku):
    #Set the values in each item of the sudoku
    

    return sudoku

def printSudoku(sudoku):
    #Prints the sudoku

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
    for y in range(3 * (gridNum), 3 * (gridNum) + 3):
        for x in range(3 * (gridNum), 3 * (gridNum) + 3)
        
    return grid
    
sudoku = [None]*81