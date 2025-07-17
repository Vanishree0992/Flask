from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# In-memory database to store applications
applications = []

# Route 1: Form to apply
@app.route("/apply", methods=["GET"])
def apply_form():
    return """
    <h2>Job Application Form</h2>
    <form method="POST" action="/submit-application">
        Name: <input type="text" name="name"><br><br>
        Email: <input type="email" name="email"><br><br>
        Position: <input type="text" name="position"><br><br>
        <input type="submit" value="Apply">
    </form>
    """

# Route 2: Handle submission
@app.route("/submit-application", methods=["POST"])
def submit_application():
    name = request.form.get("name")
    email = request.form.get("email")
    position = request.form.get("position")

    applications.append({
        "name": name,
        "email": email,
        "position": position
    })

    return redirect(url_for('application_status'))

# Route 3: Status page
@app.route("/application-status")
def application_status():
    return "<h3>Your application has been submitted successfully!</h3>"

# Route 4: Query-based filtering
@app.route("/applications")
def view_applications():
    position = request.args.get("position")
    filtered = [app for app in applications if app["position"].lower() == position.lower()] if position else applications
    
    if not filtered:
        return "<h4>No applications found.</h4>"

    result = "<h2>Applications:</h2><ul>"
    for app in filtered:
        result += f"<li>{app['name']} - {app['email']} - {app['position']}</li>"
    result += "</ul>"
    return result

# Route 5: Dynamic applicant page
@app.route("/applicant/<name>")
def applicant_profile(name):
    for app in applications:
        if app['name'].lower() == name.lower():
            return f"""
            <h2>Applicant: {app['name']}</h2>
            <p>Email: {app['email']}</p>
            <p>Position: {app['position']}</p>
            """
    return "<h4>Applicant not found.</h4>"

if __name__ == "__main__":
    app.run(debug=True)
