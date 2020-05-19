# SudokuSolver
Sudoku Solver in Python3 (console based)

# How it works?
 The program uses [Backtracking Algorithm](https://en.wikipedia.org/wiki/Backtracking)
* The process is the following:
   * Checks for the empty fields on the board
   * Gets empty field indicies and the index of the containing box.
   * Tries values from 1-9 to the given indices
   * Checking 3 positional statements if they contain the desired value:
     * BOX
     * ROW
     * COLUMN
   * If it fits to the given idices it places it in our board. Otherwise it replaces the elements of the last box retroactively with incremented values.

# How to use it?
 Just replace your desired sudoku board values in the given "board_values" 2D array variable in the code then run:
'''console
foo@bar:~$ whoami
'''
 
   
*I left the debugging prints in the code on purpose so it demonstrates what does the program do at that exact time*


