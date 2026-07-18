# Main Application Entry Point

import sys
from PyQt5.QtWidgets import QApplication
from login import LoginWindow
from dashboard import Dashboard
from database import db

def main():
    app = QApplication(sys.argv)
    
    # Show login window
    login_window = LoginWindow()
    if login_window.exec_() == 1:  # Accepted
        # Open dashboard
        user_id = login_window.user_id
        dashboard = Dashboard(user_id)
        dashboard.show()
        sys.exit(app.exec_())
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
