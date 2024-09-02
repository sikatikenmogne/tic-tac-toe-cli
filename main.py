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
        except:
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
    has_win_center = board[1][1] == sign
    if (not has_win_center):
        has_win = board[0][0] == board[0][1] == board[0][2] == sign or board[2][0] == board[2][1] == board[2][2] == sign or board[0][0] == board[0][1] == board[0][2]  == sign or board[0][2] == board[1][2] == board[2][2]  == sign    
    else:
        has_win = board[0][0] == board[1][1] == board[2][2] == sign or board[0][1] == board[1][1] == board[2][1]  == sign or board[0][2] == board[1][1] == board[2][0]  == sign or board[1][0] == board[1][1] == board[1][2]  == sign
            
    return has_win
        
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
computer_won = False
user_won = False

free_fields_count = len(make_list_of_free_fields(board))

while free_fields_count > 0:
    signs = ('X', 'O')
        
    draw_move(board)
    computer_won = victory_for(board, signs[0])
    free_fields_count = len(make_list_of_free_fields(board))
    
    if(free_fields_count > 0):
        enter_move(board)
        user_won = victory_for(board, signs[1])
        free_fields_count = len(make_list_of_free_fields(board))

    if computer_won or user_won:
        is_draw_game = False
        break
        
if not is_draw_game:
    if computer_won:
        print('You Lose')
    else:
        print('You won!')
else:
    print('is a draw')    
