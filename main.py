from random import randrange

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
            
        if not move >= 1 and move <= 9:
            print('Invalid input')
        else:
            move_row = (move - 1) // 3
            move_column = (move - 1) % 3
            
            if board[move_row][move_column] not in ['X','O']:
                is_valid_move = True
                board[move_row][move_column] = 'O'
            else:
                print('Invalid move: Already used') 
                is_valid_move = False
                continue
    display_board(board)
                    
def make_list_of_free_fields(board):
    free_list = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] not in ['X', 'O']:
                free_list.append((row, col))
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
    if board[1][1] != 'X':
        board[1][1] = 'X'
    else:
        is_valid_move = False
        while not is_valid_move:
            move = randrange(9)
            move_row = move // 3
            move_column = move % 3
            
            is_valid_move = True if board[move_row][move_column] not in ['X','O'] else False 
            
            if(is_valid_move):
                board[move_row][move_column] = 'X'
    
    display_board(board)
    
    
board = [[str(row * 3 + col + 1) for col in range(3)] for row in range(3)]

is_draw_game = True
player_wins = {'X': False, 'O': False}

free_fields_count = len(make_list_of_free_fields(board))

while free_fields_count > 0 and (not player_wins['O']) and (not player_wins['X']):        
    draw_move(board)
    player_wins['X'] = victory_for(board, 'X')
    free_fields_count = len(make_list_of_free_fields(board))
    
    if(free_fields_count > 0 and (not player_wins['X'])):
        enter_move(board)
        player_wins['O'] = victory_for(board, 'O')
        free_fields_count = len(make_list_of_free_fields(board))

    if player_wins['X'] or player_wins['O']:
        is_draw_game = False
        break
        
if is_draw_game:
    print('is a draw')    
else:
    if player_wins['X']:
        print('You Lose')
    else:
        print('You won!')
