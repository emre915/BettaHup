import tkinter as tk
from ui.sidebar import Sidebar

class MainWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("BettaHub")

        self.root.geometry("1400x850")

        self.root.minsize(1200, 700)

        self.root.configure(bg="#0f172a")
        self.sidebar = Sidebar(self.root)
        self.sidebar.pack(side="left", fill="y")

    def run(self):

        self.root.mainloop()