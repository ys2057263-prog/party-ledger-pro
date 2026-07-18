# Database Module - SQLite Database Management

import sqlite3
import os
from datetime import datetime
from config import DATABASE_PATH, DATABASE_DIR

class Database:
    def __init__(self):
        self.db_path = str(DATABASE_PATH)
        self.init_database()
    
    def get_connection(self):
        """Get database connection"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        """Initialize database with all tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Users Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    pin_hash TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_login TIMESTAMP
                )
            ''')
            
            # Ledgers Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ledgers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    UNIQUE(user_id, name)
                )
            ''')
            
            # Parties Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS parties (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ledger_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    phone TEXT,
                    email TEXT,
                    address TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (ledger_id) REFERENCES ledgers(id),
                    UNIQUE(ledger_id, name)
                )
            ''')
            
            # Transactions Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ledger_id INTEGER NOT NULL,
                    party_id INTEGER NOT NULL,
                    type TEXT NOT NULL,
                    amount REAL NOT NULL,
                    date DATE NOT NULL,
                    remark TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (ledger_id) REFERENCES ledgers(id),
                    FOREIGN KEY (party_id) REFERENCES parties(id)
                )
            ''')
            
            # Settings Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS settings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    key TEXT NOT NULL,
                    value TEXT,
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    UNIQUE(user_id, key)
                )
            ''')
            
            # Backup History Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS backup_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    backup_path TEXT NOT NULL,
                    backup_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    file_size INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            ''')
            
            conn.commit()
            print("✅ Database initialized successfully!")
            
        except Exception as e:
            print(f"❌ Error initializing database: {e}")
            conn.rollback()
        finally:
            conn.close()
    
    def execute_query(self, query, params=None):
        """Execute a query"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"❌ Error executing query: {e}")
            return False
    
    def fetch_all(self, query, params=None):
        """Fetch all results"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            results = cursor.fetchall()
            conn.close()
            return results
        except Exception as e:
            print(f"❌ Error fetching data: {e}")
            return []
    
    def fetch_one(self, query, params=None):
        """Fetch single result"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            result = cursor.fetchone()
            conn.close()
            return result
        except Exception as e:
            print(f"❌ Error fetching data: {e}")
            return None

# Global database instance
db = Database()
