# %%
import tkinter as tk

from gui import SudokuGui
# %%

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGui(root)
    tk.mainloop()
