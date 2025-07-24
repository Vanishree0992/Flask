# 1. What is a REST API?
# A REST API (Representational State Transfer Application Programming Interface) is a set of web services that allow interaction with resources using standard HTTP methods such as GET, POST, PUT, DELETE. It returns structured data, commonly in JSON format.

# 🔸 Real-world REST API Examples:
# GitHub API – fetch user repos, commits, etc.

# Twitter API – post tweets, read timelines.

# Google Maps API – get directions, places.

# Weather API (OpenWeatherMap) – current weather, forecast.

# Stripe API – manage payments and customers.

# 2.Create a new Flask app (api_app.py) intended for API only. 
from flask import Flask, jsonify
from datetime import datetime
import time
from flask_restful import Api,Response

app = Flask(__name__)
api = Api(app)

# Track server start time for uptime calculation
start_time = time.time()

# 3. Simple GET route
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({
        'message': 'Hello from Flask API!'
    }), 200

# 5. Static Info route
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'app_name': 'Flask REST API Demo',
        'version': '1.0.0'
    }), 200

# 6. System status route
@app.route('/status', methods=['GET'])
def status():
    uptime = round(time.time() - start_time, 2)
    return jsonify({
        'status': 'OK',
        'uptime_seconds': uptime,
        'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
# 7 Traditional HTML vs API JSON (in your own words)
# Traditional HTML	REST API JSON
# Returns full HTML pages	Returns structured JSON data
# Meant for human viewing (browsers)	Meant for machines or frontends (mobile/web apps)
# Uses templates like Jinja2	Uses data serialization like jsonify()
# Typically not reusable	Reusable across devices and clients

# JSON Response with jsonify()

# return jsonify({'message': 'Hello'}), 200
