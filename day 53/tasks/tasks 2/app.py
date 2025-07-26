from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/time')
def api_time():
    from datetime import datetime
    return jsonify({"time": datetime.now().strftime("%H:%M:%S")})

@app.route('/api/users')
def api_users():
    users = [
        {"id": 1, "name": "Arivu"},
        {"id": 2, "name": "Vani"},
        {"id": 3, "name": "Ravi"}
    ]
    return jsonify(users)

@app.route('/api/products')
def api_products():
    products = [
        {"name": "Laptop", "price": 50000},
        {"name": "Mouse", "price": 500},
        {"name": "Keyboard", "price": 1000}
    ]
    return jsonify(products)

@app.route('/api/submit', methods=['POST'])
def api_submit():
    data = request.get_json()
    return jsonify({"message": f"Received: {data.get('input')}"})

@app.route('/api/put-example', methods=['PUT'])
def api_put():
    data = request.get_json()
    return jsonify({"status": "updated", "data": data})

@app.route('/api/random')
def api_random():
    import random
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the computer go to therapy? It had too many bytes!",
        "404 joke not found!"
    ]
    return jsonify({"joke": random.choice(jokes)})

@app.route('/api/status')
def api_status():
    return jsonify({"status": "running", "uptime": "2 hours", "app_version": "1.0.0"})

@app.route('/api/search')
def api_search():
    q = request.args.get('q', '').lower()
    names = ["Arivu", "Vani", "Ravi", "Priya"]
    matches = [name for name in names if q in name.lower()]
    return jsonify(matches)

if __name__ == '__main__':
    app.run(debug=True)
