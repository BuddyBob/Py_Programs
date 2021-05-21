board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"
def checkAround(x,y):
    print(board[x,y])
    pass
row = 0
for rows in board:
    for letters in row:
        if letters == word[0]:
            checkAround(letters,row)

        letters += 1
    row += 1
