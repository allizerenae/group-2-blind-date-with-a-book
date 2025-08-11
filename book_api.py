import requests
import random
import itertools

GENRES = ['horror', 'comedy', 'romance']


def get_random_genre():
    """Function to get a random genre using itertools.islice"""
    shuffled = random.sample(GENRES, len(GENRES))
    return next(itertools.islice(shuffled, 1))


def get_random_book_by_genre(subject):
    """Function to get a random book based on a user chosen genre"""

    # Gets total number of books in chosen genre
    subject = subject.strip().lower()
    url = f"https://openlibrary.org/subjects/{subject}.json?languages=eng"
    response = requests.get(url)

    if response.status_code != 200:
        return {'error': 'Genre not found or API error'}

    total_books = response.json().get('work_count', 0)
    if total_books == 0:
        return {'error': 'No books found in this genre'}

    # Choose a random selection
    max_selection = max(0, total_books - 1)
    selection = random.randint(0, max_selection)

    # Get a book data
    book_url = f"{url}&limit=1&offset={selection}"
    book_response = requests.get(book_url)
    book_data = book_response.json().get('works', [])

    if not book_data:
        return {'error': 'No books found'}

    book = book_data[0]
    title = book.get('title')
    author = None
    if book.get('authors'):
        author = book['authors'][0].get('name')

    return {
        'title': title,
        'author': author,
        'genre': subject,
    }

