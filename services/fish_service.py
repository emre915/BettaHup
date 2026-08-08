"""
BettaHub
Fish Service
"""

from database.database import DatabaseManager


class FishService:

    def __init__(self):
        self.db = DatabaseManager()

    def generate_fish_code(self):
        result = self.db.fetchone(
            "SELECT MAX(id) AS max_id FROM fish"
        )
        next_id = (result["max_id"] or 0) + 1
        return f"BH-{next_id:06d}"

    def add_fish(self, data):
        fish_code = self.generate_fish_code()

        self.db.execute(
            """
            INSERT INTO fish
            (
                fish_code, name, species, variety, gender,
                color, birth_date, aquarium, section
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                fish_code,
                data.get("name", ""),
                data.get("species", ""),
                data.get("variety", ""),
                data.get("gender", ""),
                data.get("color", ""),
                data.get("birth_date", ""),
                data.get("aquarium", ""),
                data.get("section", "")
            )
        )

        return fish_code

    def get_all_fish(self):
        return self.db.fetchall(
            """
            SELECT *
            FROM fish
            ORDER BY id DESC
            """
        )

    def get_fish(self, fish_id):
        return self.db.fetchone(
            """
            SELECT *
            FROM fish
            WHERE id=?
            """,
            (fish_id,)
        )

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
                section=?,
                updated_at=CURRENT_TIMESTAMP
            WHERE id=?
            """,
            (
                data.get("name", ""),
                data.get("species", ""),
                data.get("variety", ""),
                data.get("gender", ""),
                data.get("color", ""),
                data.get("birth_date", ""),
                data.get("aquarium", ""),
                data.get("section", ""),
                fish_id
            )
        )

    def delete_fish(self, fish_id):
        self.db.execute(
            "DELETE FROM fish WHERE id=?",
            (fish_id,)
        )

    def close(self):
        self.db.close()
