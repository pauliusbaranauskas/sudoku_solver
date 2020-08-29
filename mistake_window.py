import tkinter as tk

class MistakeWindow:
    def __init__(self, root, error_message):
        self.root = root
        message = tk.Label(root, text=error_message)
        ok_button = tk.Button(root, text="OK", command=self.close_window)
        message.pack()
        ok_button.pack()

    def close_window(self):
        """Destroys root window.
        """
        self.root.destroy()