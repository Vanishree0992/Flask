from flask import Flask, render_template, jsonify, request, flash, redirect, url_for
from flask import session
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "user123"
CORS(app)

# Simulated current user
current_user = {
    "id": 1,
    "name": "Arivu Kumar",
    "email": "arivu@example.com"
}

@app.route('/')
def profile():
    message = session.pop("message", None)
    return render_template("profile.html", user=current_user, message=message)

@app.route('/api/user/<int:user_id>', methods=["PUT"])
def update_user(user_id):
    if user_id != current_user["id"]:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    if name and email:
        current_user["name"] = name
        current_user["email"] = email
        session["message"] = "✅ Profile updated successfully!"
        return jsonify({"success": True})
    return jsonify({"error": "Invalid data"}), 400

if __name__ == "__main__":
    app.run(debug=True)
