import random

def print_board(board):
"""Prints the current Tic Tac Toe board."""
for row in board:
print(" | ".join(row))
print("-" * 5)

def check_winner(board, player):
"""Checks if a player has won."""
# Check rows, columns, and diagonals
for i in range(3):
if all([board[i][j] == player for j in range(3)]) or \
all([board[j][i] == player for j in range(3)]):
return True
if board[0][0] == player and board[1][1] == player and board[2][2] == player:
return True
if board[0][2] == player and board[1][1] == player and board[2][0] == player:
return True
return False

def is_draw(board):
"""Checks if the game is a draw."""
return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
"""Returns a list of available (empty) positions on the board."""
return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def computer_move(board):
"""Randomly picks an available move for the computer."""
available = get_available_moves(board)
return random.choice(available)

def tic_tac_toe():
"""Main function to play Tic Tac Toe with the computer."""
board = [[" " for _ in range(3)] for _ in range(3)]
print("🎮 You are 'X'. The computer is 'O'.")
print_board(board)

while True:  
    # Player's turn  
    move = input("Enter your move (row col): ")  
    try:  
        row, col = map(int, move.split())  
        if board[row][col] != " ":  
            print("❌ That cell is already taken. Try again.")  
            continue  
        board[row][col] = "X"  
        print_board(board)  

        if check_winner(board, "X"):  
            print("🎉 You win!")  
            break  
        if is_draw(board):  
            print("🤝 It's a draw!")  
            break  

        # Computer's turn  
        print("Computer's turn:")  
        row, col = computer_move(board)  
        board[row][col] = "O"  
        print_board(board)  

        if check_winner(board, "O"):  
            print("💻 Computer wins!")  
            break  
        if is_draw(board):  
            print("🤝 It's a draw!")  
            break  
    except (ValueError, IndexError):  
        print("⚠️ Invalid input. Please enter row and column as two numbers (0, 1, 2).")

tic_tac_toe()
