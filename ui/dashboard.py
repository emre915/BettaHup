"""
BettaHub
Dashboard Sayfası
"""

import customtkinter as ctk


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # Arka plan
        self.configure(fg_color="#1E1E1E")

        # Başlık
        title = ctk.CTkLabel(
            self,
            text="🐠 BETTAHUB DASHBOARD",
            font=("Bahnschrift SemiBold", 28)
        )
        title.pack(pady=(30, 10))

        subtitle = ctk.CTkLabel(
            self,
            text="Hoş Geldin Emre",
            font=("Bahnschrift", 16),
            text_color="#B0B0B0"
        )
        subtitle.pack(pady=(0, 30))

        # Kartların bulunduğu alan
        cards = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        cards.pack(fill="x", padx=30)

        self.create_card(cards, "🐠", "Toplam Balık", "11", 0)
        self.create_card(cards, "♂", "Erkek", "3", 1)
        self.create_card(cards, "♀", "Dişi", "8", 2)
        self.create_card(cards, "❤️", "Tedavide", "0", 3)

    def create_card(self, parent, icon, title, value, column):

        card = ctk.CTkFrame(
            parent,
            width=220,
            height=130,
            corner_radius=15
        )

        card.grid(row=0, column=column, padx=15)

        card.grid_propagate(False)

        ctk.CTkLabel(
            card,
            text=icon,
            font=("Segoe UI Emoji", 28)
        ).pack(pady=(18, 5))

        ctk.CTkLabel(
            card,
            text=title,
            font=("Bahnschrift", 15)
        ).pack()

        ctk.CTkLabel(
            card,
            text=value,
            font=("Bahnschrift SemiBold", 30),
            text_color="#00B7FF"
        ).pack(pady=(8, 0))