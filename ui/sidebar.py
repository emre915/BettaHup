"""
BettaHub
Sol Menü (Sidebar)
"""

import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            width=250,
            corner_radius=0,
            fg_color="#252526"
        )

        self.pack_propagate(False)

        # =========================
        # Logo
        # =========================

        title = ctk.CTkLabel(
            self,
            text="🐠 BETTAHUB",
            font=("Bahnschrift SemiBold", 24),
            text_color="white"
        )
        title.pack(pady=(25, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Professional Breeding Manager",
            font=("Bahnschrift", 11),
            text_color="#A0A0A0"
        )
        subtitle.pack(pady=(0, 30))

        # =========================
        # Menü Butonları
        # =========================

        self.create_button("🏠  Ana Sayfa")
        self.create_button("🐠  Balıklar")
        self.create_button("❤️  Sağlık")
        self.create_button("🧬  Üretim")
        self.create_button("🐣  Yavrular")
        self.create_button("🏢  Akvaryumlar")
        self.create_button("📊  Raporlar")
        self.create_button("⚙️  Ayarlar")

        # Alt boşluk
        ctk.CTkLabel(self, text="").pack(expand=True)

        version = ctk.CTkLabel(
            self,
            text="BettaHub v0.2",
            font=("Bahnschrift", 11),
            text_color="#707070"
        )
        version.pack(pady=20)

    def create_button(self, text):

        button = ctk.CTkButton(
            self,
            text=text,
            height=45,
            corner_radius=8,
            font=("Bahnschrift", 15),
            anchor="w",
            fg_color="transparent",
            hover_color="#3A3A3A",
            text_color="white"
        )

        button.pack(fill="x", padx=15, pady=4)