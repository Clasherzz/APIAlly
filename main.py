# Sample API database (for demonstration purposes)
import requests
api_database = [
    {"name": "Weather API", "topic": "movies"},
    {"name": "News API", "topic": "countries"},
    {"name": "Stock API", "topic": "plants"},
    {},
    {},
    # Add more APIs and topics here
]

def recommend_apis(user_topic):
    recommended_apis = []

    # Simulated API recommendation logic (matching topic)
    for api in api_database:
        if user_topic.lower() in api["topic"].lower():
            recommended_apis.append(api["name"])

    return recommended_apis

# Main function
def main():
    user_topic = input("Enter a topic: ")
    recommended_apis = recommend_apis(user_topic)

    if recommended_apis:
        print("Recommended APIs:")
        for api in recommended_apis:
            print(api)
    else:
        print("No APIs found for the given topic.")

# if __name__ == "__main__":
#     main()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class TextInputApp(App):
    def

    def build(self):
        # Create a BoxLayout to hold the UI elements vertically
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Add a label to the layout
        label = Label(text='Enter a string:')
        layout.add_widget(label)

        # Add a text input field to the layout
        self.text_input = TextInput(multiline=False)
        layout.add_widget(self.text_input)

        # Create a button to submit the input
        submit_button = Label(text='Submit')
        submit_button.bind(on_touch_down=self.on_submit)
        layout.add_widget(submit_button)

        # Create a label to display the input
        self.display_label = Label(text='')
        layout.add_widget(self.display_label)

        return layout

    def on_submit(self, instance, touch):
        if self.text_input.text:
            input_text = self.text_input.text
            self.display_label.text = f'You entered: {input_text}'

if __name__ == '__main__':
    TextInputApp().run()




    # Define the base URL of the Flask API
base_url = "http://127.0.0.1:5000"  # Replace with the actual API URL if hosted elsewhere

# Function to retrieve user data by ID
def get_user_data(user_id):
    endpoint = f"/api/data/{user_id}"
    url = f"{base_url}{endpoint}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {'message': 'Data not found'}

# User input to select a user (1 or 2)
user_input = input("Enter user ID (1 or 2): ")


user_data = get_user_data(user_input)
print("User Data:")
print(user_data)

# Sample API database (for demonstration purposes)

import subprocess
user_topic=None
api_database = [
    {"name": "movies.py", "topic": "movies"},
    {"name": "countries.py", "topic": "countries"},
    {"name": "plants.py", "topic": "plants"},
    {"name": "animals.py", "topic": "animals"},
    {"name": "books.py", "topic": "books"},
    # Add more APIs and topics here
]

def recommend_apis(user_topic):
    recommended_apis = []

    # Simulated API recommendation logic (matching topic)
    for api in api_database:
        if user_topic.lower() in api["topic"].lower():
            recommended_apis.append(api["name"])
            subprocess.run(['python',api['name']])

    return recommended_apis

# Main function
def main():
    global user_topic
    user_topic = input("Enter a topic: ")
    recommended_apis = recommend_apis(user_topic)

    if recommended_apis:
        print("Recommended APIs:")
        for api in recommended_apis:
            print(api)
    else:
        print("No APIs found for the given topic.")




# Replace 'script_to_run.py' with the name of the Python file you want to run.
subprocess.run(['python', 'testing.py'])

if __name__ == "__main__":
    main()

