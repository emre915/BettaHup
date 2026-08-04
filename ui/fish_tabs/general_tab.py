"""
BettaHub
Genel Bilgiler Sekmesi
"""

import customtkinter as ctk

from ui.widgets import (
    SectionTitle,
    FormLabel,
    FormEntry,
    FormCombo
)


class GeneralTab(ctk.CTkScrollableFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="transparent")

        # ==========================
        # Grid
        # ==========================

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ==========================
        # Başlık
        # ==========================

        SectionTitle(
            self,
            "🐠 Genel Bilgiler"
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=20,
            pady=(20, 20)
        )

        # ======================================================
        # SOL SÜTUN
        # ======================================================

        FormLabel(self, "Balık Adı").grid(
            row=1,
            column=0,
            sticky="w",
            padx=20,
            pady=(10, 2)
        )

        self.fish_name = FormEntry(self)

        self.fish_name.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20
        )

        FormLabel(self, "Varyete").grid(
            row=3,
            column=0,
            sticky="w",
            padx=20,
            pady=(15, 2)
        )

        self.variety = FormCombo(
            self,
            [
                "Halfmoon",
                "HMPK",
                "Plakat",
                "Crowntail",
                "Double Tail",
                "Dumbo",
                "Koi",
                "Alien",
                "Dragon",
                "Veiltail",
                "Diğer"
            ]
        )

        self.variety.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=20
        )

        FormLabel(self, "Renk").grid(
            row=5,
            column=0,
            sticky="w",
            padx=20,
            pady=(15, 2)
        )

        self.color = FormEntry(self)

        self.color.grid(
            row=6,
            column=0,
            sticky="ew",
            padx=20
        )

        FormLabel(self, "Akvaryum").grid(
            row=7,
            column=0,
            sticky="w",
            padx=20,
            pady=(15, 2)
        )

        self.aquarium = FormCombo(
            self,
            [
                "Henüz Yok"
            ]
        )

        self.aquarium.grid(
            row=8,
            column=0,
            sticky="ew",
            padx=20
        )

        # ======================================================
        # SAĞ SÜTUN
        # ======================================================

        FormLabel(self, "Tür").grid(
            row=1,
            column=1,
            sticky="w",
            padx=20,
            pady=(10, 2)
        )

        self.fish_type = FormCombo(
            self,
            [
                "Betta splendens"
            ]
        )

        self.fish_type.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=20
        )

        FormLabel(self, "Cinsiyet").grid(
            row=3,
            column=1,
            sticky="w",
            padx=20,
            pady=(15, 2)
        )

        self.gender = FormCombo(
            self,
            [
                "Erkek",
                "Dişi"
            ]
        )

        self.gender.grid(
            row=4,
            column=1,
            sticky="ew",
            padx=20
        )

        FormLabel(self, "Doğum Tarihi").grid(
            row=5,
            column=1,
            sticky="w",
            padx=20,
            pady=(15, 2)
        )

        self.birth_date = FormEntry(
        self,
        placeholder="GG/AA/YYYY"
        )  

        self.birth_date.grid(
            row=6,
            column=1,
            sticky="ew",
            padx=20
        )

        FormLabel(self, "Bölme").grid(
            row=7,
            column=1,
            sticky="w",
            padx=20,
            pady=(15, 2)
        )

        self.section = FormCombo(
            self,
            [
                "Henüz Yok"
            ]
        )

        self.section.grid(
            row=8,
            column=1,
            sticky="ew",
            padx=20
        )

    # ======================================================
    # Form Verileri
    # ======================================================

    def get_data(self):
        """
        Formdaki tüm bilgileri sözlük olarak döndürür.
        """

        return {
            "name": self.fish_name.get().strip(),
            "species": self.fish_type.get().strip(),
            "variety": self.variety.get().strip(),
            "gender": self.gender.get().strip(),
            "color": self.color.get().strip(),
            "birth_date": self.birth_date.get().strip(),
            "aquarium": self.aquarium.get().strip(),
            "section": self.section.get().strip(),
        }

    # ======================================================
    # Form Temizle
    # ======================================================

    def clear(self):
        """
        Formu temizler.
        """

        self.fish_name.delete(0, "end")
        self.color.delete(0, "end")
        self.birth_date.delete(0, "end")