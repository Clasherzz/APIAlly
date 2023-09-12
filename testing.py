
# from flask import Flask, jsonify, request
#
# # Create a Flask app
# app = Flask(__name__)
#
# # Sample movie data (in-memory database)
# movies_data = {
#     'Movie A': {
#         'title': 'Movie A',
#         'release_year': 2020,
#         'director': 'Director A',
#         'genre': 'Action',
#     },
#     'Movie B': {
#         'title': 'Movie B',
#         'release_year': 2018,
#         'director': 'Director B',
#         'genre': 'Comedy',
#     },
#     'Movie C': {
#         'title': 'Movie C',
#         'release_year': 2019,
#         'director': 'Director C',
#         'genre': 'Drama',
#     },
#     # Add more movie data as needed
# }
#
# # Define an endpoint to retrieve all movie data
# @app.route('/api/movies', methods=['GET'])
# def get_all_movies():
#     return jsonify(movies_data)
#
# # Define an endpoint to retrieve movie data by title
# @app.route('/api/movies/<string:title>', methods=['GET'])
# def get_movie_by_title(title):
#     movie = movies_data.get(title)
#     if movie:
#         return jsonify(movie)
#     else:
#         return jsonify({'message': 'Movie not found'}), 404
#
# if __name__ == '__main__':
#     app.run(debug=True)

# User input for the movie title

import requests


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
inputp='STRING'
movie_data=None
temp=None
class TextInputApp(App):


    def build(self):
        # Create a BoxLayout to hold the UI elements vertically
        Window.clearcolor = (0.7, 0.7, 1, 1)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Add a label to the layout
        label = Label(text=f'Enter {inputp}:')
        layout.add_widget(label)

        # Add a text input field to the layout
        self.text_input = TextInput(multiline=False)
        layout.add_widget(self.text_input)
        # movie_title = input("Enter a movie title: ")
        # print(self.text_input.text)
# Create a label to display the input
        self.display_label = Label(text='')
        layout.add_widget(self.display_label)

        # Create a button to submit the input
        submit_button = Label(text='Submit')
        submit_button.bind(on_touch_down=self.on_submit)
        layout.add_widget(submit_button)



        return layout


    def on_submit(self, instance, touch):
        # Send a GET request to the Flask API to retrieve movie data
        response = requests.get('http://127.0.0.1:5000/api/movies/'+self.text_input.text)

# Check the response status code
        global movie_data
        if response.status_code == 200:

             movie_data = response.json()
             print("Movie Data:")
             print(movie_data)
        elif response.status_code == 404:
             print("Movie not found.")
        else:
             print("Error fetching movie data.")

        if self.text_input.text:
            input_text = self.text_input.text
            self.display_label.text = f'You entered: {movie_data}'

if __name__ == '__main__':
    TextInputApp().run()
