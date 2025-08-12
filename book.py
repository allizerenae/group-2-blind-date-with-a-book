class Book:
    def __init__(self, title, author, genre, assigned_date, deadline=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.assigned_date = assigned_date
        self.deadline = deadline

    def to_dict(self):
        """Convert Book object to dictionary for DB insertion."""
        return {
            "book_title": self.title,
            "author": self.author,
            "genre": self.genre,
            "assigned_date": self.assigned_date,
            "deadline": self.deadline
        }

    def __str__(self):
        deadline_str = self.deadline if self.deadline else "No deadline set"
        return f"'{self.title}' by {self.author} ({self.genre}) — Assigned: {self.assigned_date}, Deadline: {deadline_str}"
