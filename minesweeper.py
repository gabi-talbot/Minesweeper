grid = [['-', '-', '-', '#', '#'],
        ['-', '#', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '#', '#', '-', '-'],
        ['-', '-', '-', '-', '-']]

for count_row, row in enumerate(grid):
    for count_col, item in enumerate(row):
        # Initialise count and list - sets back to 0/empty on each iteration
        digit = 0
        check_list = []

        # If current position is '#' - skip
        if grid[count_row][count_col] == '#':
            continue

        # If current column is not the last - append East item
        if count_col < len(grid) - 1:
            check_list.append(grid[count_row][count_col + 1])
            # ... and if current row is not the last - append SE item
            if count_row < len(grid) - 1:
                check_list.append(grid[count_row + 1][count_col + 1])
            # ... and if current row is not the first - append NE item
            if 0 < count_row <= len(grid) - 1:
                check_list.append(grid[count_row - 1][count_col + 1])

        # If current column not the first - append West item
        if 0 < count_col <= len(grid) - 1:
            check_list.append(grid[count_row][count_col - 1])
            # ... and current row is not the last - append item SW
            if count_row < len(grid) - 1:
                check_list.append(grid[count_row + 1][count_col - 1])
            # ... and current row is not the first - append item NW
            if 0 < count_row <= len(grid) - 1:
                check_list.append(grid[count_row - 1][count_col - 1])

        # If current row between first and last - append both North and South
        if 0 < count_row < len(grid) - 1:
            check_list.append(grid[count_row + 1][count_col])
            check_list.append(grid[count_row - 1][count_col])
        # If this is the first row - just append South
        elif count_row == 0:
            check_list.append(grid[count_row + 1][count_col])
        # If this is the last row - just append North
        elif count_row == len(grid)-1:
            check_list.append(grid[count_row - 1][count_col])

        # Check for mines and update digit variable
        for char in check_list:
            if char == '#':
                digit += 1
        # Replace dash with digit
        grid[count_row][count_col] = digit

# Display altered grid
for row in grid:
    for column in row:
        print(column, end=" ")
    print()