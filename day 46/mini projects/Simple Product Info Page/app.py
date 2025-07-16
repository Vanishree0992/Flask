from flask import Flask

app = Flask(__name__)

# Hardcoded product data
products = {
    1: {"name": "Laptop", "price": 1200, "stock": True},
    2: {"name": "Smartphone", "price": 800, "stock": False},
    3: {"name": "Headphones", "price": 150, "stock": True}
}

@app.route('/product/<int:id>')
def product_info(id):
    print(f"[LOG] /product/{id} accessed")  # Terminal log

    product = products.get(id)
    if product:
        stock_status = "In Stock" if product["stock"] else "Out of Stock"
        return f"""
        <html>
          <body style="font-family: Arial;">
            <h1>Product Info</h1>
            <p><b>ID:</b> {id}</p>
            <p><b>Name:</b> {product['name']}</p>
            <p><b>Price:</b> ${product['price']}</p>
            <p><b>Stock Status:</b> {stock_status}</p>
            <p><a href="/products">Back to Products</a></p>
          </body>
        </html>
        """
    else:
        return f"<h1>Product ID {id} not found.</h1>"

@app.route('/products')
def all_products():
    print("[LOG] /products accessed")  # Terminal log

    rows = ""
    for pid, pdata in products.items():
        rows += f"<tr><td>{pid}</td><td>{pdata['name']}</td></tr>"

    return f"""
    <html>
      <body style="font-family: Arial;">
        <h1>All Products</h1>
        <table border="1" cellpadding="5" cellspacing="0">
          <tr><th>ID</th><th>Name</th></tr>
          {rows}
        </table>
        <p>Click on /product/&lt;id&gt; to see details</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
