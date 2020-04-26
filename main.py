# %%
from sudoku import force_sudoku

# %%
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

#%%

force_sudoku(empty_sudoku)

# %%
