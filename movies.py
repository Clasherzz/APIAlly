
from flask import Flask, jsonify, request

# Create a Flask app
app = Flask(__name__)

# Sample movie data (in-memory database)
movies_data = {
    'Movie A': {
        'title': 'Movie A',
        'release_year': 2020,
        'director': 'Director A',
        'genre': 'Action',
    },
    'Movie B': {
        'title': 'Movie B',
        'release_year': 2018,
        'director': 'Director B',
        'genre': 'Comedy',
    },
    'Movie C': {
        'title': 'Movie C',
        'release_year': 2019,
        'director': 'Director C',
        'genre': 'Drama',
    },
    # Add more movie data as needed
}

# Define an endpoint to retrieve all movie data
@app.route('/api/movies', methods=['GET'])
def get_all_movies():
    return jsonify(movies_data)

# Define an endpoint to retrieve movie data by title
@app.route('/api/movies/<string:title>', methods=['GET'])
def get_movie_by_title(title):
    movie = movies_data.get(title)
    if movie:
        return jsonify(movie)
    else:
        return jsonify({'message': 'Movie not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

# User input for the movie title

