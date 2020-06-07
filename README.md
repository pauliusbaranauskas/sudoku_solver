My free time project that aims to solve sudoku.

Future goals: pass a picture of sudoku to the app and app returns solved sudoku.

# Usage (CLI)

To use solver from file `sudoku.py` import function `force_sudoku`.

```
from sudoku import force_sudoku

empty_sudoku = [
    [None, None, None, 9, None, 1, None, 6, None],
    [None, 6, None, None, None, 4, 1, None, None],
    [None, 8, 1, 6, 7, 2, 4, None, 3],
    [None, 3, 5, 7, None, 8, None, None, None],
    [None, 9, 2, 3, None, 6, 7, 4, None],
    [None, None, None, 1, None, 9, 5, 3, None],
    [8, None, 4, 2, 9, 3, 6, 7, None],
    [None, None, 6, None, None, None, None, 8, None],
    [None, 7, None, None, None, 5, None, None, None],
]

solved_sudoku = force_sudoku(empty_sudoku)
```
Or you could import `Sudoku` class and have your own implementation of methods existing.

# Usage GUI

To use solver with Graphical User Interface (GUI) you have to lauch this interface. To do so, launch your terminal and navigate to directory of this project. Then use command `python3 main.py` to lauch app.
After lauch, you will be able to set your existing values.
When your values are selected, click `Submit` button to solve this sudoku or `Clear` button, to clear all cells.

# Project rules

* language: `Python`
* Docstring style: `google`

