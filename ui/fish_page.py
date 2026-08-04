"""
BettaHub
Balık Yönetimi Sayfası
"""

import customtkinter as ctk
from ui.fish_form import FishForm


class FishPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="#1E1E1E")

        # ==========================
        # Üst Başlık
        # ==========================

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(20, 10))

        title = ctk.CTkLabel(
            header,
            text="🐠 Balık Yönetimi",
            font=("Bahnschrift SemiBold", 28)
        )
        title.pack(side="left")

        new_button = ctk.CTkButton(
            header,
            text="+ Yeni Balık",
            width=140,
            height=40,
            command=self.open_fish_form
        )
        new_button.pack(side="right")

        # ==========================
        # Arama Alanı
        # ==========================

        search_frame = ctk.CTkFrame(self)
        search_frame.pack(fill="x", padx=20)

        search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Balık ara..."
        )

        search_entry.pack(
            side="left",
            padx=10,
            pady=10,
            fill="x",
            expand=True
        )

        # ==========================
        # Tablo
        # ==========================

        table = ctk.CTkFrame(self)

        table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        columns = [
            "ID",
            "Foto",
            "Adı",
            "Tür",
            "Cinsiyet",
            "Akvaryum",
            "Durum",
            "Yaş"
        ]

        for i, text in enumerate(columns):

            lbl = ctk.CTkLabel(
                table,
                text=text,
                font=("Bahnschrift SemiBold", 14)
            )

            lbl.grid(
                row=0,
                column=i,
                padx=12,
                pady=12
            )

        empty = ctk.CTkLabel(
            table,
            text="Henüz kayıtlı balık bulunmuyor.",
            text_color="gray",
            font=("Bahnschrift", 15)
        )

        empty.grid(
            row=1,
            column=0,
            columnspan=8,
            pady=50)

    # ======================================
    # Yeni Balık Penceresini Aç
    # ======================================

    def open_fish_form(self):
        FishForm(self)