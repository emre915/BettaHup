"""
BettaHub
Ana Pencere
"""

import customtkinter as ctk

from ui.sidebar import Sidebar
from ui.dashboard import Dashboard


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Pencere Ayarları
        self.title("BettaHub")
        self.geometry("1400x850")
        self.minsize(1200, 700)

        # Arka Plan
        self.configure(fg_color="#1E1E1E")

        # Sol Menü
        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")

        # Dashboard
        self.dashboard = Dashboard(self)
        self.dashboard.pack(side="right", fill="both", expand=True)