from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Simulated warranty data
warranty_data = {
    "ABC123": {"product": "Laptop", "warranty": "2 years"},
    "XYZ789": {"product": "Smartphone", "warranty": "1 year"},
    "LMN456": {"product": "Tablet", "warranty": "18 months"}
}

@app.route("/check-warranty", methods=["GET", "POST"])
def check_warranty():
    if request.method == "POST":
        serial = request.form.get("serial")
        return redirect(url_for("result", serial=serial))
    return '''
        <h2>Warranty Check</h2>
        <form method="POST">
            Enter Serial Number: <input name="serial" required>
            <button type="submit">Check</button>
        </form>
    '''

@app.route("/result")
def result():
    serial = request.args.get("serial")
    info = warranty_data.get(serial.upper())
    if info:
        return f'''
            <h3>Warranty Details for Serial: {serial}</h3>
            <p><strong>Product:</strong> {info["product"]}</p>
            <p><strong>Warranty:</strong> {info["warranty"]}</p>
            <a href="/check-warranty">Check Another</a>
        '''
    else:
        return f'''
            <h3>No warranty info found for Serial: {serial}</h3>
            <a href="/check-warranty">Try Again</a>
        '''

@app.route("/warranty/<product>")
def warranty_by_product(product):
    results = [s for s, info in warranty_data.items() if info["product"].lower() == product.lower()]
    if results:
        serials = ", ".join(results)
        return f'''
            <h3>{product.title()} Warranty Info</h3>
            Serial Numbers with this product: {serials}<br>
            <a href="/check-warranty">Back</a>
        '''
    else:
        return f"<h3>No warranty info for {product.title()}</h3><a href='/check-warranty'>Back</a>"

if __name__ == "__main__":
    app.run(debug=True)
