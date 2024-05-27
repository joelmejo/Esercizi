# etermina se una tavola Sudoku 9 x 9 è valida. Solo le celle compilate devono essere convalidate secondo le seguenti regole:

#     Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
#     Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
#     Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere le cifre 1-9 senza ripetizione.

# Nota:

#     Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente risolvibile.
#     Solo le celle riempite devono essere convalidate secondo le regole menzionate.

def valid_sudoku(board: list[list[str]]) -> bool:
    # la tavola del sudo viene rapperentata come una matrice (lista di liste)
    # con 9 righe e 9 colonne
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] != '.':
                num = board[row][col]
                board[row][col] = '.'
                # check the row
                if num in board[row]:
                    return False
                # check the column
                if num in [board[i][col] for i in range(len(board))]:
                    return False
                # check the 3x3 box
                if col < 3:
                    start_col = 0
                elif col < 6:
                    start_col = 3
                else:
                    start_col = 6
                if row < 3:
                    start_row = 0
                elif row < 6:
                    start_row = 3
                else:
                    start_row = 6
                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        if board[i][j] == num:
                            return False
    return True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))