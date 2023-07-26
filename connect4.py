from graphics import *

rows = 6
cols = 7
col_names = ['A','B','C','D','E','F','G']
board = [['','','','','',''],['','','','','',''],['','','','','',''],
         ['','','','','',''],['','','','','',''],['','','','','',''],
         ['','','','','','']]

def tokenDrop(player, column, board):
    column_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    col_idx = column_mapping.get(column, None)

    if col_idx is not None:
        if board[col_idx][5] == '':
            board[col_idx][5] = player
            return True
        else:
            for i in range(1, len(board[col_idx])):
                if board[col_idx][i] != '':
                    board[col_idx][i - 1] = player
                    return True

    return False

        
def game_over(board):
    global gui
    boardX = len(board)
    boardY = len(board[0])
    red_victory_msg = "🔴 Red Wins 🔴"
    yellow_victory_msg = "🟡 Yellow Wins 🟡"
    for x in range(boardX):
        for y in range(boardY - 3):
            #checks for vertical win condition
            if board[x][y] == '🔴' and board[x][y+1] == '🔴' and board[x][y+2] == '🔴' and board[x][y+3] == '🔴':
                gui.rectangle(0,0,960,80, "black")
                gui.text(355,10,"Red Wins!", "#d74f53",52)
                gui.rectangle(0,33,300,20, "#d74f53")
                gui.rectangle(660,33,300,20, "#d74f53")
                return True
            if board[x][y] == '🟡' and board[x][y+1] == '🟡' and board[x][y+2] == '🟡' and board[x][y+3] == '🟡':
                gui.rectangle(0,0,960,80, "black")
                gui.text(330,10,"Yellow Wins!", "#dbc646",52)
                gui.rectangle(0,33,300,20, "#dbc646")
                gui.rectangle(660,33,300,20, "#dbc646")
                return True
    for y in range(boardY):
        for x in range(boardX - 3):
            #checks for horizonal win condition
            if board[x][y] == '🔴' and board[x+1][y] == '🔴' and board[x+2][y] == '🔴' and board[x+3][y] == '🔴':
                gui.rectangle(0,0,960,80, "black")
                gui.text(355,10,"Red Wins!", "#d74f53",52)
                gui.rectangle(0,33,300,20, "#d74f53")
                gui.rectangle(660,33,300,20, "#d74f53")
                return True
            if board[x][y] == '🟡' and board[x+1][y] == '🟡' and board[x+2][y] == '🟡' and board[x+3][y] == '🟡':
                gui.rectangle(0,0,960,80, "black")
                gui.text(330,10,"Yellow Wins!", "#dbc646",52)
                gui.rectangle(0,33,300,20, "#dbc646")
                gui.rectangle(660,33,300,20, "#dbc646")
                return True
    for x in range(boardX - 3):
        for y in range(3, boardY):
            #checks for left to right upward diag win
            '''
              A   B   C   D   E   F   G  
            +---+---+---+---+---+---+---+
            |   |   |   | 0 |   |   |   | 0
            +---+---+---+---+---+---+---+
            |   |   | 0 | 0 |   |   |   | 1
            +---+---+---+---+---+---+---+
            |   | 0 | 0 | 0 |   |   |   | 2
            +---+---+---+---+---+---+---+
            | 0 | 0 | 0 |   |   |   |   | 3
            +---+---+---+---+---+---+---+
            | 0 | 0 |   |   |   |   |   | 4
            +---+---+---+---+---+---+---+
            | 0 |   |   |   |   |   |   | 5
            +---+---+---+---+---+---+---+
              0   1   2   3   4   5   6
            '''
            if board[x][y] == '🔴' and board[x+1][y-1] == '🔴' and board[x+2][y-2] == '🔴' and board[x+3][y-3] == '🔴':
                gui.rectangle(0,0,960,80, "black")
                gui.text(355,10,"Red Wins!", "#d74f53",52)
                gui.rectangle(0,33,300,20, "#d74f53")
                gui.rectangle(660,33,300,20, "#d74f53")
                return True
            if board[x][y] == '🟡' and board[x+1][y-1] == '🟡' and board[x+2][y-2] == '🟡' and board[x+3][y-3] == '🟡':
                gui.rectangle(0,0,960,80, "black")
                gui.text(330,10,"Yellow Wins!", "#dbc646",52)
                gui.rectangle(0,33,300,20, "#dbc646")
                gui.rectangle(660,33,300,20, "#dbc646")
                return True
    for x in range(boardX - 3):
        for y in range(boardY - 3):
            '''
              A   B   C   D   E   F   G  
            +---+---+---+---+---+---+---+
            | 0 |   |   |   |   |   |   | 0
            +---+---+---+---+---+---+---+
            | 0 | 0 |   |   |   |   |   | 1
            +---+---+---+---+---+---+---+
            | 0 | 0 | 0 |   |   |   |   | 2
            +---+---+---+---+---+---+---+
            |   | 0 | 0 | 0 |   |   |   | 3
            +---+---+---+---+---+---+---+
            |   |   | 0 | 0 |   |   |   | 4
            +---+---+---+---+---+---+---+
            |   |   |   | 0 |   |   |   | 5
            +---+---+---+---+---+---+---+
              0   1   2   3   4   5   6
            '''
            #checks for left to right downward diag win
            if board[x][y] == '🔴' and board[x+1][y+1] == '🔴' and board[x+2][y+2] == '🔴' and board[x+3][y+3] == '🔴':
                gui.rectangle(0,0,960,80, "black")
                gui.text(355,10,"Red Wins!", "#d74f53",52)
                gui.rectangle(0,33,300,20, "#d74f53")
                gui.rectangle(660,33,300,20, "#d74f53")
                return True
            if board[x][y] == '🟡' and board[x+1][y+1] == '🟡' and board[x+2][y+2] == '🟡' and board[x+3][y+3] == '🟡':
                gui.rectangle(0,0,960,80, "black")
                gui.text(330,10,"Yellow Wins!", "#dbc646",52)
                gui.rectangle(0,33,300,20, "#dbc646")
                gui.rectangle(660,33,300,20, "#dbc646")
                return True
    return False

