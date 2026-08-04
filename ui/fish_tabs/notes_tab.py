"""
BettaHub
Notlar Sekmesi
"""

import customtkinter as ctk

from ui.widgets import SectionTitle


class NotesTab(ctk.CTkScrollableFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="transparent")

        title = SectionTitle(
            self,
            "📝 Notlar"
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        self.notes = ctk.CTkTextbox(
            self,
            height=400
        )

        self.notes.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )