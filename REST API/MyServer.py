import json
from flask import Flask, jsonify, request
app = Flask(__name__)

order =[]

@app.route('/order', methods=['GET'])
def get_order():
    return jsonify(order)

@app.route('/order', methods=['POST'])
def create_order():
    order.append(json.loads(request.data))
    return '', 201, { 'location': f'/order/{order[-1]["id"]}' }

def get_order(id):
 return next((e for e in order if e['id'] == id), None)

@app.route('/order/<int:id>', methods=['GET'])
def get_employee_by_id(id: int):
 order = get_order(id)
 if order is None:
   return jsonify({ 'error': 'order does not exist'}), 404
 return jsonify(order)

@app.route('/order/<int:id>', methods=['PUT'])
def update_order_status(id: int):
 order = get_order(id)
 if order is None:
   return jsonify({ 'error': 'order does not exist.' }), 404

 updated_order = json.loads(request.data)

 order.update(updated_order)

 return jsonify(order), 200

if __name__ == '__main__':
    app.run(port=5000)