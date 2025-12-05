Book Inventory REST API (Flask)

This project provides a simple RESTful API for managing a collection of books.
It allows users to retrieve, add, update, and delete books from inventory.
The API is built using Flask and stores data in-memory using a Python dictionary.

Setup Instructions
------------------

1. Clone the Repository:
git clone https://github.com/jeremytriutomo/system-integration-book-api.git
cd system-integration-book-api

2. Install Dependencies:
pip install flask

3. Run the Application:
python app.py

The API will start at:
http://127.0.0.1:5000

API Endpoints
-------------

GET /books/<book_id>
    Retrieve a book by its ID.

POST /books/add/<book_id>
    Add a new book (requires JSON body).

DELETE /books/delete/<book_id>
    Delete a book by its ID.

PUT /books/update-stock/<book_id>/<new_stock>
    Update the stock count of a book.

Request Body Example for Adding a Book
--------------------------------------

{
  "title": "Sample Book",
  "author": "John Doe",
  "publisher": "Example Press",
  "year": 2024,
  "genre": "Fiction",
  "stock": 5
}

Example API Calls (cURL)
------------------------

# Get a Book
curl -i http://127.0.0.1:5000/books/Book_001

# Add a New Book
curl -i -X POST http://127.0.0.1:5000/books/add/Book_100 \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Code","author":"Robert C. Martin","publisher":"Prentice Hall","year":2008,"genre":"Software","stock":5}'

# Update Stock
curl -i -X PUT http://127.0.0.1:5000/books/update-stock/Book_100/12

# Delete a Book
curl -i -X DELETE http://127.0.0.1:5000/books/delete/Book_100


Limitations
-----------

- Data is not saved permanently; restarting the server resets the inventory.
- No user authentication included.
- Intended for educational and prototyping use.

