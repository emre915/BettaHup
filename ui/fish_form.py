"""
BettaHub
Balık Formu
Yeni Balık + Balık Düzenleme + Balık Silme
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

    def __init__(self, parent, fish=None):
        super().__init__(parent)

        self.parent_page = parent
        self.fish_service = FishService()
        self.fish = fish

        # ==========================
        # Pencere
        # ==========================

        if self.fish:
            self.title("🐠 Balık Düzenle")
        else:
            self.title("🐠 Yeni Balık")

        self.geometry("1000x720")
        self.resizable(False, False)

        self.grab_set()
        self.focus()

        # ==========================
        # Başlık
        # ==========================

        title_text = "🐠 Balık Düzenle" if self.fish else "🐠 Yeni Balık"

        title = ctk.CTkLabel(
            self,
            text=title_text,
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
        # Düzenleme verisini yükle
        # ==========================

        if self.fish:
            self.load_fish_data()

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

        # Sil butonu sadece düzenleme modunda
        if self.fish:

            self.delete_button = ctk.CTkButton(
                bottom,
                text="🗑 Balığı Sil",
                width=120,
                height=38,
                fg_color="#B3261E",
                hover_color="#8C1D18",
                command=self.delete_fish
            )

            self.delete_button.pack(
                side="left",
                padx=5
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
            text="Değişiklikleri Kaydet" if self.fish else "Kaydet",
            command=self.save
        )

        self.save_button.pack(
            side="right",
            padx=5
        )

    # ======================================
    # Mevcut Balık Bilgilerini Forma Yükle
    # ======================================

    def load_fish_data(self):

        try:

            fish = self.fish

            data = {
                "name": fish["name"] or "",
                "species": fish["species"] or "",
                "variety": fish["variety"] or "",
                "gender": fish["gender"] or "",
                "color": fish["color"] or "",
                "birth_date": fish["birth_date"] or "",
                "aquarium": fish["aquarium"] or "",
                "section": fish["section"] or ""
            }

            # Balık adı
            self.general_tab.fish_name.delete(0, "end")
            self.general_tab.fish_name.insert(0, data["name"])

            # Varyete
            self.general_tab.variety.set(data["variety"])

            # Renk
            self.general_tab.color.delete(0, "end")
            self.general_tab.color.insert(0, data["color"])

            # Akvaryum
            self.general_tab.aquarium.set(data["aquarium"])

            # Tür
            self.general_tab.fish_type.set(data["species"])

            # Cinsiyet
            self.general_tab.gender.set(data["gender"])

            # Doğum tarihi
            self.general_tab.birth_date.delete(0, "end")
            self.general_tab.birth_date.insert(0, data["birth_date"])

            # Bölme
            self.general_tab.section.set(data["section"])

        except Exception as e:

            messagebox.showerror(
                "Hata",
                f"Balık bilgileri forma yüklenemedi.\n\n{e}"
            )

    # ======================================
    # Kaydet / Güncelle
    # ======================================

    def save(self):

        try:

            data = self.general_tab.get_data()

            # ------------------------------
            # Basit doğrulama
            # ------------------------------

            if not data.get("name", "").strip():

                messagebox.showwarning(
                    "Uyarı",
                    "Lütfen balık adını giriniz."
                )

                return

            # ==============================
            # Düzenleme
            # ==============================

            if self.fish:

                self.fish_service.update_fish(
                    self.fish["id"],
                    data
                )

                messagebox.showinfo(
                    "Başarılı",
                    "Balık bilgileri başarıyla güncellendi."
                )

            # ==============================
            # Yeni kayıt
            # ==============================

            else:

                fish_code = self.fish_service.add_fish(data)

                messagebox.showinfo(
                    "Başarılı",
                    f"Balık başarıyla kaydedildi.\n\nKod: {fish_code}"
                )

            # Listeyi yenile
            if hasattr(self.parent_page, "refresh"):
                self.parent_page.refresh()

            self.destroy()

        except Exception as e:

            messagebox.showerror(
                "Hata",
                str(e)
            )

    # ======================================
    # Balık Sil
    # ======================================

    def delete_fish(self):

        if not self.fish:
            return

        fish_name = self.fish["name"] or self.fish["fish_code"]

        answer = messagebox.askyesno(
            "Balığı Sil",
            f'"{fish_name}" adlı balığı silmek istediğinize emin misiniz?\n\n'
            "Bu işlem geri alınamaz."
        )

        if not answer:
            return

        try:

            self.fish_service.delete_fish(
                self.fish["id"]
            )

            messagebox.showinfo(
                "Başarılı",
                "Balık başarıyla silindi."
            )

            if hasattr(self.parent_page, "refresh"):
                self.parent_page.refresh()

            self.destroy()

        except Exception as e:

            messagebox.showerror(
                "Hata",
                f"Balık silinemedi.\n\n{e}"
            )
