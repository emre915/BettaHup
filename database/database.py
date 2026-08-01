"""
==========================================
BettaHub Database Manager
==========================================

Bu dosya BettaHub uygulamasının
veritabanı bağlantısını yönetir.

"""

import sqlite3
from pathlib import Path

from config import DATABASE_FILE


class DatabaseManager:
    """
    BettaHub Veritabanı Yöneticisi
    """

    def __init__(self):

        self.database = DATABASE_FILE
        self.connection = None

    def connect(self):
        """
        Veritabanına bağlan.
        """

        self.connection = sqlite3.connect(self.database)

        return self.connection

    def close(self):
        """
        
        Bağlantıyı kapat.
        """

        if self.connection:
            self.connection.close()
            self.connection = None
    def execute(self, query, params=()):
        """
        INSERT, UPDATE ve DELETE sorgularını çalıştırır.
        """
        cursor = self.connect().cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def fetchone(self, query, params=()):
        """
        Tek bir kayıt döndürür.
        """
        cursor = self.connect().cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def fetchall(self, query, params=()):
        """
        Tüm kayıtları döndürür.
        """
        cursor = self.connect().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()