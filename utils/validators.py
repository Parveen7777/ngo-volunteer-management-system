import re

def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, phone) is not None

def validate_required(value):
    return value is not None and str(value).strip() != ''

def validate_volunteer_data(data):
    errors = []

    if not validate_required(data.get('name')):
        errors.append('Name is required')

    if not validate_email(data.get('email', '')):
        errors.append('Valid email is required')

    if not validate_phone(data.get('phone', '')):
        errors.append('Valid 10-digit phone number is required')

    return errors
