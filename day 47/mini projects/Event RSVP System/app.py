from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# In-memory RSVP list
guests = []

# Route 1: RSVP form
@app.route("/rsvp", methods=["GET"])
def rsvp_form():
    return """
    <h2>Event RSVP</h2>
    <form method="POST" action="/rsvp-confirm">
        Name: <input type="text" name="name" required><br><br>
        Email: <input type="email" name="email" required><br><br>
        Attending:
        <select name="attending">
            <option value="yes">Yes</option>
            <option value="no">No</option>
        </select><br><br>
        <input type="submit" value="Submit RSVP">
    </form>
    """

# Route 2: Handle form submission
@app.route("/rsvp-confirm", methods=["POST"])
def rsvp_confirm():
    name = request.form.get("name")
    email = request.form.get("email")
    attending = request.form.get("attending")

    guests.append({
        "name": name,
        "email": email,
        "attending": attending
    })

    return redirect(url_for("thank_you", name=name))

# Route 3: Thank the user personally
@app.route("/thank-you/<name>")
def thank_you(name):
    return f"<h3>Thank you, {name}, for your RSVP!</h3>"

# Route 4: Guest list filtered by attendance
@app.route("/guests")
def guest_list():
    attending = request.args.get("attending", "").lower()
    filtered = [g for g in guests if g["attending"].lower() == attending] if attending else guests

    if not filtered:
        return "<p>No matching guests found.</p>"

    html = "<h2>Guest List</h2><ul>"
    for g in filtered:
        html += f"<li>{g['name']} - {g['email']} - Attending: {g['attending']}</li>"
    html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(debug=True)
