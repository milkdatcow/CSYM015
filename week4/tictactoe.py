def print_board(board):
    """Print the tic-tac-toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    """Check if the given player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    """Check if the board is full (draw)."""
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    """Return a list of empty cell coordinates."""
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    """Minimax algorithm to determine the best move for AI (O)."""
    if is_winner(board, "X"):
        return -1  # Human win
    if is_winner(board, "O"):
        return 1   # AI win
    if is_board_full(board):
        return 0   # Draw

    if is_maximizing:  # AI's turn (O)
        best_score = -float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "  # Undo move
            best_score = max(best_score, score)
        return best_score
    else:  # Human's turn (X)
        best_score = float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "  # Undo move
            best_score = min(best_score, score)
        return best_score

def ai_move(board):
    """AI chooses the best move using minimax."""
    best_score = -float("inf")
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = "O"

def play_game():
    """Main game loop."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print("Enter row (0-2) and column (0-2) separated by a space (e.g., '1 1').")

    while True:
        # Human turn (X)
        print_board(board)
        while True:
            try:
                row, col = map(int, input("Your move (row col): ").split())
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Invalid input! Use format 'row col' (e.g., '1 1').")

        # Check for win or draw
        if is_winner(board, "X"):
            print_board(board)
            print("You win!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI turn (O)
        ai_move(board)
        print("AI moved:")
        if is_winner(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()