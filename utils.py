# Utility Functions

import hashlib
from datetime import datetime

def hash_pin(pin):
    """Hash PIN for security"""
    return hashlib.sha256(pin.encode()).hexdigest()

def verify_pin(pin, pin_hash):
    """Verify PIN against hash"""
    return hash_pin(pin) == pin_hash

def format_date(date_obj):
    """Format date for display"""
    if isinstance(date_obj, str):
        return date_obj
    return date_obj.strftime("%d-%m-%Y") if date_obj else ""

def format_amount(amount):
    """Format amount for display"""
    try:
        return f"₹ {float(amount):,.2f}"
    except:
        return "₹ 0.00"

def get_today_date():
    """Get today's date"""
    return datetime.now().strftime("%Y-%m-%d")

def get_current_datetime():
    """Get current datetime"""
    return datetime.now()

def validate_email(email):
    """Simple email validation"""
    return "@" in email and "." in email

def validate_phone(phone):
    """Simple phone validation"""
    return len(phone) >= 10 and phone.isdigit()

class ValidationError(Exception):
    """Custom validation error"""
    pass

def validate_ledger_name(name):
    """Validate ledger name"""
    if not name or len(name) < 2:
        raise ValidationError("Ledger name must be at least 2 characters")
    if len(name) > 100:
        raise ValidationError("Ledger name must not exceed 100 characters")
    return True

def validate_party_name(name):
    """Validate party name"""
    if not name or len(name) < 2:
        raise ValidationError("Party name must be at least 2 characters")
    if len(name) > 100:
        raise ValidationError("Party name must not exceed 100 characters")
    return True

def validate_amount(amount):
    """Validate transaction amount"""
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValidationError("Amount must be greater than 0")
        return amount
    except ValueError:
        raise ValidationError("Invalid amount")
