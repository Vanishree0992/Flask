from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html', location="Chennai", title="Live Weather Dashboard")

@app.route('/api/weather')
def weather_api():
    weather_data = {
        "temperature": round(random.uniform(25, 40), 1),
        "humidity": random.randint(40, 90),
        "status": random.choice(["Sunny", "Cloudy", "Rainy", "Stormy"])
    }
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
