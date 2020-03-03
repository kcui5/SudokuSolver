#File used to test code

col = []
for x in range(9):
    col.append("1")
print(col)


sudoku = [None] * 81

sudoku[42] = 52
print(sudoku[42])
print(sudoku[21])

if sudoku[2] == None:
    print("Nothing's here")