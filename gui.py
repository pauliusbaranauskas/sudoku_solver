# %%
import tkinter as tk
from sudoku import Sudoku
import numpy as np

# %%
class SudokuGui(Sudoku):
    def __init__(self, root):
        empty_sudoku = [[None] * 9] * 9
        self.sudoku = Sudoku(empty_sudoku)
        self.root = root
        self.mainframe = tk.Frame(self.root)
        self.draw_sudoku()
        self.draw_buttons()
        self.mainframe.pack(expand=True)

    @staticmethod
    def create_cell(sudoku_frame, row_id, col_id, value=""):
        digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9", ""}
        tkvar = tk.StringVar(root)
        tkvar.set(value)
        cell = tk.OptionMenu(sudoku_frame, tkvar, *digits)
        cell.row_id = row_id
        cell.col_id = col_id
        cell.tkvar = tkvar
        cell.grid(row=row_id, column=col_id)
        return cell

    def draw_sudoku(self):
        self.sudoku_frame = tk.Frame(self.mainframe)
        cells = []
        for row_id in range(9):
            for col_id in range(9):
                cell = self.create_cell(self.sudoku_frame, row_id, col_id)
                cells.append(cell)
        self.sudoku_frame.pack()

    def draw_buttons(self):
        self.button_frame = tk.Frame(self.root)
        self.submit_button = tk.Button(
            self.button_frame, text="SUBMIT", command=self.submit_digits
        )
        self.submit_button.pack()
        self.clear_button = tk.Button(
            self.button_frame, text="CLEAR", command=self.clear_digits
        )
        self.button_frame.pack()
        self.clear_button.pack()

    def submit_digits(self):
        matrix = self.loop_labels()
        sudoku = Sudoku(matrix)

    def clear_digits(self):
        pass

    @staticmethod
    def insert_value(matrix, row_id, col_id, value):
        if value == "":
            value = None
        else:
            value = int(value)
        matrix[row_id, col_id] = value
        return matrix

    @staticmethod
    def get_empty_matrix():
        matrix = [[None] * 9] * 9
        matrix = np.array(matrix)
        return matrix

    def loop_labels(self):
        matrix = self.get_empty_matrix()
        for child in self.sudoku_frame.children.values():
            matrix = self.insert_value(
                matrix, child.row_id, child.col_id, child.tkvar.get()
            )
        return matrix


#%%
root = tk.Tk()


gui = SudokuGui(root)

tk.mainloop()

# %%
