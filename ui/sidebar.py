import tkinter as tk


class Sidebar(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(
            width=250,
            bg="#202020"
        )

        self.pack_propagate(False)

        # =========================
        # Logo
        # =========================
        title = tk.Label(
            self,
            text="BETTAHUB",
            font=("Bahnschrift SemiBold", 22),
            bg="#202020",
            fg="#00D4FF"
        )
        title.pack(pady=(25, 5))

        subtitle = tk.Label(
            self,
            text="Professional Breeding Manager",
            font=("Bahnschrift", 9),
            bg="#202020",
            fg="#A0A0A0"
        )
        subtitle.pack(pady=(0, 30))

        # =========================
        # Menü Butonları
        # =========================

        self.create_button("🏠  Ana Sayfa")
        self.create_button("🐠  Balıklar")
        self.create_button("🏥  Sağlık")
        self.create_button("🧬  Üretim")
        self.create_button("🐣  Yavrular")
        self.create_button("🏢  Akvaryumlar")
        self.create_button("📅  Takvim")
        self.create_button("📊  Raporlar")
        self.create_button("💬  Sohbet")
        self.create_button("📷  Galeri")
        self.create_button("⚙️  Ayarlar")

    def create_button(self, text):

        button = tk.Button(
            self,
            text=text,
            font=("Bahnschrift", 11),
            bg="#2B2B2B",
            fg="white",
            activebackground="#00AEEF",
            activeforeground="white",
            relief="flat",
            bd=0,
            anchor="w",
            padx=20,
            cursor="hand2",
            height=2
        )

        button.pack(
            fill="x",
            padx=10,
            pady=3
        )