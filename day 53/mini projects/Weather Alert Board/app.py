from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

REGION = "Tamil Nadu"

SAMPLE_ALERTS = [
    {"type": "warning", "message": "Heavy rainfall expected today."},
    {"type": "danger", "message": "Cyclone alert for coastal areas."},
    {"type": "info", "message": "Humidity expected to rise."},
    {"type": "success", "message": "Clear skies in the evening."}
]

@app.route('/')
def index():
    return render_template("alerts.html", region=REGION, title="Weather Alert Board")

@app.route('/api/weather/alerts')
def weather_alerts():
    count = random.randint(1, 3)
    alerts = random.sample(SAMPLE_ALERTS, count)
    return jsonify(alerts)

if __name__ == '__main__':
    app.run(debug=True)
