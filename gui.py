# %%
import tkinter as tk

# %%
class SudokuGui:
    def __init__(self, root):

        self.root = root
        self.mainframe = tk.Frame(self.root)
        self.draw_sudoku()
        self.draw_buttons()
        self.mainframe.pack(expand=True)

    def draw_sudoku(self):
        self.sudoku_frame = tk.Frame(self.mainframe)
        for row_id in range(9):
            for col_id in range(9):
                cell = tk.Entry(self.sudoku_frame)
                cell.grid(row=row_id, column=col_id)
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
        print("a")

    def clear_digits(self):
        print("b")


#%%
root = tk.Tk()


gui = SudokuGui(root)

tk.mainloop()

# %%
