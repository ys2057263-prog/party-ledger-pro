# Party Ledger Pro - Windows Desktop Application

A professional-grade party ledger management application built with Python and PyQt5.

## Features

### Phase 1 - Core Features ✅
- **Login System**: PIN-based authentication with user signup
- **Multiple Ledgers**: Create and manage multiple ledgers
- **Party Management**: Add, edit, and delete parties
- **Transaction Entry**: Quick entry for credit/debit transactions
- **Dashboard**: Real-time balance, party count, and recent transactions
- **Ledger Operations**: Rename and delete ledgers

### Phase 2 - Coming Soon 🔜
- Reports (Daily, Monthly, Party-wise)
- PDF & Excel Export
- Backup & Restore
- Settings & PIN Management
- Dark Mode
- Charts & Analytics

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/ys2057263-prog/party-ledger-pro.git
cd party-ledger-pro
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python main.py
```

## Usage

### First Time Setup
1. Launch the application
2. Click "Sign Up"
3. Enter username (minimum 3 characters)
4. Enter 4-digit PIN
5. Click "Sign Up" to create account

### Login
1. Enter your username
2. Enter your 4-digit PIN
3. Click "Login"

### Creating a Ledger
1. From the left sidebar, click "➕ New Ledger"
2. Enter ledger name
3. Optionally add description
4. Click "Create"

### Adding a Party
1. Select a ledger from the dropdown
2. Go to "👥 Parties" tab
3. Click "➕ Add Party"
4. Fill in party details
5. Click "Add"

### Adding Transactions
1. Go to "📝 Entries" tab
2. Select party from dropdown
3. Choose transaction type (Credit/Debit)
4. Enter amount
5. Select date
6. Click "➕ Add"

## Project Structure

```
party-ledger-pro/
├── main.py              # Application entry point
├── config.py            # Configuration settings
├── database.py          # Database management
├── utils.py             # Utility functions
├── login.py             # Login interface
├── dashboard.py         # Main dashboard interface
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── database/           # Database files (created at runtime)
```

## Database Schema

### Users
- id, username, pin_hash, created_at, last_login

### Ledgers
- id, user_id, name, description, created_at, updated_at

### Parties
- id, ledger_id, name, phone, email, address, created_at, updated_at

### Transactions
- id, ledger_id, party_id, type, amount, date, remark, created_at

### Settings
- id, user_id, key, value

### Backup History
- id, user_id, backup_path, backup_date, file_size

## Security Features

- PIN-based authentication (4-digit)
- SHA256 password hashing
- SQLite database with encryption support (planned)
- Auto-lock after inactivity (planned)

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Style
This project follows PEP 8 style guide.

## Roadmap

- [x] Login & Authentication
- [x] Ledger Management
- [x] Party Management
- [x] Transaction Entry
- [ ] Reports Generation
- [ ] PDF Export
- [ ] Excel Export
- [ ] Backup & Restore
- [ ] Dark Mode
- [ ] Mobile App (Flutter)

## Known Issues

- Reports feature in development
- Backup/Restore not yet implemented
- Settings page not yet implemented

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Created by ys2057263-prog

## Support

For support, please create an issue on GitHub.

---

**Version**: 1.0.0  
**Last Updated**: 2024
