board = []
word = "MAS"
count = 0

# Read the input file and parse it into a 2D list
with open('input.txt', 'r') as f:
    board = [list(line.strip()) for line in f]

# Get the dimensions of the board
height = len(board)
width = len(board[0])

# Iterate through the board, skipping the edges
for row in range(1, height - 1):
    for col in range(1, width - 1):
        # Check if the current cell is 'A'
        if board[row][col] != 'A':
            continue

        # Check for both valid patterns around the current cell
        if (
            (board[row - 1][col - 1] == 'M' and board[row + 1][col + 1] == 'S')
            or (board[row - 1][col - 1] == 'S' and board[row + 1][col + 1] == 'M')
        ) and (
            (board[row - 1][col + 1] == 'M' and board[row + 1][col - 1] == 'S')
            or (board[row - 1][col + 1] == 'S' and board[row + 1][col - 1] == 'M')
        ):
            count += 1
            print(f"X-MAS pattern found at center ({row}, {col})")

print(f"Total count of X-MAS patterns found: {count}")