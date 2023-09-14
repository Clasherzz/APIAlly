from flask import Flask, jsonify

# Create a Flask app
app = Flask(__name__)

# Sample data (in-memory database)

books_data = {
    '1': {
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'genre': 'Fiction',
        'year_published': 1960,
        'isbn': '978-0-06-112008-4',
    },
    '2': {
        'title': '1984',
        'author': 'George Orwell',
        'genre': 'Dystopian Fiction',
        'year_published': 1949,
        'isbn': '978-0-452-28423-4',
    },
    '3': {
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'genre': 'Romance',
        'year_published': 1813,
        'isbn': '978-1-85326-000-0',
    },
    '4': {
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'genre': 'Classics',
        'year_published': 1925,
        'isbn': '978-0-7432-7356-5',
    },
    '5': {
        'title': 'Harry Potter and the Sorcerer\'s Stone',
        'author': 'J.K. Rowling',
        'genre': 'Fantasy',
        'year_published': 1997,
        'isbn': '978-0-590-35340-3',
    },
    '6': {
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger',
        'genre': 'Coming-of-Age',
        'year_published': 1951,
        'isbn': '978-0-316-76948-0',
    },
    '7': {
        'title': 'The Hobbit',
        'author': 'J.R.R. Tolkien',
        'genre': 'Fantasy',
        'year_published': 1937,
        'isbn': '978-0-261-10295-6',
    },
    '8': {
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'genre': 'Young Adult',
        'year_published': 2008,
        'isbn': '978-0-439-02352-8',
    },
    '9': {
        'title': 'Brave New World',
        'author': 'Aldous Huxley',
        'genre': 'Science Fiction',
        'year_published': 1932,
        'isbn': '978-0-06-085052-4',
    },
    '10': {
        'title': 'The Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'genre': 'Fantasy',
        'year_published': 1954,
        'isbn': '978-0-618-34625-0',
    }
}


# Define an endpoint to retrieve all data
@app.route('/api/books', methods=['GET'])
def get_all_data():
    return jsonify(books_data)

# Define an endpoint to retrieve data by ID
@app.route('/api/data/<string:id>', methods=['GET'])
def get_data_by_id(title):
    book=books_data.get(title)
    if book:
        return jsonify(book)
    else:
        return jsonify({'message': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
