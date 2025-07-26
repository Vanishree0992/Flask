from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

products = [
    {"name": "Apple iPhone 14", "price": "$799"},
    {"name": "Samsung Galaxy S23", "price": "$749"},
    {"name": "OnePlus 11", "price": "$699"},
    {"name": "Google Pixel 7", "price": "$599"},
    {"name": "Sony WH-1000XM4", "price": "$349"},
    {"name": "Dell XPS 13", "price": "$999"},
    {"name": "MacBook Air M2", "price": "$1199"},
]

@app.route('/')
def index():
    return render_template("index.html", title="Product Search")

@app.route('/api/products')
def api_products():
    query = request.args.get("q", "").lower()
    filtered = [p for p in products if query in p["name"].lower()]
    return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True)
