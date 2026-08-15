from datetime import datetime

def current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def format_date(date_string):
    try:
        return datetime.strptime(date_string, '%Y-%m-%d').strftime('%d %b %Y')
    except:
        return date_string

def success_response(message, data=None):
    return {
        'success': True,
        'message': message,
        'data': data
    }

def error_response(message):
    return {
        'success': False,
        'message': message
    }

def volunteer_status_color(status):
    if status == 'Active':
        return 'green'
    elif status == 'Inactive':
        return 'red'
    return 'gray'
