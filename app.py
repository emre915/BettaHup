"""
BettaHub
Ana Başlatma Dosyası

Bu dosya programı başlatır.
"""

import customtkinter as ctk

from ui.main_window import MainWindow


def main():
    # Tema ayarları
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Programı başlat
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()