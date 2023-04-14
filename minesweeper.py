import random

def reveal_cell(grid, row, col):
    """Reveals the contents of the specified cell and any adjacent blank cells.
       Returns True if a mine was encountered, False otherwise.
    """
    if grid[row][col] == '*':
        return True  # mine encountered
    elif grid[row][col] == ' ':
        # Reveal the cell and any adjacent blank cells
        num_adjacent_mines = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                    if grid[i][j] == '*':
                        num_adjacent_mines += 1
        if num_adjacent_mines > 0:
            grid[row][col] = str(num_adjacent_mines)
        else:
            grid[row][col] = '.'
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                        if grid[i][j] == ' ':
                            if reveal_cell(grid, i, j):
                                return True  # mine encountered
    return False  # no mines encountered

def display_grid(grid):
    """Displays the grid to the player."""
    for row in grid:
        print(' '.join(row))

# Get the dimensions of the grid and the number of mines
while True:
    try:
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))
        mines = int(input("Enter the number of mines: "))
        if rows > 0 and columns > 0 and mines > 0:
            break
        elif rows == 0 and columns == 0 and mines == 0:
            exit()
            break
    except ValueError:
        pass

# Generate a random arrangement of mines and blank cells
grid = [[' ' for _ in range(columns)] for _ in range(rows)]
for _ in range(mines):
    while True:
        row = random.randint(0, rows-1)
        col = random.randint(0, columns-1)
        if grid[row][col] == ' ':
            grid[row][col] = '*'
            break

# Play the game
while True:
    display_grid(grid)
    while True:
        try:
            row = int(input("Enter the row of the cell to reveal: "))
            col = int(input("Enter the column of the cell to reveal: "))
            if row >= 0 and row < rows and col >= 0 and col < columns:
                break
        except ValueError:
            pass
    if reveal_cell(grid, row, col):
        display_grid(grid)
        print("You lost!")
        break
    if all(cell != ' ' for row in grid for cell in row):
        display_grid(grid)
        print("You won!")
        break