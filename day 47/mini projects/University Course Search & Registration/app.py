from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Sample course data
courses = [
    {"code": "CS101", "name": "Intro to CS", "dept": "CS"},
    {"code": "CS201", "name": "Data Structures", "dept": "CS"},
    {"code": "EE101", "name": "Basic Circuits", "dept": "EE"},
    {"code": "ME101", "name": "Thermodynamics", "dept": "ME"},
]

# Route to show courses and filter by dept
@app.route("/courses")
def course_list():
    dept = request.args.get("dept")
    if dept:
        filtered = [c for c in courses if c["dept"].lower() == dept.lower()]
    else:
        filtered = courses

    html = "<h2>Available Courses</h2><ul>"
    for course in filtered:
        html += f"<li>{course['code']} - {course['name']} ({course['dept']})</li>"
    html += "</ul>"

    html += '''
        <form method="get">
            <label>Filter by Department (e.g., CS, EE):</label>
            <input type="text" name="dept">
            <button type="submit">Search</button>
        </form>
        <br><a href="/register">Register for a Course</a>
    '''
    return html

# Route to register for a course
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        course_code = request.form.get("course")
        return redirect(url_for("confirm", name=name))

    return '''
        <h2>Course Registration</h2>
        <form method="post">
            Student Name: <input type="text" name="name" required><br><br>
            Course Code: <input type="text" name="course" required><br><br>
            <button type="submit">Register</button>
        </form>
        <br><a href="/courses">Back to Course List</a>
    '''

# Route to confirm registration
@app.route("/confirm-registration/<name>")
def confirm(name):
    return f"<h3>Thank you, {name}, your course registration was successful!</h3>"

if __name__ == "__main__":
    app.run(debug=True)
