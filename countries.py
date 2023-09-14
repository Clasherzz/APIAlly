from flask import Flask, jsonify

# Create a Flask app
app = Flask(__name__)

# Sample data (in-memory database)
countries_data = {
    '1': {
        'name': 'United States',
        'capital': 'Washington, D.C.',
        'population': 331002651,
        'currency': 'United States Dollar (USD)',
        'language': 'English',
    },
    '2': {
        'name': 'United Kingdom',
        'capital': 'London',
        'population': 67886011,
        'currency': 'Pound Sterling (GBP)',
        'language': 'English',
    },
    '3': {
        'name': 'France',
        'capital': 'Paris',
        'population': 65273511,
        'currency': 'Euro (EUR)',
        'language': 'French',
    },
    '4': {
        'name': 'India',
        'capital': 'New Delhi',
        'population': 1380004385,
        'currency': 'Indian Rupee (INR)',
        'language': 'Hindi, English',
    },
    '5': {
        'name': 'Japan',
        'capital': 'Tokyo',
        'population': 126476461,
        'currency': 'Japanese Yen (JPY)',
        'language': 'Japanese',
    },
    '6': {
        'name': 'Brazil',
        'capital': 'Brasília',
        'population': 212559417,
        'currency': 'Brazilian Real (BRL)',
        'language': 'Portuguese',
    },
    '7': {
        'name': 'Australia',
        'capital': 'Canberra',
        'population': 25499884,
        'currency': 'Australian Dollar (AUD)',
        'language': 'English',
    },
    '8': {
        'name': 'Canada',
        'capital': 'Ottawa',
        'population': 37742154,
        'currency': 'Canadian Dollar (CAD)',
        'language': 'English, French',
    },
    '9': {
        'name': 'China',
        'capital': 'Beijing',
        'population': 1444216107,
        'currency': 'Chinese Yuan (CNY)',
        'language': 'Mandarin',
    },
    '10': {
        'name': 'Russia',
        'capital': 'Moscow',
        'population': 145934462,
        'currency': 'Russian Ruble (RUB)',
        'language': 'Russian',
    }
}


# Define an endpoint to retrieve all data
@app.route('/api/countries', methods=['GET'])
def get_all_data():
    return jsonify(countries_data)

# Define an endpoint to retrieve data by ID
@app.route('/api/data/<string:id>', methods=['GET'])
def get_data_by_id(name):
    country=countries_data.get(name)
    if country:
        return jsonify(country)
    else:
        return jsonify({'message': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
