"""
BettaHub
Sağlık Sekmesi
"""

import customtkinter as ctk
from ui.widgets import SectionTitle


class HealthTab(ctk.CTkScrollableFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="transparent")

        title = SectionTitle(
            self,
            "❤️ Sağlık Bilgileri"
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        info = ctk.CTkLabel(
            self,
            text="Bu bölüm bir sonraki görevde geliştirilecek.",
            font=("Bahnschrift", 14)
        )

        info.pack(
            anchor="w",
            padx=20
        )