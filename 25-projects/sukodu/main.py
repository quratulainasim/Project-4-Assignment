import streamlit as st
import numpy as np

def print_grid(grid):
    """
    Displays the Sudoku grid in a readable format using Streamlit.
    """
    styled_grid = ""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            styled_grid += "- - - - - - - - - - - - \n"
        for j in range(9):
            if j % 3 == 0 and j != 0:
                styled_grid += "| "
            styled_grid += str(grid[i][j]) + " "
        styled_grid += "\n"
    st.text(styled_grid)

def find_empty(grid):
    """
    Finds an empty cell in the grid.
    Returns (row, col) if an empty cell is found, otherwise None.
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid(grid, num, pos):
    """
    Checks if the number can be placed in the given position.
    """
    row, col = pos
    

    if num in grid[row]:
        return False
    

    if num in [grid[i][col] for i in range(9)]:
        return False
    

    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False
    
    return True

def solve(grid):
    """
    Solves the Sudoku puzzle using backtracking.
    Returns True if solved, False otherwise.
    """
    empty = find_empty(grid)
    if not empty:
        return True
    
    row, col = empty
    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0  
    
    return False

def main():
    st.title("Sudoku Solver")
    st.write("Enter your Sudoku puzzle below (use 0 for empty cells).")
  
    user_grid = []
    for i in range(9):
        row_input = st.text_input(f"Row {i+1}", "".join(map(str, [0]*9)))
        if len(row_input) == 9 and row_input.isdigit():
            user_grid.append([int(x) for x in row_input])
        else:
            st.warning("Each row must contain exactly 9 digits (0-9).")
            return
    
    grid = np.array(user_grid)
    
    
    st.write("Your Sudoku Puzzle:")
    print_grid(grid)
    
    if st.button("Solve Sudoku"):
        if solve(grid):
            st.success("Sudoku Solved Successfully!")
            st.write("Solution:")
            print_grid(grid)
        else:
            st.error("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()