from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
votes = {"A": 0, "B": 0, "C": 0}
voter_choices = {}

# Route 1: Poll form
@app.route("/poll", methods=["GET"])
def poll():
    return """
    <h2>Vote for Your Favorite Option</h2>
    <form method="POST" action="/vote">
        Name: <input type="text" name="name" required><br><br>
        <input type="radio" name="option" value="A" required> Option A<br>
        <input type="radio" name="option" value="B"> Option B<br>
        <input type="radio" name="option" value="C"> Option C<br><br>
        <input type="submit" value="Vote">
    </form>
    """

# Route 2: Handle vote submission
@app.route("/vote", methods=["POST"])
def vote():
    name = request.form.get("name")
    option = request.form.get("option")

    if name and option:
        votes[option] += 1
        voter_choices[name.lower()] = option
        return redirect(url_for("voter", name=name))
    else:
        return "Invalid input. Please go back and fill the form.", 400

# Route 3: Show personalized vote result
@app.route("/voter/<name>")
def voter(name):
    vote = voter_choices.get(name.lower())
    if vote:
        return f"<h3>{name}, you voted for Option {vote}.</h3>"
    else:
        return "<p>No vote found for this name.</p>"

# Route 4: Result page showing count by option
@app.route("/result")
def result():
    option = request.args.get("option")
    if option in votes:
        return f"<h2>Votes for Option {option}: {votes[option]}</h2>"
    else:
        return """
        <h2>Poll Results</h2>
        <ul>
            <li>Option A: {}</li>
            <li>Option B: {}</li>
            <li>Option C: {}</li>
        </ul>
        """.format(votes["A"], votes["B"], votes["C"])

if __name__ == "__main__":
    app.run(debug=True)
