# Sudoku-Solver-with-AI-and-Python-and GUI


This project is a Sudoku solver and graphical user interface (GUI) built using Python and Pygame. The solver uses a backtracking algorithm to solve Sudoku puzzles, while the GUI allows users to interact with the puzzle and solve it step-by-step.

## Features

- Sudoku puzzle generation from a preloaded dataset.
- Interactive GUI to place numbers, clear cells, and solve the puzzle.
- Automatic validation of the puzzle state.
- Display of elapsed time and strike count for incorrect placements.

## Requirements

- Python 3.x
- Pygame
- Pandas


## Usage

Run the main script to start the Sudoku GUI:

bash
python GUI.py

## Code Overview

### GUI.py

This file contains the main code for the Sudoku solver and GUI.

#### Classes

- **Grid**: Manages the Sudoku grid, handles user interactions, and updates the display.
- **Cube**: Represents individual cells in the Sudoku grid.

#### Functions

- `redraw_window(win, board, time, strikes)`: Redraws the game window.
- `format_time(secs)`: Formats the elapsed time.
- `main()`: The main game loop, handling events and updating the game state.

### Solver.py

Contains the Sudoku solving algorithm and helper functions.

#### Functions

- `get_grid(grids_data)`: Selects a random Sudoku puzzle from the dataset.
- `print_grid(grid)`: Prints the grid to the console.
- `find_empty_cells(grid)`: Finds the next empty cell in the grid.
- `valid(grid, num, pos)`: Validates if a number can be placed in a given position.
- `solve(grid)`: Solves the Sudoku puzzle using backtracking.

## Controls

- **Number keys (1-9)**: Place a number in the selected cell.
- **Delete key**: Clear the selected cell.
- **Enter key**: Confirm placement of the temporary number in the selected cell.
- **Mouse click**: Select a cell.

## Example

To see the solver in action, simply run the `GUI.py` script. You will see a Sudoku puzzle, and you can interact with it using the controls described above. The puzzle will automatically validate and solve itself when possible.



## License

This project is licensed under the MIT License.

