"""
BettaHub
Yeni Balık Formu
"""

import customtkinter as ctk
from tkinter import messagebox

from services.fish_service import FishService

from ui.fish_tabs.general_tab import GeneralTab
from ui.fish_tabs.genetics_tab import GeneticsTab
from ui.fish_tabs.health_tab import HealthTab
from ui.fish_tabs.breeding_tab import BreedingTab
from ui.fish_tabs.photos_tab import PhotosTab
from ui.fish_tabs.notes_tab import NotesTab

from ui.widgets import (
    PrimaryButton,
    SecondaryButton
)


class FishForm(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)

        # ==========================
        # Pencere
        # ==========================

        self.title("🐠 Yeni Balık")
        self.geometry("1000x720")
        self.resizable(False, False)

        self.grab_set()
        self.focus()

        # ==========================
        # Servis
        # ==========================

        self.fish_service = FishService()

        # ==========================
        # Başlık
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="🐠 Yeni Balık",
            font=("Bahnschrift SemiBold", 28)
        )

        title.pack(
            pady=(20, 10)
        )

        # ==========================
        # Sekmeler
        # ==========================

        self.tabs = ctk.CTkTabview(self)

        self.tabs.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        general_page = self.tabs.add("Genel")
        genetics_page = self.tabs.add("Genetik")
        health_page = self.tabs.add("Sağlık")
        breeding_page = self.tabs.add("Üretim")
        photos_page = self.tabs.add("Fotoğraflar")
        notes_page = self.tabs.add("Notlar")
                # ==========================
        # Genel
        # ==========================

        self.general_tab = GeneralTab(general_page)
        self.general_tab.pack(
            fill="both",
            expand=True
        )

        # ==========================
        # Genetik
        # ==========================

        self.genetics_tab = GeneticsTab(genetics_page)
        self.genetics_tab.pack(
            fill="both",
            expand=True
        )

        # ==========================
        # Sağlık
        # ==========================

        self.health_tab = HealthTab(health_page)
        self.health_tab.pack(
            fill="both",
            expand=True
        )

        # ==========================
        # Üretim
        # ==========================

        self.breeding_tab = BreedingTab(breeding_page)
        self.breeding_tab.pack(
            fill="both",
            expand=True
        )

        # ==========================
        # Fotoğraflar
        # ==========================

        self.photos_tab = PhotosTab(photos_page)
        self.photos_tab.pack(
            fill="both",
            expand=True
        )

        # ==========================
        # Notlar
        # ==========================

        self.notes_tab = NotesTab(notes_page)
        self.notes_tab.pack(
            fill="both",
            expand=True
        )

        # ==========================
        # Alt Butonlar
        # ==========================

        bottom = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        bottom.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        self.cancel_button = SecondaryButton(
            bottom,
            text="İptal",
            command=self.destroy
        )

        self.cancel_button.pack(
            side="right",
            padx=5
        )

        self.save_button = PrimaryButton(
            bottom,
            text="Kaydet",
            command=self.save
        )

        self.save_button.pack(
            side="right",
            padx=5
        )
          # =====================================
          # Kaydet
          # =====================================

    def save(self):

        try:
            data = self.general_tab.get_data()

            # Basit doğrulama
            if not data.get("name", "").strip():
                messagebox.showwarning(
                    "Uyarı",
                    "Lütfen balık adını giriniz."
                )
                return

            fish_code = self.fish_service.add_fish(data)

            messagebox.showinfo(
                "Başarılı",
                f"Balık başarıyla kaydedildi.\n\nKod: {fish_code}"
            )

            self.destroy()

        except Exception as e:

            messagebox.showerror(
                "Hata",
                str(e))