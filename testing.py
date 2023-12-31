import requests
from main.py import user_topic


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
inputp='STRING'
d_ata=None
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
        response = requests.get(f'http://127.0.0.1:5000/api/{user_topic}/'+self.text_input.text)

# Check the response status code
        global d_ata
        if response.status_code == 200:

             d_ata = response.json()
             print("Movie Data:")
             print(d_ata)
        elif response.status_code == 404:
             print("Movie not found.")
        else:
             print("Error fetching movie data.")

        if self.text_input.text:
            input_text = self.text_input.text
            self.display_label.text = f'You entered: {d_ata}'
TextInputApp().run()
