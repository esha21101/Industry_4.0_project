from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated databases
orders = []
feedbacks = []

@app.route('/order', methods=['POST'])
def order_part():
    data = request.json
    part_id = data.get('part_id')
    quantity = data.get('quantity')
    order = {"part_id": part_id, "quantity": quantity, "status": "ordered"}
    orders.append(order)
    return jsonify({"message": f"Order placed for {quantity} of Part ID {part_id}", "orders": orders})

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    feedback = data.get('feedback')
    feedbacks.append(feedback)
    return jsonify({"message": "Feedback recorded", "feedbacks": feedbacks})

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({"orders": orders})

@app.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    return jsonify({"feedbacks": feedbacks})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
