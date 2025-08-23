from flask import Flask, jsonify, request
from app.db_utils import view_all_books_db, view_latest_book_db, add_new_book_db

app = Flask(__name__)

# This file utilises Flask to create endpoints that interact with the database


@app.route("/books", methods=["GET"])
def view_all_books_api():
    return jsonify(view_all_books_db())


@app.route("/books/current", methods=["GET"])
def view_latest_book_api():
    return jsonify(view_latest_book_db())


@app.route("/books/add", methods=["POST"])
def add_new_book_api():
    new_book_dict = request.get_json()
    return jsonify(add_new_book_db(new_book_dict))


if __name__ == "__main__":
    app.run(debug=True)

