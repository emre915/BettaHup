"""
BettaHub
Fish Service
"""

from database.database import DatabaseManager


class FishService:

    def __init__(self):

        self.db = DatabaseManager()

    # ==========================================
    # Yeni BH Kodu
    # ==========================================

    def generate_fish_code(self):

        result = self.db.fetchone(
            "SELECT COUNT(*) AS total FROM fish"
        )

        total = result["total"] + 1

        return f"BH-{total:06d}"

    # ==========================================
    # Balık Ekle
    # ==========================================

    def add_fish(self, data):

        fish_code = self.generate_fish_code()

        self.db.execute(
            """
            INSERT INTO fish
            (
                fish_code,
                name,
                species,
                variety,
                gender,
                color,
                birth_date,
                aquarium,
                section
            )

            VALUES
            (
                ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                fish_code,
                data["name"],
                data["species"],
                data["variety"],
                data["gender"],
                data["color"],
                data["birth_date"],
                data["aquarium"],
                data["section"]
            )
        )

        return fish_code

    # ==========================================
    # Tüm Balıkları Getir
    # ==========================================

    def get_all_fish(self):
        # ==========================================
        # Tek Balık Getir
        # ==========================================

     def get_fish(self, fish_id):

        return self.db.fetchone(
            """
            SELECT *
            FROM fish
            WHERE id=?
            """,
            (fish_id,)
        )

        return self.db.fetchall(
            """
            SELECT *
            FROM fish
            ORDER BY id DESC
            """
        )

    # ==========================================
    # Balık Sil
    # ==========================================
    # ==========================================
    # Balık Güncelle
    # ==========================================

    def update_fish(self, fish_id, data):

        self.db.execute(
            """
            UPDATE fish
            SET
                name=?,
                species=?,
                variety=?,
                gender=?,
                color=?,
                birth_date=?,
                aquarium=?,
                section=?
            WHERE id=?
            """,
            (
                data["name"],
                data["species"],
                data["variety"],
                data["gender"],
                data["color"],
                data["birth_date"],
                data["aquarium"],
                data["section"],
                fish_id
            )
        )
    def delete_fish(self, fish_id):

        self.db.execute(
            """
            DELETE FROM fish
            WHERE id=?
            """,
            (fish_id,)
        )

    # ==========================================
    # Veritabanını Kapat
    # ==========================================

    def close(self):

        self.db.close()