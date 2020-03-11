from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My wondeful store',
        'items': [
            {
                'name': 'First item',
                'price': 19.99
            },
            {
                'name': 'Second item',
                'price': 15.00
            }
        ]
    }
]


# GET WELCOME ROUTE
@app.route('/', methods=['GET'])
def home():
    return "HELLO WORLD2"


# GET STORES LIST ROUTE
@app.route('/stores', methods=['GET', 'POST'])
def stores_index():
    return jsonify({
        'stores': stores
    })


# POST STORE NEW STORE ROUTE
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)


# GET SEPECIFIC STORE
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({
        'message': 'store not found'
    })


# GET ITEMS OF STORE
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
    for store in stores:
        if stores['name'] == name:
            return jsonify({
                'items': store['items']
            })
    return jsonify({
        'message': 'store not found'
    })


# POST STORE NEW ITEM IN STORE
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({
        'message': 'store not found'
    })


app.run(port=5000)
