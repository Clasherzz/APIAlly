from flask import Flask, jsonify

# Create a Flask app
app = Flask(__name__)

# Sample data (in-memory database)

animals_data = {
    '1': {
        'name': 'Lion',
        'species': 'Panthera leo',
        'habitat': 'Savannah',
        'average_lifespan': 10-14 years (wild),
        'diet': 'Carnivore',
    },
    '2': {
        'name': 'Elephant',
        'species': 'Loxodonta africana',
        'habitat': 'Grasslands, forests',
        'average_lifespan': 60-70 years (wild),
        'diet': 'Herbivore',
    },
    '3': {
        'name': 'Dolphin',
        'species': 'Delphinidae',
        'habitat': 'Oceans',
        'average_lifespan': 25 years (wild),
        'diet': 'Carnivore (fish)',
    },
    '4': {
        'name': 'Panda',
        'species': 'Ailuropoda melanoleuca',
        'habitat': 'Bamboo forests',
        'average_lifespan': 20 years (wild),
        'diet': 'Herbivore (mainly bamboo)',
    },
    '5': {
        'name': 'Tiger',
        'species': 'Panthera tigris',
        'habitat': 'Grasslands, forests',
        'average_lifespan': 10-15 years (wild),
        'diet': 'Carnivore (deer, boar, etc.)',
    },
    '6': {
        'name': 'Kangaroo',
        'species': 'Macropus',
        'habitat': 'Australia',
        'average_lifespan': 6-8 years (wild),
        'diet': 'Herbivore (grasses, plants)',
    },
    '7': {
        'name': 'Giraffe',
        'species': 'Giraffa camelopardalis',
        'habitat': 'African savannahs',
        'average_lifespan': 25 years (wild),
        'diet': 'Herbivore (leaves, twigs)',
    },
    '8': {
        'name': 'Humpback Whale',
        'species': 'Megaptera novaeangliae',
        'habitat': 'Oceans',
        'average_lifespan': 45-50 years (wild),
        'diet': 'Carnivore (krill, fish)',
    },
    '9': {
        'name': 'Red Fox',
        'species': 'Vulpes vulpes',
        'habitat': 'Various habitats',
        'average_lifespan': 3-4 years (wild),
        'diet': 'Omnivore (small mammals, fruits)',
    },
    '10': {
        'name': 'Bald Eagle',
        'species': 'Haliaeetus leucocephalus',
        'habitat': 'North America',
        'average_lifespan': 20-30 years (wild),
        'diet': 'Carnivore (fish, waterfowl)',
    }
}


# Define an endpoint to retrieve all data
@app.route('/api/animals', methods=['GET'])
def get_all_data():
    return jsonify(data)

# Define an endpoint to retrieve data by ID
@app.route('/api/data/<string:id>', methods=['GET'])
def get_data_by_id(id):
    if id in data:
        return jsonify(data[id])
    else:
        return jsonify({'message': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
