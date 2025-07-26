from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Dummy student and score data
students = [
    {"id": 1, "name": "Arivu"},
    {"id": 2, "name": "Banu"},
    {"id": 3, "name": "Chitra"}
]

scores = {
    1: {"Math": 88, "Science": 92, "English": 85},
    2: {"Math": 75, "Science": 80, "English": 78},
    3: {"Math": 90, "Science": 95, "English": 93}
}

@app.route('/')
def index():
    return render_template("index.html", students=students, title="Student Score Viewer")

@app.route('/api/score/<int:student_id>')
def get_score(student_id):
    student_scores = scores.get(student_id)
    if student_scores:
        return jsonify(student_scores)
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
