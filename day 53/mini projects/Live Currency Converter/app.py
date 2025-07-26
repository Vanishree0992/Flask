from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample static conversion rates to INR
conversion_rates = {
    "USD": 83.12,
    "EUR": 91.34,
    "GBP": 107.89,
    "JPY": 0.57,
    "INR": 1.0
}

@app.route('/')
def index():
    return render_template("index.html", currencies=conversion_rates.keys(), title="Live Currency Converter")

@app.route('/api/convert')
def convert():
    try:
        amount = float(request.args.get("amount", 0))
        target_currency = request.args.get("to", "INR").upper()
        rate = conversion_rates.get(target_currency)

        if rate:
            converted = round(amount * rate, 2)
            return jsonify({"converted": converted, "rate": rate})
        else:
            return jsonify({"error": "Invalid currency"}), 400
    except:
        return jsonify({"error": "Conversion failed"}), 500

if __name__ == '__main__':
    app.run(debug=True)
