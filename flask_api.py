from flask import Flask, jsonify, request
from db_utils import view_all_books_db, view_latest_book_db, add_new_book_db

app = Flask(__name__)


# Views all books from database
@app.route("/books", methods=["GET"])
def view_all_books_api():
    return jsonify(view_all_books_db())


# Views latest book from database
@app.route("/books/current", methods=["GET"])
def view_latest_book_api():
    return jsonify(view_latest_book_db())

# Adds new book to database
@app.route("/books/add", methods=["POST"])
def add_new_book_api():
    new_book = request.get_json()
    return jsonify(add_new_book_db(new_book))