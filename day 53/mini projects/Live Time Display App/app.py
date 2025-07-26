from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", title="Live Time Display")

@app.route('/api/time')
def get_time():
    now = datetime.now().strftime('%H:%M:%S')
    return jsonify({"time": now})

if __name__ == '__main__':
    app.run(debug=True)
