from flask import Flask, render_template

app = Flask(__name__)

@app.route('/courses')
def courses():
    course_list = [
        {"title": "Python for Beginners", "instructor": "Alice", "duration": "6 weeks", "level": "beginner"},
        {"title": "Web Development with Flask", "instructor": "Bob", "duration": "8 weeks", "level": "intermediate"},
        {"title": "Data Science with Python", "instructor": "Charlie", "duration": "10 weeks", "level": "advanced"}
    ]
    return render_template("courses.html", courses=course_list)

if __name__ == '__main__':
    app.run(debug=True)
