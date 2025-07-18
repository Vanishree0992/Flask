from flask import Flask, render_template

app = Flask(__name__)

@app.route('/result')
def student_result():
    student = {
        "name": "Vanishree",
        "subjects": {
            "Math": 88,
            "Science": 75,
            "English": 92,
            "History": 67
        }
    }

    marks = student["subjects"].values()
    avg = sum(marks) / len(marks)

    if avg >= 85:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    else:
        grade = "C"

    return render_template('result.html', student=student, grade=grade)

if __name__ == '__main__':
    app.run(debug=True)
