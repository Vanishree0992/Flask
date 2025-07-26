from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

users = [{"name": "Arivu", "email": "arivu@example.com"}]
products = [
    {"name": "Laptop", "price": 75000},
    {"name": "Mouse", "price": 599},
    {"name": "Keyboard", "price": 1299}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/api/time')
def time_api():
    from datetime import datetime
    return jsonify({"time": datetime.now().strftime("%H:%M:%S")})

@app.route('/api/products')
def product_api():
    return jsonify(products)

@app.route('/api/items')
def paginate():
    page = int(request.args.get('page', 1))
    per_page = 2
    start = (page - 1) * per_page
    return jsonify(products[start:start + per_page])

@app.route('/api/status')
def status():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True)
