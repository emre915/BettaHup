"""
BettaHub
Ortak Arayüz Bileşenleri
"""

import customtkinter as ctk
from themes.theme import COLORS, FONTS, SIZES


class SectionTitle(ctk.CTkLabel):
    """
    Form bölüm başlığı
    """

    def __init__(self, parent, text):
        super().__init__(
            parent,
            text=text,
            font=FONTS["subtitle"],
            text_color=COLORS["text"]
        )


class FormLabel(ctk.CTkLabel):
    """
    Alan etiketi
    """

    def __init__(self, parent, text):
        super().__init__(
            parent,
            text=text,
            font=FONTS["body"],
            text_color=COLORS["text"]
        )


class FormEntry(ctk.CTkEntry):
    """
    Standart giriş kutusu
    """

    def __init__(self, parent, placeholder=""):

        super().__init__(
            parent,
            height=SIZES["entry_height"],
            placeholder_text=placeholder
        )


class FormCombo(ctk.CTkComboBox):
    """
    Standart açılır liste
    """

    def __init__(self, parent, values):

        super().__init__(
            parent,
            values=values,
            height=SIZES["entry_height"]
        )


class PrimaryButton(ctk.CTkButton):
    """
    Ana işlem butonu
    """

    def __init__(self, parent, text, command=None):

        super().__init__(
            parent,
            text=text,
            command=command,
            width=SIZES["button_width"],
            height=SIZES["button_height"],
            corner_radius=SIZES["corner_radius"]
        )


class SecondaryButton(ctk.CTkButton):
    """
    İptal / Geri butonu
    """

    def __init__(self, parent, text, command=None):

        super().__init__(
            parent,
            text=text,
            command=command,
            width=SIZES["button_width"],
            height=SIZES["button_height"],
            corner_radius=SIZES["corner_radius"],
            fg_color="gray40",
            hover_color="gray30"
        )