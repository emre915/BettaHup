"""
BettaHub
Balık Yönetimi Sayfası
"""

import customtkinter as ctk

from services.fish_service import FishService
from ui.fish_form import FishForm


class FishPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # ==========================
        # Servis
        # ==========================

        self.fish_service = FishService()

        # ==========================
        # Pencere
        # ==========================

        self.configure(
            fg_color="#1E1E1E"
        )

        # ==========================
        # Üst Alan
        # ==========================

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        title = ctk.CTkLabel(
            header,
            text="🐠 Balık Yönetimi",
            font=("Bahnschrift SemiBold", 28)
        )

        title.pack(
            side="left"
        )

        self.new_button = ctk.CTkButton(
            header,
            text="+ Yeni Balık",
            width=150,
            height=40,
            command=self.open_fish_form
        )

        self.new_button.pack(
            side="right"
        )

        # ==========================
        # Arama Alanı
        # ==========================

        search_frame = ctk.CTkFrame(self)

        search_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Balık ara..."
        )

        self.search_entry.pack(
            fill="x",
            expand=True,
            padx=10,
            pady=10
        )

        # ==========================
        # Tablo Alanı
        # ==========================

        self.table_frame = ctk.CTkScrollableFrame(self)

        self.table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )
                # ==========================
        # Tablo Başlıkları
        # ==========================

        self.columns = [
            "Kod",
            "Adı",
            "Tür",
            "Varyete",
            "Cinsiyet",
            "Akvaryum",
            "Bölme",
            "İşlem"
        ]

        for col, title in enumerate(self.columns):

            header = ctk.CTkLabel(
                self.table_frame,
                text=title,
                font=("Bahnschrift SemiBold", 14)
            )

            header.grid(
                row=0,
                column=col,
                padx=10,
                pady=(10, 15),
                sticky="w"
            )

        # Kolonların genişleyebilmesi için
        for i in range(len(self.columns)):
            self.table_frame.grid_columnconfigure(
                i,
                weight=1
            )

        # İlk yükleme
        self.load_fish()
            # ======================================
    # Formu Aç
    # ======================================

    def open_fish_form(self):

        FishForm(self)

        self.after(
            300,
            self.load_fish
        )

    # ======================================
    # Tabloyu Temizle
    # ======================================

    def clear_table(self):

        for widget in self.table_frame.winfo_children():

            info = widget.grid_info()

            if int(info["row"]) > 0:
                widget.destroy()
                    # ======================================
    # Balıkları Yükle
    # ======================================
        print("load_fish çalıştı")
    def load_fish(self):

        # Eski satırları temizle
        self.clear_table()

        try:

            fish_list = self.fish_service.get_all_fish()
            print("Balık sayısı:", len(fish_list))

            for fish in fish_list:
             print(dict(fish))

        except Exception as e:

            error = ctk.CTkLabel(
                self.table_frame,
                text=f"Hata : {e}",
                text_color="red"
            )

            error.grid(
                row=1,
                column=0,
                columnspan=8,
                pady=20
            )

            return

        # Hiç kayıt yoksa
        if not fish_list:

            empty = ctk.CTkLabel(
                self.table_frame,
                text="Henüz kayıtlı balık bulunmuyor.",
                text_color="gray"
            )

            empty.grid(
                row=1,
                column=0,
                columnspan=8,
                pady=30
            )

            return

        # ==========================
        # Satırları oluştur
        # ==========================

        for row, fish in enumerate(fish_list, start=1):

            values = [

                fish["fish_code"],

                fish["name"],

                fish["species"],

                fish["variety"],

                fish["gender"],

                fish["aquarium"],

                fish["section"]

            ]

            for col, value in enumerate(values):

                lbl = ctk.CTkLabel(
                    self.table_frame,
                    text=str(value)
                )

                lbl.grid(
                    row=row,
                    column=col,
                    padx=10,
                    pady=8,
                    sticky="w"
                )

            action = ctk.CTkButton(
                self.table_frame,
                text="Düzenle",
                width=80,
                height=28
            )

            action.grid(
                row=row,
                column=7,
                padx=10
            )
                # ======================================
    # Listeyi Yenile
    # ======================================

    def refresh(self):
        """
        Balık listesini yeniden yükler.
        """
        self.load_fish()