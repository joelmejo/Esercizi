# Il rompicapo (o problema) delle otto regine è un problema che consiste nel trovare il modo di posizionare otto donne (pezzo degli scacchi) su una scacchiera 8×8 tali che nessuna di esse possa catturarne un'altra,
# usando i movimenti standard della regina. Perciò, una soluzione dovrà prevedere che nessuna regina abbia una colonna, traversa o diagonale in comune con un'altra regina.
# Il problema delle otto regine è un esempio del più generale problema delle n regine, che consiste nel piazzare, con le condizioni illustrate precedentemente, n regine su una scacchiera n × n; in questa forma,
# in particolare, esso viene spesso usato per illustrare tecniche di progettazione di algoritmi e di programmazione. È stato dimostrato matematicamente che il problema è risolvibile per n = 1 o n ≥ 4, mentre non lo è per n = 2 e n = 3.

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
queens_positioned: dict = {}
columns_in_use: dict = {}
rows_in_use: dict = {}
tried_positions: dict = {}

def check_diagonal(row, column):
    column_right = column
    column_left = column
    row_down = row
    row_up = row
    # diagonale principale
    # for i in range(max(len(chess_board[row]) - row, abs(row - len(chess_board[row])), len(chess_board[row]) - column, abs(column - len(chess_board[row])))):
    for i in range(8):
        column_right = column + 1
        column_left = column - 1
        row_down = row + 1
        row_up = row - 1
            # diagonale destra basso
        if column_right <= 7 and row_down <= 7:
            if chess_board[row_down][column_right] == 1:
                return False
        # diagonale sinistra alto
        if column_left >= 0 and row_up >= 0:
            if chess_board[row_up][column_left] == 1:
                return False
        # diagonale sinistra basso
        if column_left >= 0 and row_down <= 7:
            if chess_board[row_down][column_left] == 1:
                return False
        # diagonale destra alto
        if column_right <= 7 and row_up >= 0:
            if chess_board[row_up][column_right] == 1:
                return False
    return True

    # # diagonale destra basso
    # for i in range(len(chess_board[row] - row)):
    #     for j in range(len(chess_board[row]) - column):
    #         column += 1
    #         row += 1
    #         if chess_board[row][column] == 1:
    #             return False
    #         if column == 7 or row == 7:
    #             break
    # # diagonale sinistra alto
    # for i in range(abs(row - len(chess_board[row]))):
    #     for j in range(abs(column - len(chess_board[row]))):
    #         column -= 1
    #         row -= 1
    #         if chess_board[row][column] == 1:
    #             return False
    #         if column == 0 or row == 0:
    #             break
    # # diagonale sinistra basso
    # for i in range(len(chess_board[row]) - row):
    #     for j in range(abs(column - len(chess_board[row]))):
    #         column -= 1
    #         row += 1
    #         if chess_board[row][column] == 1:
    #             return False
    #         if column == 0 or row == 7:
    #             break
    # # diagonale destra alto
    # for i in range(abs(row - len(chess_board[row]))):
    #     for j in range(len(chess_board[row]) - column):
    #         column += 1
    #         row -= 1
    #         if chess_board[row][column] == 1:
    #             return False
    #         if column == 7 or row == 0:
    #             break

def check_row(row) -> bool:
    if 1 in chess_board[row]:
        return False
    return True

def check_column(column) -> bool:
    for i in range(8):
        if chess_board[i][column] == 1:
            return False
        else:
            return True

def possible_queen_position(row, column) -> bool:
    if check_row(row) and check_column(column) and check_diagonal(row, column):
        return True
    else:
        return False

def place_queen() -> bool:
    for row in range(8):
        if row in rows_in_use:
            continue
        for column in range(8):
                if column in columns_in_use:
                    continue
                if len(queens_positioned) - 1 in tried_positions:
                    if (row, column) in tried_positions[len(queens_positioned) - 1]:
                        continue
                if possible_queen_position(row, column):
                    chess_board[row][column] = 1
                    rows_in_use[row] = row
                    columns_in_use[column] = column
                    queens_positioned[len(queens_positioned)] = (row, column)
                    return True
    return False
    
while len(queens_positioned) < 8:
    if place_queen() == False:
        row, column = queens_positioned.pop(len(queens_positioned) - 1)
        if len(queens_positioned) - 1 in tried_positions:
            list = tried_positions[len(queens_positioned) - 1]
            list.append((row, column))
        else:
            tried_positions[len(queens_positioned) - 1] = [(row, column)]
        chess_board[row][column] = 0
        rows_in_use.pop(row)
        columns_in_use.pop(column)

for row in chess_board:
    print(row)
print(queens_positioned)