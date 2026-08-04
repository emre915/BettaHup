"""
BettaHub
Sol Menü
"""

import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            width=250,
            fg_color="#252526",
            corner_radius=0
        )

        self.parent = parent

        self.pack_propagate(False)

        # ==========================
        # Logo
        # ==========================

        ctk.CTkLabel(
            self,
            text="🐠 BETTAHUB",
            font=("Bahnschrift SemiBold", 24),
            text_color="white"
        ).pack(pady=(25, 5))

        ctk.CTkLabel(
            self,
            text="Professional Breeding Manager",
            font=("Bahnschrift", 11),
            text_color="#A0A0A0"
        ).pack(pady=(0, 30))

        # ==========================
        # Menü Butonları
        # ==========================

        self.create_button(
            "🏠 Ana Sayfa",
            self.parent.show_dashboard
        )

        self.create_button(
            "🐠 Balıklar",
            self.parent.show_fish_page
        )

        self.create_button("❤️ Sağlık")
        self.create_button("🧬 Üretim")
        self.create_button("🐣 Yavrular")
        self.create_button("🏢 Akvaryumlar")
        self.create_button("📊 Raporlar")
        self.create_button("⚙️ Ayarlar")

        ctk.CTkLabel(
            self,
            text=""
        ).pack(expand=True)

        ctk.CTkLabel(
            self,
            text="BettaHub v0.3",
            font=("Bahnschrift", 11),
            text_color="#808080"
        ).pack(pady=20)

    # ===================================

    def create_button(self, text, command=None):

        button = ctk.CTkButton(
            self,
            text=text,
            command=command,
            height=45,
            corner_radius=8,
            anchor="w",
            fg_color="transparent",
            hover_color="#3A3A3A",
            text_color="white",
            font=("Bahnschrift", 15)
        )

        button.pack(
            fill="x",
            padx=15,
            pady=4
        )