from flask import Flask, jsonify

# Create a Flask app
app = Flask(__name__)

# Sample data (in-memory database)
plants_data = {
    '1': {
        'name': 'Rose',
        'species': 'Rosa',
        'habitat': 'Gardens, temperate regions',
        'blooming_season': 'Spring to early summer',
        'average_lifespan': 'Several years to decades',
    },
    '2': {
        'name': 'Oak Tree',
        'species': 'Quercus',
        'habitat': 'Forests, woodlands',
        'blooming_season': 'Spring',
        'average_lifespan': 'Centuries',
    },
    '3': {
        'name': 'Sunflower',
        'species': 'Helianthus',
        'habitat': 'Fields, gardens',
        'blooming_season': 'Summer to early autumn',
        'average_lifespan': 'One season (annual)',
    },
    '4': {
        'name': 'Cactus',
        'species': 'Cactaceae',
        'habitat': 'Deserts, arid regions',
        'blooming_season': 'Varies by species',
        'average_lifespan': 'Decades to centuries',
    },
    '5': {
        'name': 'Fern',
        'species': 'Pteridophyta',
        'habitat': 'Forests, wetlands',
        'blooming_season': 'N/A (reproduces via spores)',
        'average_lifespan': 'Several years to decades',
    },
    '6': {
        'name': 'Tulip',
        'species': 'Tulipa',
        'habitat': 'Gardens, temperate regions',
        'blooming_season': 'Spring',
        'average_lifespan': 'Several years (perennial)',
    },
    '7': {
        'name': 'Pine Tree',
        'species': 'Pinus',
        'habitat': 'Forests, mountains',
        'blooming_season': 'Varies by species',
        'average_lifespan': 'Centuries',
    },
    '8': {
        'name': 'Daisy',
        'species': 'Bellis perennis',
        'habitat': 'Gardens, meadows',
        'blooming_season': 'Spring to early summer',
        'average_lifespan': 'Several years (perennial)',
    },
    '9': {
        'name': 'Bamboo',
        'species': 'Bambusoideae',
        'habitat': 'Asian forests, grasslands',
        'blooming_season': 'Infrequent and varies',
        'average_lifespan': 'Decades to centuries',
    },
    '10': {
        'name': 'Lavender',
        'species': 'Lavandula',
        'habitat': 'Gardens, Mediterranean regions',
        'blooming_season': 'Late spring to summer',
        'average_lifespan': 'Several years (perennial)',
    }
}



# Define an endpoint to retrieve all data
@app.route('/api/plants', methods=['GET'])
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
