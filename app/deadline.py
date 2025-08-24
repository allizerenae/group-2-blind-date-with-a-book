from datetime import date, timedelta

#gets today's date
def get_assigned_date():
    current_date = date.today()
    return current_date

#gets the reading deadline date
def get_deadline():
    book_deadline = date.today() + timedelta(days=7)
    return book_deadline

#if __name__ == "__main__":
    #manual testing
    #print(get_deadline() - get_assigned_date())
