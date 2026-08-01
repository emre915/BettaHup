print("BettaHub başlıyor...")
import tkinter as tk


class BettaHub:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("BettaHub")

        self.root.geometry("1400x850")

        self.root.minsize(1200, 700)

        self.root.configure(bg="#0f172a")

    def run(self):

        self.root.mainloop()


if __name__ == "__main__":

    app = BettaHub()

    app.run()