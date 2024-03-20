from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello, World! This is a GET request.'

@app.route('/data', methods=['POST'])
def post_data():
    data = request.json
    # Do something with the received data
    return jsonify({'message': 'Data received successfully!', 'data': data}), 201

@app.route('/update/<int:id>', methods=['PUT'])
def update_data(id):
    # Assuming we have some data stored and we're updating it
    # Here, I'm just returning a message for demonstration
    return jsonify({'message': f'Data with id {id} updated successfully!'})

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_data(id):
    # Assuming we have some data stored and we're deleting it
    # Here, I'm just returning a message for demonstration
    return jsonify({'message': f'Data with id {id} deleted successfully!'}), 204

if __name__ == '__main__':
    app.run(debug=True)
