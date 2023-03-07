# Grid Minesweeper
The code provided is a Python implementation of the classic Minesweeper game. It takes in a grid (in the form of a list of lists) where '#' represents a mine and '-' represents an empty space. The code iterates over each item in the grid and for each empty space, it counts the number of mines in its surrounding cells and replaces the empty space with the count.

## Usage
To use this code, simply copy and paste it into a Python environment and run it. The grid to be analyzed is provided as a variable named 'grid' in the code. You can modify this variable to analyze different grids. The output will be the modified grid with the counts replacing the empty spaces.

## Implementation
The code works by iterating over each item in the grid using nested for loops. For each empty space, it constructs a list of the surrounding cells and counts the number of mines in that list. Finally, it replaces the empty space with the count. The updated grid is then printed to the console.

## Contributions
Contributions to this code are welcome. If you find any bugs or have suggestions for improvement, please create a pull request.
