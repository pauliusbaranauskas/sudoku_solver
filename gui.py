# %%
import tkinter as tk
from sudoku import Sudoku
import numpy as np
from sudoku import force_sudoku
from tkinter import ttk

# %%
class SudokuGui(Sudoku):
    def __init__(self, root):
        self.sudoku = Sudoku()
        self.root = root
        self.mainframe = tk.Frame(self.root)
        self.draw_sudoku()
        self.draw_buttons()
        self.mainframe.pack(expand=True)

    def insert_row_separator(self, parent, row_id, col_id):
        """Inserts horizontal separator between lines.

        Args:
            parent (tk.Frame): Tkinter frame used as a parent.
            row_id (int): Position of label in a grid.
            col_id (int): Position of label in a grid.
        """
        separator = ttk.Separator(parent, orient=tk.HORIZONTAL)
        separator.separator = True
        separator.grid(column=col_id, row=row_id, pady=5)

    def insert_column_separator(self, parent, row_id, col_id):
        """Inserts vertical separator between columns

        Args:
            parent (tk.Frame): Parent frame.
            row_id (int): Position of label in a grid.
            col_id (int): Position of label in a grid.
        """
        separator = ttk.Separator(parent, orient=tk.VERTICAL)
        separator.separator = True
        separator.grid(column=col_id, row=row_id, padx=5)

    def create_cell(self, sudoku_frame, row_id, col_id, value):
        """Creates a single cell for a single number.

        Args:
            sudoku_frame (Tk.Frame): Parent frame.
            row_id (int): Row id of a sudoku.
            col_id (int): Column id of a sudoku.
            value (int): Number to be inserted to a cell.

        Returns:
            Tk.OptionMenu: Created dropdown list.
        """
        grid_row = row_id + row_id // 3
        grid_column = col_id + col_id // 3
        if row_id in [3, 6]:
            self.insert_row_separator(sudoku_frame, grid_row, grid_column)
        if col_id in [3, 6]:
            self.insert_column_separator(sudoku_frame, grid_row, grid_column)
        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
        tkvar = tk.StringVar(self.root)
        if value is None:
            value = " "
        else:
            value = str(value)
        tkvar.set(value)
        cell = tk.OptionMenu(sudoku_frame, tkvar, *digits)
        cell.row_id = row_id
        cell.col_id = col_id
        cell.tkvar = tkvar
        cell.separator = False
        cell.grid(row=grid_row + 1, column=grid_column + 1)
        return cell

    def draw_sudoku(self):
        """Draws and fills cells for sudoku.
        """
        self.sudoku_frame = tk.Frame(self.mainframe)
        cells = []
        for row_id, row in enumerate(self.sudoku.sudoku):
            for col_id, cell in enumerate(row):
                cell = self.create_cell(self.sudoku_frame, row_id, col_id, cell)
                cells.append(cell)
        self.sudoku_frame.pack()

    def draw_buttons(self):
        """Draws buttons frame and buttons. Also assigns commands to buttons.
        """
        self.button_frame = tk.Frame(self.root)
        self.submit_button = tk.Button(
            self.button_frame, text="SUBMIT", command=self.submit_digits
        )
        self.clear_button = tk.Button(
            self.button_frame, text="CLEAR", command=self.clear_digits
        )
        self.submit_button.pack(side="left")
        self.clear_button.pack(side="right")
        self.button_frame.pack(fill=tk.X)

    def submit_digits(self):
        """Runs through cells, takes digits from cells, passes results to a solver
        and fills cells with solutions.
        """
        matrix = self.loop_labels()
        self.sudoku.sudoku = force_sudoku(matrix)
        self.redraw_sudoku()

    def clear_digits(self):
        """Clears all entered digits and redraws sudoku frame.
        """
        self.sudoku.sudoku = self.sudoku.get_empty_matrix()
        self.redraw_sudoku()

    @staticmethod
    def insert_value(matrix, row_id, col_id, value):
        """Parses input from a cell, inserts it into matrix and returns updated matrix.

        Args:
            matrix (np.matrix): Original matrix with sudoku values.
            row_id (int): Id of row, where value should be inserted.
            col_id (int): Id of column, where value should be inserted.
            value (str): Value to be inserted to a matrix. It is converted to integer.

        Returns:
            np.matrix: Updated matrix.
        """
        if value == " ":
            value = None
        else:
            value = int(value)
        matrix[row_id, col_id] = value
        return matrix

    def loop_labels(self):
        """Loops through cells, extracts digits and formats matrix.

        Returns:
            np.matrix: Matrix filled with inserted values.
        """
        matrix = self.get_empty_matrix()
        for child in self.sudoku_frame.children.values():
            if child.separator is False:
                matrix = self.insert_value(
                    matrix, child.row_id, child.col_id, child.tkvar.get()
                )
        return matrix

    def redraw_sudoku(self):
        """Destroys sudoku frame and redraws new one.
        """
        self.sudoku_frame.destroy()
        self.draw_sudoku()
