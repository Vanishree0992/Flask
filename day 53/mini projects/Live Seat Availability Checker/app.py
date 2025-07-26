from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

EVENT_NAME = "Python Conference 2025"

# Simulated seat layout (A1–A6, B1–B6)
seat_ids = [f"A{i}" for i in range(1, 7)] + [f"B{i}" for i in range(1, 7)]

@app.route('/')
def index():
    return render_template("seats.html", event_name=EVENT_NAME, title="Live Seat Availability")

@app.route('/api/seats')
def get_seats():
    # Simulate random seat availability
    availability = {seat_id: random.choice([True, False]) for seat_id in seat_ids}
    return jsonify(availability)

if __name__ == '__main__':
    app.run(debug=True)
