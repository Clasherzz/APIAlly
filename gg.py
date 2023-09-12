import requests
movie_title = input("Enter a movie title: ")

# Send a GET request to the Flask API to retrieve movie data
response = requests.get(f'http://127.0.0.1:5000/api/movies/{movie_title}')

# Check the response status code
if response.status_code == 200:
    movie_data = response.json()
    print("Movie Data:")
    print(movie_data)
elif response.status_code == 404:
    print("Movie not found.")
else:
    print("Error fetching movie data.")
