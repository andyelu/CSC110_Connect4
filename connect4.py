rows = 6
cols = 7
col_names = ['A','B','C','D','E','F','G']
board = [['','','','','',''],['','','','','',''],['','','','','',''],
         ['','','','','',''],['','','','','',''],['','','','','',''],
         ['','','','','','']]

def createBoard():
    print("   A   B   C   D   E   F   G  ", end = "")
    for x in range(rows):
        print("\n +---+---+---+---+---+---+---+")
        print(' |', end = '')
        for y in range(cols):
            if board[y][x] == 'R':
                print(' ' + board[y][x], end = ' |')
            elif board[y][x] == 'Y':
                print(' ' + board[y][x], end = ' |')
            else:
                print(' ' + board[y][x], end = '  |')
    print("\n +---+---+---+---+---+---+---+")

def tokenDrop(player,column,board):
    if column == 'A':
        for i in range(1,len(board[0])):
            #if there is item in spot, places token in next open spot
            if board[0][i] != '': 
                board[0].insert(i-1,player)
        #if last slot is empty aka column empty, token places on last slot
        if board[0][5] == '':
            board[0].insert(5,player)
        if board[0][0] != '':
            print('choose another column') 
            #add code here to make it so u can't place items in empty row
    if column == 'B':
        for i in range(1,len(board[1])):
            #if there is item in spot, places token in next open spot
            if board[1][i] != '': 
                board[1].insert(i-1,player)
        #if last slot is empty aka column empty, token places on last slot
        if board[1][5] == '':
            board[1].insert(5,player)
        if board[1][0] != '':
            print('choose another column') 
            #add code here to make it so u can't place items in empty row
    if column == 'C':
        for i in range(1,len(board[2])):
            #if there is item in spot, places token in next open spot
            if board[2][i] != '': 
                board[2].insert(i-1,player)
        #if last slot is empty aka column empty, token places on last slot
        if board[2][5] == '':
            board[2].insert(5,player)
        if board[2][0] != '':
            print('choose another column') 
            #add code here to make it so u can't place items in empty row
    if column == 'D':
        for i in range(1,len(board[3])):
            #if there is item in spot, places token in next open spot
            if board[3][i] != '': 
                board[3].insert(i-1,player)
        #if last slot is empty aka column empty, token places on last slot
        if board[3][5] == '':
            board[3].insert(5,player)
        if board[3][0] != '':
            print('choose another column') 
            #add code here to make it so u can't place items in empty row
    if column == 'E':
        for i in range(1,len(board[4])):
            #if there is item in spot, places token in next open spot
            if board[4][i] != '': 
                board[4].insert(i-1,player)
        #if last slot is empty aka column empty, token places on last slot
        if board[4][5] == '':
            board[4].insert(5,player)
        if board[4][0] != '':
            print('choose another column') 
            #add code here to make it so u can't place items in empty row
    if column == 'F':
        for i in range(1,len(board[5])):
            #if there is item in spot, places token in next open spot
            if board[5][i] != '': 
                board[5].insert(i-1,player)
        #if last slot is empty aka column empty, token places on last slot
        if board[5][5] == '':
            board[5].insert(5,player)
        if board[5][0] != '':
            print('choose another column') 
            #add code here to make it so u can't place items in empty row
    if column == 'G':
        for i in range(1,len(board[6])):
            #if there is item in spot, places token in next open spot
            if board[6][i] != '': 
                board[6].insert(i-1,player)
        #if last slot is empty aka column empty, token places on last slot
        if board[6][5] == '':
            board[6].insert(5,player)
        if board[6][0] != '':
            print('choose another column') 
            #add code here to make it so u can't place items in empty row

createBoard()
#+---+---+---+---+---+---+---+
#|---|---|---|---|---|---|---|
