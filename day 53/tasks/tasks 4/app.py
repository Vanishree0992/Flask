from flask import Flask, render_template, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Arivu", "status": "active"},
    {"id": 2, "name": "Vani", "status": "inactive"},
    {"id": 3, "name": "Ravi", "status": "active"}
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html', users=users, user_id=1)

@app.route('/api/users')
def api_users():
    return jsonify(users)

@app.route('/api/chart-data')
def chart_data():
    return jsonify({"labels": ["Jan", "Feb", "Mar"], "values": [10, 20, 30]})

if __name__ == '__main__':
    app.run(debug=True)
