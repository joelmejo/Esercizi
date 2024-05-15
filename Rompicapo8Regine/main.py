# Considerazioni
# la regina si muove in diagonale, verticale e orizzontale
# * ^ ^ ^ * ^ ^ ^ *
# ^ * ^ ^ * ^ ^ * ^
# ^ ^ * ^ * ^ * ^ ^
# ^ ^ ^ * * * ^ ^ ^
# * * * * Q * * * *
# ^ ^ ^ * * * ^ ^ ^
# ^ ^ * ^ * ^ * ^ ^
# ^ * ^ ^ * ^ ^ * ^
# * ^ ^ ^ * ^ ^ ^ *

# quindi si può dedurre che una volta posizionata una donna, non si possono più posizionare altre donne
#   sulla stessa riga, colonna e diagonali

# quindi si potrebbe creare una lista che contiene tutte le posizioni gia escluse cosi da non ricontrollarle ogni volta

chess_board = [[0 for column in range(8)] for row in range(8)]

results: list= []

def diagonal(row, column):
    # diagonale destra basso
    for i in range(len(chess_board[row]) - row):
        for j in range(len(chess_board[row]) - column):
            column += 1
            row += 1
            if chess_board[row][column] == 1:
                return False
            if column == 7 or row == 7:
                break
    # diagonale sinistra alto
    for i in range(abs(row - len(chess_board[row]))):
        for j in range(abs(column - len(chess_board[row]))):
            column -= 1
            row -= 1
            if chess_board[row][column] == 1:
                return False
            if column == 0 or row == 0:
                break
    # diagonale sinistra basso
    for i in range(len(chess_board[row]) - row):
        for j in range(abs(column - len(chess_board[row]))):
            column -= 1
            row += 1
            if chess_board[row][column] == 1:
                return False
            if column == 0 or row == 7:
                break
    # diagonale destra alto
    for i in range(abs(row - len(chess_board[row]))):
        for j in range(len(chess_board[row]) - column):
            column += 1
            row -= 1
            if chess_board[row][column] == 1:
                return False
            if column == 7 or row == 0:
                break
    

def position_queen(chess_board: list[list][int], positioned_queens: list):
    for row in range(8):
        for column in range(8):
            if 1 in chess_board[row]:
                break
            elif any(0 == chess_board[row][column] for row in range(8)) == False:
                break
            elif diagonal(row, column) == False:
                break
        

for row in range(8):
    position_queen(chess_board)
    