# Login Module - User Authentication

from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QMessageBox, QWidget
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from config import APP_NAME, PRIMARY_COLOR
from database import db
from utils import hash_pin, verify_pin

class LoginWindow(QDialog):
    login_successful = pyqtSignal(int)  # Signal with user_id
    
    def __init__(self):
        super().__init__()
        self.user_id = None
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        self.setWindowTitle(f"{APP_NAME} - Login")
        self.setGeometry(100, 100, 400, 250)
        self.setModal(True)
        self.setStyleSheet(self.get_styles())
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("Party Ledger Pro")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Username
        username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username")
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        
        # PIN
        pin_label = QLabel("PIN:")
        pin_layout = QHBoxLayout()
        
        self.pin_input = QLineEdit()
        self.pin_input.setPlaceholderText("Enter 4-digit PIN")
        self.pin_input.setEchoMode(QLineEdit.Password)
        self.pin_input.setMaxLength(4)
        
        self.show_pin_btn = QPushButton("👁")
        self.show_pin_btn.setMaximumWidth(40)
        self.show_pin_btn.clicked.connect(self.toggle_pin_visibility)
        
        pin_layout.addWidget(self.pin_input)
        pin_layout.addWidget(self.show_pin_btn)
        
        layout.addWidget(pin_label)
        layout.addLayout(pin_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.login)
        login_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {PRIMARY_COLOR};
                color: white;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #1976D2;
            }}
        """)
        
        signup_btn = QPushButton("Sign Up")
        signup_btn.clicked.connect(self.signup)
        
        button_layout.addWidget(login_btn)
        button_layout.addWidget(signup_btn)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def toggle_pin_visibility(self):
        """Toggle PIN visibility"""
        if self.pin_input.echoMode() == QLineEdit.Password:
            self.pin_input.setEchoMode(QLineEdit.Normal)
            self.show_pin_btn.setText("🙈")
        else:
            self.pin_input.setEchoMode(QLineEdit.Password)
            self.show_pin_btn.setText("👁")
    
    def login(self):
        """Handle login"""
        username = self.username_input.text().strip()
        pin = self.pin_input.text().strip()
        
        if not username or not pin:
            QMessageBox.warning(self, "Validation Error", "Please enter username and PIN")
            return
        
        if len(pin) != 4 or not pin.isdigit():
            QMessageBox.warning(self, "Validation Error", "PIN must be 4 digits")
            return
        
        # Check user in database
        query = "SELECT id, pin_hash FROM users WHERE username = ?"
        user = db.fetch_one(query, (username,))
        
        if user and verify_pin(pin, user['pin_hash']):
            self.user_id = user['id']
            # Update last login
            db.execute_query(
                "UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = ?",
                (self.user_id,)
            )
            self.login_successful.emit(self.user_id)
            self.accept()
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or PIN")
            self.pin_input.clear()
    
    def signup(self):
        """Handle signup"""
        username = self.username_input.text().strip()
        pin = self.pin_input.text().strip()
        
        if not username or not pin:
            QMessageBox.warning(self, "Validation Error", "Please enter username and PIN")
            return
        
        if len(username) < 3:
            QMessageBox.warning(self, "Validation Error", "Username must be at least 3 characters")
            return
        
        if len(pin) != 4 or not pin.isdigit():
            QMessageBox.warning(self, "Validation Error", "PIN must be 4 digits")
            return
        
        # Check if user exists
        query = "SELECT id FROM users WHERE username = ?"
        existing_user = db.fetch_one(query, (username,))
        
        if existing_user:
            QMessageBox.warning(self, "Error", "Username already exists")
            return
        
        # Create new user
        pin_hash = hash_pin(pin)
        query = "INSERT INTO users (username, pin_hash) VALUES (?, ?)"
        
        if db.execute_query(query, (username, pin_hash)):
            QMessageBox.information(self, "Success", "Account created successfully! Please login.")
            self.username_input.clear()
            self.pin_input.clear()
        else:
            QMessageBox.critical(self, "Error", "Failed to create account")
    
    def get_styles(self):
        """Get stylesheet"""
        return """
            QDialog {
                background-color: #f5f5f5;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 11pt;
            }
            QLineEdit:focus {
                border: 2px solid """ + PRIMARY_COLOR + """;
            }
            QLabel {
                font-weight: bold;
            }
            QPushButton {
                padding: 8px;
                border-radius: 4px;
                border: 1px solid #ddd;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """
