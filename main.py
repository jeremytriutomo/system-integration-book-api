from flask import Flask, jsonify, request

app = Flask(__name__)

books = {
    "Book_001": {
        "title": "The Skin That We Speak",
        "author": "Lisa Delpit",
        "publisher": "The New Press",
        "year": 2006,
        "genre": "Education",
        "stock": 4
    },

    "Book_002": {
        "title": "Pedagogy of the Oppressed",
        "author": "Paulo Freire",
        "publisher": "Continuum",
        "year": 1970,
        "genre": "Education",
        "stock": 7
    },

    "Book_003": {
        "title": "The Power of Habit",
        "author": "Charles Duhigg",
        "publisher": "Random House",
        "year": 2012,
        "genre": "Psychology",
        "stock": 10
    },

    "Book_004": {
        "title": "Thinking, Fast and Slow",
        "author": "Daniel Kahneman",
        "publisher": "Farrar, Straus and Giroux",
        "year": 2011,
        "genre": "Cognitive Science",
        "stock": 9
    },

    "Book_005": {
        "title": "How to Read a Book",
        "author": "Mortimer J. Adler",
        "publisher": "Simon & Schuster",
        "year": 1940,
        "genre": "Education",
        "stock": 12
    },

    "Book_006": {
        "title": "Outliers",
        "author": "Malcolm Gladwell",
        "publisher": "Little, Brown and Company",
        "year": 2008,
        "genre": "Sociology",
        "stock": 6
    }
}


@app.route('/books/<string:book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if book:
        return jsonify(book), 200
    else:
        return jsonify({"error": "Book not found"}), 404


@app.route('/books/add/<string:book_id>', methods=['POST'])
def add_book(book_id):
    if book_id in books:
        return jsonify({"error": "Book ID is taken"}), 409

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}), 400

    required_fields = [
        "title",
        "author",
        "publisher",
        "year",
        "genre",
        "stock"
    ]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields in input"}), 400

    books[book_id] = {
        "title": data["title"],
        "author": data["author"],
        "publisher": data["publisher"],
        "year": data["year"],
        "genre": data["genre"],
        "stock": data["stock"]
    }

    return jsonify({"message": "Book added", "book": books[book_id]}), 201


@app.route('/books/delete/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id in books:
        del books[book_id]
        return jsonify({"message": "Book deleted"}), 200
    else:
        return jsonify({"error": "Book not found"}), 404


@app.route('/books/update-stock/<string:book_id>/<int:new_stock>', methods=['PUT'])
def update_stock(book_id, new_stock):
    if book_id not in books:
        return jsonify({"error": "Book not found"}), 404

    # Update only stock
    books[book_id]["stock"] = new_stock

    return jsonify({
        "message": "Stock updated successfully",
        "book_id": book_id,
        "new_stock": new_stock
    }), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
