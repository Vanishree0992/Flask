from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initial simulated count
current_count = 105

@app.route('/')
def home():
    return render_template('index.html', title="Live User Count Tracker")

@app.route('/api/users/count')
def user_count():
    global current_count
    # Simulate increase by 0-2 users
    current_count += random.choice([0, 1, 2])
    return jsonify({"count": current_count})

if __name__ == '__main__':
    app.run(debug=True)
