from datetime import date, timedelta


def get_assigned_date():
    current_date = date.today()
    return current_date


def get_deadline():
    book_deadline = date.today() + timedelta(days=7)
    return book_deadline
