from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def clock():
    now = datetime.now()
    return render_template('clock.html', hour=now.hour, minute=now.minute, second=now.second, title="Digital Clock")

@app.route('/api/time')
def get_time():
    now = datetime.now()
    return jsonify({
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second
    })

if __name__ == '__main__':
    app.run(debug=True)
