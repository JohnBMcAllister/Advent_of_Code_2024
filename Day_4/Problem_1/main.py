board = []
word = "XMAS"
count = 0

# Read the file and split each line into individual characters
with open('input.txt', 'r') as f:
    for line in f:
        board.append(list(line.strip()))

# Iterate through the board
for row in range(len(board)):
    for col in range(len(board[row])):
        if board[row][col] == word[0]:

            # UP
            if row > 0 and board[row - 1][col] == word[1]:
                i = 1
                current_row = row - 1
                while current_row >= 0 and board[current_row][col] == word[i]:
                    i += 1
                    current_row -= 1
                    if i == len(word):
                        count += 1
                        break

            # Left
            if col > 0 and board[row][col - 1] == word[1]:
                i = 1
                current_col = col - 1
                while current_col >= 0 and board[row][current_col] == word[i]:
                    i += 1
                    current_col -= 1
                    if i == len(word):
                        count += 1
                        break

            # Down
            if row < len(board) - 1 and board[row + 1][col] == word[1]:
                i = 1
                current_row = row + 1
                while current_row < len(board) and board[current_row][col] == word[i]:
                    i += 1
                    current_row += 1
                    if i == len(word):
                        count += 1
                        break

            # Right
            if col < len(board[row]) - 1 and board[row][col + 1] == word[1]:
                i = 1
                current_col = col + 1
                while current_col < len(board[row]) and board[row][current_col] == word[i]:
                    i += 1
                    current_col += 1
                    if i == len(word):
                        count += 1
                        break

            # Up Right
            if row > 0 and col < len(board[row]) - 1 and board[row - 1][col + 1] == word[1]:
                i = 1
                current_row = row - 1
                current_col = col + 1
                while current_col < len(board[row]) and current_row >= 0 and board[current_row][current_col] == word[i]:
                    i += 1
                    current_col += 1
                    current_row -= 1

                    if i == len(word):
                        count += 1
                        break

            # Up Left
            if row > 0 and col > 0 and board[row - 1][col - 1] == word[1]:
                i = 1
                current_row = row - 1
                current_col = col - 1
                while current_col >= 0 and current_row >= 0 and board[current_row][current_col] == word[i]:
                    i += 1
                    current_col -= 1
                    current_row -= 1

                    if i == len(word):
                        count += 1
                        break

            # Down Left
            if row < len(board) - 1 and col > 0 and board[row + 1][col - 1] == word[1]:
                i = 1
                current_row = row + 1
                current_col = col - 1
                while current_col >= 0 and current_row <= len(board) - 1 and board[current_row][current_col] == word[i]:
                    i += 1
                    current_col -= 1
                    current_row += 1

                    if i == len(word):
                        count += 1
                        break

            # Down Right
            if row < len(board) - 1 and col < len(board[row]) - 1 and board[row + 1][col + 1] == word[1]:
                i = 1
                current_row = row + 1
                current_col = col + 1
                while current_col <= len(board[row]) - 1 and current_row <= len(board) - 1 and board[current_row][current_col] == word[i]:
                    i += 1
                    current_col += 1
                    current_row += 1

                    if i == len(word):
                        count += 1
                        break

print(f"Total count of '{word}' found: {count}")