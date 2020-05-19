# SudokuSolver
Sudoku Solver in Python3 (console based)

# How it works?
 The program uses [Backtracking Algorithm](https://en.wikipedia.org/wiki/Backtracking)
* The process is the following:
   * Checks for the empty fields on the board.
   * Gets empty field indicies and the index of the containing box.
   * Tries values from 1-9 to the given indices.
   * Checking 3 positional statements if they contain the desired value:
     * BOX
     * ROW
     * COLUMN
   * If it fits to the given idices it places it in our board. Otherwise it replaces the elements of the last box retroactively with incremented values.

# Usage
 * Just replace your desired sudoku board values in the given "board_values" 2D array variable in the code:
 ```python3
 board_values = [
	[0, 0, 0, 8, 7, 1, 0, 0, 0],
	[0, 4, 9, 0, 0, 0, 1, 0, 5],
	[2, 0, 8, 0, 0, 0, 0, 0, 0],
	[5, 0, 0, 7, 0, 6, 0, 0, 0],
	[1, 7, 0, 0, 2, 0, 0, 9, 4],
	[0, 0, 0, 9, 0, 3, 0, 0, 2],
	[0, 0, 0, 0, 0, 0, 9, 0, 7],
	[8, 0, 4, 0, 0, 0, 3, 6, 0],
	[0, 0, 0, 1, 6, 4, 0, 0, 0]
]
 ```
 
 * Then run:
```console
your@name:~$ python3 sudoku.py
```
 
   
*I left the debugging prints in the code on purpose so it demonstrates what does the program do at that exact time.*


