import random
import os

# Initialize constants
SIZE = 4  # Grid size (4x4)
EMPTY = 0  # Represents an empty cell

# Directions for moving tiles (up, down, left, right)
MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

# Function to initialize a new game board
def initialize_board():
    board = [[EMPTY] * SIZE for _ in range(SIZE)]
    spawn_tile(board)
    spawn_tile(board)
    return board

# Function to spawn a random tile (2 or 4) in an empty cell
def spawn_tile(board):
    empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == EMPTY]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = random.choice([2, 4])

# Function to compress the board (move tiles to the left)
def compress(board):
    new_board = []
    for row in board:
        # Remove all zeros and slide tiles to the left
        new_row = [tile for tile in row if tile != EMPTY]
        new_row += [EMPTY] * (SIZE - len(new_row))
        new_board.append(new_row)
    return new_board

# Function to merge the tiles in a row (leftward)
def merge(board):
    for r in range(SIZE):
        for c in range(SIZE - 1):
            if board[r][c] == board[r][c + 1] and board[r][c] != EMPTY:
                board[r][c] *= 2
                board[r][c + 1] = EMPTY
    return board

# Function to rotate the board 90 degrees (used for moving in all directions)
def rotate(board):
    return [list(row) for row in zip(*board[::-1])]

# Function to move the tiles
def move(board, direction):
    if direction == "left":
        board = compress(board)
        board = merge(board)
        board = compress(board)
    elif direction == "right":
        board = [row[::-1] for row in board]
        board = compress(board)
        board = merge(board)
        board = compress(board)
        board = [row[::-1] for row in board]
    elif direction == "up":
        board = rotate(board)
        board = compress(board)
        board = merge(board)
        board = compress(board)
        board = rotate(board)
        board = rotate(board)
        board = rotate(board)
    elif direction == "down":
        board = rotate(board)
        board = [row[::-1] for row in board]
        board = compress(board)
        board = merge(board)
        board = compress(board)
        board = [row[::-1] for row in board]
        board = rotate(board)
        board = rotate(board)
        board = rotate(board)
    return board

# Function to check if the player has won
def check_win(board):
    for row in board:
        if 2048 in row:
            return True
    return False

# Function to check if the game is over (no possible moves)
def check_game_over(board):
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == EMPTY:
                return False
            if r < SIZE - 1 and board[r][c] == board[r + 1][c]:
                return False
            if c < SIZE - 1 and board[r][c] == board[r][c + 1]:
                return False
    return True

# Function to print the board to the console
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for each update
    for row in board:
        print("\t".join(str(x) if x != 0 else "." for x in row))
    print("\n")

# Main game loop
def play_game():
    board = initialize_board()
    print_board(board)
    
    while True:
        if check_win(board):
            print("Congratulations! You've reached 2048!")
            break
        if check_game_over(board):
            print("Game Over! No more moves!")
            break
        
        move_input = input("Move (W = up, S = down, A = left, D = right): ").lower()
        if move_input in ["w", "s", "a", "d"]:
            direction = ""
            if move_input == "w":
                direction = "up"
            elif move_input == "s":
                direction = "down"
            elif move_input == "a":
                direction = "left"
            elif move_input == "d":
                direction = "right"
            
            board = move(board, direction)
            spawn_tile(board)
            print_board(board)
        else:
            print("Invalid input. Use W, A, S, or D.")

# Start the game
if __name__ == "__main__":
    play_game()
