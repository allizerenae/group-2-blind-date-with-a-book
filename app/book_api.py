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
    if subject == "random":
        subject = get_random_genre()

    url = f"https://openlibrary.org/subjects/{subject}.json?languages=eng" # Url to return only books in English

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return {'ERROR': 'Network or API error'}

    total_books = response.json().get('work_count', 0)
    if total_books == 0:
        return {'ERROR': 'No books found in this genre'}

    # Choose a random selection
    selection = random.randint(0, max(0, total_books - 1))
    # Get book data
    book_url = f"{url}&limit=1&offset={selection}"

    try:
        book_response = requests.get(book_url, timeout=10)
        book_response.raise_for_status()
    except requests.RequestException:
        return {'ERROR': 'Network or API error'}

    book_data = book_response.json().get('works', [])
    if not book_data:
        return {'ERROR': 'No books found'}

    book = book_data[0]
    title = book.get('title', 'Unknown Title')
    author = "Unknown Author"
    if book.get('authors'):
        author = book['authors'][0].get('name', "Unknown Author")

    return {
        'title': title,
        'author': author,
        'genre': subject,
    }


if __name__ == '__main__':
    print("=== TESTING ===")
    print(get_random_book_by_genre("random"))




