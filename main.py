"""Driver file."""

from tk_src.gui import MainApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
