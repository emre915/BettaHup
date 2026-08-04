"""
BettaHub
Ana Pencere
"""

import customtkinter as ctk

from ui.sidebar import Sidebar
from ui.dashboard import Dashboard
from ui.fish_page import FishPage


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        # -----------------------------
        # Pencere Ayarları
        # -----------------------------

        self.title("BettaHub")
        self.geometry("1400x850")
        self.minsize(1200, 700)

        self.configure(fg_color="#1E1E1E")

        # -----------------------------
        # Sol Menü
        # -----------------------------

        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")

        # -----------------------------
        # İçerik Alanı
        # -----------------------------

        self.content = ctk.CTkFrame(
            self,
            fg_color="#1E1E1E",
            corner_radius=0
        )

        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        # Sayfalar

        self.dashboard = Dashboard(self.content)
        self.fish_page = FishPage(self.content)

        # İlk açılışta Dashboard göster

        self.show_dashboard()

    # =================================

    def clear_pages(self):

        for widget in self.content.winfo_children():
            widget.pack_forget()

    # =================================

    def show_dashboard(self):

        self.clear_pages()

        self.dashboard.pack(
            fill="both",
            expand=True
        )

    # =================================

    def show_fish_page(self):

        self.clear_pages()

        self.fish_page.pack(
            fill="both",
            expand=True
        )