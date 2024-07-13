import pandas as pd
import random as rand

data_file = pd.read_csv("C:\\Users\\shokr\\Desktop\\Sudoku Models\\sudoku.csv")
grids_data = data_file["quizzes"]


def get_grid(grids_data):
    rand_number = rand.randint(0, 1000000)
    grid_data2 = grids_data[rand_number]

    string_grid = str(grid_data2)
    grid_list = []

    for num in string_grid:
        grid_list.append(int(num))

    grid = []
    index = 0

    for i in range(0, 9):
        list = []
        for j in range(0, 9):
            list.append(grid_list[index])
            index = index + 1

        grid.append(list)
    return grid


grid = get_grid(grids_data)


def Grid():
    return grid


def print_grid(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("----------------------------------------")
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(str(grid[i][j]) + "  ")
            else:
                print(str(grid[i][j]) + "   ", end="")


def find_empty_cells(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)  # row, col

    return None


def valid(grid, num, pos):
    # Check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(grid):
    find = find_empty_cells(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return True

            grid[row][col] = 0

    return False
