# Configuration File for Party Ledger Pro

import os
from pathlib import Path

# Application Details
APP_NAME = "Party Ledger Pro"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Your Name"

# Paths
BASE_DIR = Path(__file__).parent
DATABASE_DIR = BASE_DIR / "database"
BACKUP_DIR = BASE_DIR / "backups"
DATABASE_PATH = DATABASE_DIR / "party_ledger.db"

# Create directories if they don't exist
DATABASE_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)

# UI Configuration
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
WINDOW_TITLE = f"{APP_NAME} v{APP_VERSION}"

# Database Configuration
DB_TIMEOUT = 30

# Security
DEFAULT_PIN = "1234"
AUTO_LOCK_TIME = 300  # 5 minutes in seconds

# UI Colors
PRIMARY_COLOR = "#2196F3"
SECONDARY_COLOR = "#FFC107"
SUCCESS_COLOR = "#4CAF50"
ERROR_COLOR = "#F44336"
WARNING_COLOR = "#FF9800"
BACKGROUND_COLOR = "#FAFAFA"
TEXT_COLOR = "#212121"

# Font Configuration
FONT_FAMILY = "Segoe UI"
FONT_SIZE_TITLE = 16
FONT_SIZE_NORMAL = 11
FONT_SIZE_SMALL = 9
