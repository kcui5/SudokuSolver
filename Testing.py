#File used to test code

board = [[[] for _ in range(9)] for i in range(9)]

print(board)
print(board[3])
print(board[3][3])

board[3][3].append(3)
print(board[3][3])
print(board[3])
print(board)