def column_input():
    while True:  
        column = input("Enter a column (A-G):")
        if column.upper() in col_names:
            if board[col_names.index(column.upper())][0] == "":
                return column.upper()
            elif (board[col_names.index(column.upper())][0] != ""):
                print("That column is full - Pick another one")
        else:
            print("Invalid column input - try again:")

player = "🟡"

def column_click(gui,mousex,mousey):
    global player
    global board
    ranges = {'A': 120 * (0+1), 'B': 120 * (1+1), 'C': 120 * (2+1), 
              'D': 120 * (3+1), 'E': 120 * (4+1), 'F': 120 * (5+1), 'G': 120 * (6+1)}
    if game_over(board) == False:
        for k,v in ranges.items():
            if v - 50 < mousex < v + 50:
                if board[col_names.index(k)][0] == "":
                    tokenDrop(player,k,board)
                    drawboard(gui)
                    if player == "🟡":
                        player = "🔴"
                        gui.rectangle(0,0,960,80, "black")
                        gui.text(355,10,"Red's Turn", "#d74f53", 52)
                    else:
                        player = "🟡"
                        gui.rectangle(0,0,960,80, "black")
                        gui.text(330,10,"Yellow's Turn", "#dbc646",52)
    if game_over(board) == True:
        gui.rectangle(355,355,250,130, "#6c757d")
        gui.rectangle(360,360,240,120, "#5a6269")
        gui.text(385,377, "Click Here to \n  Play Again", "white", 32)
        gui.set_left_click_action(restartgame)
        
def restartgame(gui,mousex,mousey):
    if 360 <= mousex <= 600 and 360 <= mousey <= 480:
        global board
        gui.clear()
        board = [['','','','','',''],['','','','','',''],['','','','','',''],
            ['','','','','',''],['','','','','',''],['','','','','',''],
            ['','','','','','']]
        drawboard(gui)
        playerTurn = 0
        gui.set_left_click_action(column_click) #column_input()
        while not game_over(board):
            if playerTurn % 2 == 0:
                player = "🟡"
                column = column_input()
                print("🟡 Yellow Turn 🟡")
                tokenDrop(player,column,board)
                drawboard(gui)

            if playerTurn % 2 != 0:
                player = "🔴"
                print("🔴 Red Turn 🔴")
                column = column_input()
                tokenDrop(player,column,board)
                drawboard(gui)
            playerTurn += 1

def drawboard(gui):
    gui.rectangle(0, 80, 960, 880, "#3254ad")
    gui.rectangle(0,0,960,80, "black")
    gui.text(330,10,"Yellow's Turn", "#dbc646",52)
    for y in range(rows):
        for x in range(cols):
            if board[x][y] == '🔴':
                gui.ellipse(120 * (x+1), 80 + 107 * (y+1), 100, 100, "#d74f53")
            elif board[x][y] == '🟡':
                gui.ellipse(120 * (x+1), 80 + 107 * (y+1), 100, 100, "#dbc646")
            else:
                gui.ellipse(120 * (x+1), 80 + 107 * (y+1), 100, 100, "#ffffff")

gui = graphics(960, 960, 'connect4')
def initializeGameLoop():
    playerTurn = 0
    drawboard(gui)
    gui.set_left_click_action(column_click) #column_input()
    while not game_over(board):
        if playerTurn % 2 == 0:
            player = "🟡"
            column = column_input()
            print("🟡 Yellow Turn 🟡")
            tokenDrop(player,column,board)
            drawboard(gui)

        if playerTurn % 2 != 0:
            player = "🔴"
            print("🔴 Red Turn 🔴")
            column = column_input()
            tokenDrop(player,column,board)
            drawboard(gui)
        playerTurn += 1

    print("\nTurns taken: "+ str(playerTurn))

initializeGameLoop()

