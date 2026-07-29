"""
====================================================
BettaHub Configuration
====================================================
Bu dosya BettaHub uygulamasının merkezi ayar dosyasıdır.
Tüm modüller ayarlarını buradan alacaktır.
====================================================
"""

from pathlib import Path

# --------------------------------------------------
# Uygulama Bilgileri
# --------------------------------------------------

APP_NAME = "BettaHub"
APP_VERSION = "0.1.0"
APP_AUTHOR = "Emre Oğuz Köse"
APP_DESCRIPTION = "Profesyonel Akvaryum ve Balık Yönetim Sistemi"

# --------------------------------------------------
# Ana Dizinler
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATABASE_DIR = BASE_DIR / "database"
ASSETS_DIR = BASE_DIR / "assets"
BACKUP_DIR = BASE_DIR / "backups"
EXPORT_DIR = BASE_DIR / "exports"
LOG_DIR = BASE_DIR / "logs"
LANGUAGE_DIR = BASE_DIR / "languages"
THEME_DIR = BASE_DIR / "themes"

# --------------------------------------------------
# Veritabanı
# --------------------------------------------------

DATABASE_FILE = DATABASE_DIR / "bettahub.db"

# --------------------------------------------------
# Logo ve Görseller
# --------------------------------------------------

LOGO_DIR = ASSETS_DIR / "logos"
ICON_DIR = ASSETS_DIR / "icons"
BACKGROUND_DIR = ASSETS_DIR / "backgrounds"
FONT_DIR = ASSETS_DIR / "fonts"

# --------------------------------------------------
# Varsayılan Tema
# --------------------------------------------------

DEFAULT_THEME = "dark"

# --------------------------------------------------
# Varsayılan Dil
# --------------------------------------------------

DEFAULT_LANGUAGE = "tr"

SUPPORTED_LANGUAGES = [
    "tr",
    "en"
]

# --------------------------------------------------
# Pencere Ayarları
# --------------------------------------------------

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

WINDOW_MIN_WIDTH = 1000
WINDOW_MIN_HEIGHT = 650

# --------------------------------------------------
# Yedekleme
# --------------------------------------------------

AUTO_BACKUP = True

BACKUP_COUNT = 10

# --------------------------------------------------
# Log
# --------------------------------------------------

LOG_LEVEL = "INFO"

# --------------------------------------------------
# Oluşturulacak klasörler
# --------------------------------------------------

REQUIRED_FOLDERS = [
    DATABASE_DIR,
    ASSETS_DIR,
    BACKUP_DIR,
    EXPORT_DIR,
    LOG_DIR,
    LANGUAGE_DIR,
    THEME_DIR,
    LOGO_DIR,
    ICON_DIR,
    BACKGROUND_DIR,
    FONT_DIR,
]

# --------------------------------------------------
# Klasörleri oluştur
# --------------------------------------------------

for folder in REQUIRED_FOLDERS:
    folder.mkdir(parents=True, exist_ok=True)