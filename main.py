

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

