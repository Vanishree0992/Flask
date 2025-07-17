from flask import Flask, request, redirect, url_for, flash, render_template_string, session

app = Flask(__name__)
app.secret_key = "supersecret"  # Needed for flashing messages

# Sample departments
departments = ['sales', 'support', 'hr', 'admin']

# Route 1: Show contact form
@app.route("/contact", methods=["GET"])
def contact():
    thank_you = ""
    if '_flashes' in dict(session):
        thank_you = '<p style="color:green;">' + list(dict(session['_flashes']).values())[0] + '</p>'
    return render_template_string("""
        <h2>Contact Us</h2>
        <form method="POST" action="/submit?source=homepage">
            Name: <input type="text" name="name" required><br><br>
            Email: <input type="email" name="email" required><br><br>
            Message: <textarea name="message" required></textarea><br><br>
            Department:
            <select name="department">
                <option value="sales">Sales</option>
                <option value="support">Support</option>
                <option value="hr">HR</option>
                <option value="admin">Admin</option>
            </select><br><br>
            <input type="submit" value="Send">
        </form>
        {{ thank_you }}
    """, thank_you=thank_you)

# Route 2: Handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    department = request.form.get("department")
    source = request.args.get("source", "unknown")

    # In real use-case: store/save/send these values
    print(f"Received from {name} ({email}) to {department} from {source}:\n{message}")

    flash("Thanks for contacting us! We'll get back to you soon.")
    return redirect(url_for("thank_you", department=department))

# Route 3: Thank You Page with department context
@app.route("/contact/<department>")
def thank_you(department):
    if department.lower() not in departments:
        return "<h3>Unknown department.</h3>", 404
    return f"""
    <h3>Thank you for contacting {department.title()} Department.</h3>
    <a href="/contact">Back to Contact Form</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
