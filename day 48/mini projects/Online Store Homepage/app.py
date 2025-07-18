from flask import Flask, render_template

app = Flask(__name__)

@app.route('/products')
def products():
    items = [
        {"name": "Laptop", "price": 899.99, "in_stock": True, "image": "laptop.jpg"},
        {"name": "Smartphone", "price": 499.99, "in_stock": False, "image": "phone.jpg"},
        {"name": "Headphones", "price": 129.99, "in_stock": True, "image": "headphones.jpg"}
    ]
    return render_template("products.html", products=items)

if __name__ == "__main__":
    app.run(debug=True)
