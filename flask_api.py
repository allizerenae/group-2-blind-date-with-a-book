from flask import Flask, jsonify, request
from db_utils import view_all_books_db, view_latest_book_db, add_new_book_db

app = Flask(__name__)


@app.route("/books", methods=["GET"])
def view_all_books_api():
    return jsonify(view_all_books_db())


@app.route("/books/current", methods=["GET"])
def view_latest_book_api():
    return jsonify(view_latest_book_db())


@app.route("/books/add", methods=["POST"])
def add_new_book_api():
    new_book = request.get_json()
    return jsonify(add_new_book_db(new_book))


# Stub for testing API from main.py
def mock_get_random_book_by_genre(genre):
    return {"title": "Mock Book Title", "author": "Mock Author"}

if __name__ == "__main__":
    app.run(debug=True)

