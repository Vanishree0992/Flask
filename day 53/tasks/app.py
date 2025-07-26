from flask import Flask, jsonify, request, make_response
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "Arivu", "email": "arivu@example.com"},
    {"id": 2, "name": "Vani", "email": "vani@example.com"},
    {"id": 3, "name": "Kumar", "email": "kumar@example.com"},
    {"id": 4, "name": "Ravi", "email": "ravi@example.com"},
    {"id": 5, "name": "Priya", "email": "priya@example.com"},
    {"id": 6, "name": "Rani", "email": "rani@example.com"},
]

products = [
    {"name": "Laptop", "price": 75000, "in_stock": True},
    {"name": "Mouse", "price": 599, "in_stock": True},
    {"name": "Keyboard", "price": 1299, "in_stock": False}
]

# Start time for uptime
start_time = datetime.now()

@app.route('/api/time')
def get_time():
    return jsonify({"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

@app.route('/api/users')
def get_users():
    return jsonify(users)

@app.route('/api/random')
def get_random():
    data = [
        "Keep learning!",
        "Flask is fun!",
        "Hello from the server!",
        random.randint(100, 999)
    ]
    return jsonify({"message": random.choice(data)})

@app.route('/api/status')
def status():
    uptime = str(datetime.now() - start_time)
    return jsonify({
        "status": "running",
        "uptime": uptime,
        "app_version": "1.0.0"
    })

@app.route('/api/products')
def product_list():
    return jsonify(products)

@app.route('/api/greet')
def greet_user():
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/api/error')
def trigger_error():
    error_type = request.args.get('type')
    if error_type == "404":
        return jsonify({"error": "Resource not found"}), 404
    elif error_type == "500":
        return jsonify({"error": "Internal Server Error"}), 500
    else:
        return jsonify({"message": "No error triggered"})

@app.route('/api/users_paginated')
def paginated_users():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 2))
    start = (page - 1) * limit
    end = start + limit
    return jsonify({
        "page": page,
        "limit": limit,
        "total_users": len(users),
        "users": users[start:end]
    })

@app.route('/api/custom-header')
def custom_header():
    data = {"message": "Check the custom headers in dev tools"}
    response = make_response(jsonify(data))
    response.headers['X-Custom-Header'] = 'FlaskAPI'
    return response

if __name__ == '__main__':
    app.run(debug=True)
