#My First App

# First of all we need a board to play the game
board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

# After creating the board, that's how it will be displayed
def display_board():
  print(board[0] + ' | ' + board[1] + ' | ' + board[2])
  print(board[3] + ' | ' + board[4] + ' | ' + board[5])
  print(board[6] + ' | ' + board[7] + ' | ' + board[8])


#Setting some useful variables
game_is_still_going = True
winner = None
current_player = 'X'


# We need a fucntion which will initialize the game
def play_game():
  display_board()
  while game_is_still_going:
    handle_turn(current_player)
    check_if_game_over()
    flip_player()
  if winner == 'X' or winner == 'O':
    print(winner + ' won.')
  elif winner == None:
    print("Tie.")
  

#Function to handle the turns of two players
def handle_turn(player):
  print(player + 's turn.')
  position = input('Chose from position 1-9: ')
  
  valid = False
  while not valid:
    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
      position = input('Chose from position 1-9: ')
    
    position = int(position)-1

    if board[position] == '-':
      valid = True
    else:
        print('You can\'t go there')

  board[position]= player
  display_board()


#Either the game is running or its a time to decide resulls
def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_if_tie():
  global game_is_still_going
  if '-' not in board:
    game_is_still_going = False
  return


#CHecking for the winner
def check_for_winner():
  global winner
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return



def check_rows():
  global game_is_still_going
  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"

  if row1 or row2 or row3:
    game_is_still_going = False
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]
  return


def check_columns():
  global game_is_still_going
  column1 = board[0] == board[3] == board[6] != "-"
  column2 = board[1] == board[4] == board[7] != "-"
  column3 = board[2] == board[5] == board[8] != "-"

  if column1 or column2 or column3:
    game_is_still_going = False
  if column1:
    return board[0]
  elif column2:
    return board[1]
  elif column3:
    return board[2]
  return


def check_diagonals():
  global game_is_still_going
  diagonal1 = board[0] == board[4] == board[8] != "-"
  diagonal2 = board[2] == board[4] == board[6] != "-"

  if diagonal1 or diagonal2:
    game_is_still_going = False
  if diagonal1:
    return board[0]
  elif diagonal2:
    return board[2]
  return


#Assigning X and O to the players
def flip_player():
  global current_player
  if current_player == 'X':
    current_player = 'O'
  elif current_player == 'O':
    current_player = 'X' 
  return

#Let's play
play_game()