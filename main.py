from random import randrange
"""
This script implements a command-line version of the Tic-Tac-Toe game.
The game is played between the player (O) and the computer (X).
The player and the computer take turns making moves on a 3x3 board.
The first player to get three of their marks in a row, column, or diagonal wins the game.
If all the cells on the board are filled and no player has won, the game is a draw.
Functions:
- display_board(board): Displays the current state of the board.
- enter_move(board): Allows the player to enter their move and updates the board accordingly.
- make_list_of_free_fields(board): Returns a list of coordinates of the free cells on the board.
- victory_for(board, sign): Checks if the specified player has won the game.
- draw_move(board): Makes a move for the computer and updates the board accordingly.
"""

def display_board(board):
    print('+-------+-------+-------+')
    for row in board:
        print('|       |       |       |')
        print('|', end="")
        for cell in row:
            print(f'   {cell}   |', end="")
        print()
        print('|       |       |       |')    
        print('+-------+-------+-------+')
        
def enter_move(board):
    is_valid_move = False

    while not is_valid_move:
        try:
            move = int(input('Enter your move: '))
        except ValueError:
            print('Invalid input')
            is_valid_move = False
            continue
            
        if not (1 <= move <= 9):
            print('Invalid input')
        else:
            # Calculate the row index from the move
            move_row = (move - 1) // 3
            # Calculate the column index from the move
            move_column = (move - 1) % 3
                 
            if board[move_row][move_column] not in ['X','O']:
                is_valid_move = True
                board[move_row][move_column] = 'O'
            else:
                print('Invalid move: Already used') 
                is_valid_move = False
                continue
                    
def make_list_of_free_fields(board):
    free_list = []
    for row_idx, row in enumerate(board):
        for col_idx, cell in enumerate(row):
            if cell not in ['X', 'O']:
                free_list.append((row_idx, col_idx))
    return free_list

def victory_for(board, sign):
    # Check rows for victory
    def check_rows(board, sign):
        for row in board:
            if all(cell == sign for cell in row):
                return True
        return False

    # Check columns for victory
    def check_columns(board, sign):
        for col in range(3):
            if all(board[row][col] == sign for row in range(3)):
                return True
        return False

    # Check diagonals for victory
    def check_diagonals(board, sign):
        if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
            return True
        return False

    # Check all conditions
    return check_rows(board, sign) or check_columns(board, sign) or check_diagonals(board, sign)
        
def draw_move(board):
    # Place 'X' in the center cell if it's not already occupied
    if board[1][1] != 'X':
        board[1][1] = 'X'
    else:
        is_valid_move = False
        # Loop until a valid move is found
        while not is_valid_move:
            # Generate a random move between 0 and 8
            move = randrange(9)
            
            # Calculate the row and column indices from the move
            move_row = move // 3
            move_column = move % 3
            
            # Check if the selected cell is free (not 'X' or 'O')
            if board[move_row][move_column] not in ['X', 'O']:
                is_valid_move = True
                # Place 'X' in the selected cell
                board[move_row][move_column] = 'X'
    

    
# Initialize the board as a 3x3 grid with numbers 1 to 9    
board = [[str(row * 3 + col + 1) for col in range(3)] for row in range(3)]

# Display the initial board
display_board(board)

# Flag to check if the game is a draw
is_draw = True

# Dictionary to track if a player has won
player_wins = {'X': False, 'O': False}

free_fields_count = len(make_list_of_free_fields(board))

# Main game loop: continue while there are free fields and no player has won
while free_fields_count > 0 and (not player_wins['O']) and (not player_wins['X']):        
    # Computer makes a move
    draw_move(board)

    # Display the updated board
    display_board(board)

    # Check if the computer has won
    player_wins['X'] = victory_for(board, 'X')

    free_fields_count = len(make_list_of_free_fields(board))
    
    # If there are still free fields and the computer hasn't won
    if free_fields_count > 0 and (not player_wins['X']):
        # Player makes a move
        enter_move(board)

        # Display the updated board
        display_board(board)

        # Check if the player has won
        player_wins['O'] = victory_for(board, 'O')

        free_fields_count = len(make_list_of_free_fields(board))

    # If either player has won, set the draw flag to False and break the loop
    if player_wins['X'] or player_wins['O']:
        is_draw = False
        break
        
if is_draw:
    print('is a draw')    
else:
    # If the computer has won
    if player_wins['X']:
        print('You Lose')
    else:
        print('You won!')