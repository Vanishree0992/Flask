from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Sample deals for /deals
sample_deals = {
    "paris": ["Eiffel Tour", "Romantic Dinner", "Seine Cruise"],
    "london": ["Big Ben Visit", "London Eye", "Thames Walk"],
    "tokyo": ["Shibuya Tour", "Mt. Fuji Day Trip", "Sushi Making Class"]
}

# Route to show booking form
@app.route("/booking", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        name = request.form.get("name")
        destination = request.form.get("destination")
        date = request.form.get("date")
        # Here you could store to DB, session, etc.
        return redirect(url_for("confirm_booking", name=name))
    
    return '''
        <h2>Travel Booking Form</h2>
        <form method="post">
            Name: <input type="text" name="name" required><br><br>
            Destination: 
            <select name="destination">
                <option>paris</option>
                <option>london</option>
                <option>tokyo</option>
            </select><br><br>
            Travel Date: <input type="date" name="date" required><br><br>
            <button type="submit">Submit</button>
        </form>
    '''

# Dynamic confirmation route
@app.route("/booking/confirm/<name>")
def confirm_booking(name):
    return f"<h3>Thank you, {name}, your travel booking enquiry has been received!</h3>"

# /deals?destination=paris
@app.route("/deals")
def deals():
    dest = request.args.get("destination", "").lower()
    offers = sample_deals.get(dest)
    
    if not offers:
        return f"<h3>No deals found for '{dest}'</h3>"
    
    offer_list = ''.join(f"<li>{deal}</li>" for deal in offers)
    return f"<h2>Deals for {dest.title()}</h2><ul>{offer_list}</ul>"

if __name__ == "__main__":
    app.run(debug=True)
