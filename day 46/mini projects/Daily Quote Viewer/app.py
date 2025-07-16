from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Hardcoded quotes for each day
quotes = {
    "monday": "Start your week with a smile!",
    "tuesday": "Keep going, you're doing great!",
    "wednesday": "Halfway there. Stay strong!",
    "thursday": "Push through, the weekend is near.",
    "friday": "Finish strong and celebrate your wins!",
    "saturday": "Relax, recharge, and enjoy your day.",
    "sunday": "Prepare, reflect, and plan for success."
}

# / shows today’s quote
@app.route('/')
def today_quote():
    day_name = datetime.now().strftime('%A').lower()
    quote = quotes.get(day_name, "Have a wonderful day!")
    return f"""
    <html>
      <body style="background-color:#f0f8ff; font-family: Arial; text-align: center;">
        <h1 style="color:#333;">Quote for {day_name.title()}</h1>
        <p style="font-size: 24px; color: #555;">"{quote}"</p>
      </body>
    </html>
    """

# /quote/<day> shows quote for that day
@app.route('/quote/<string:day>')
def quote_for_day(day):
    day_lower = day.lower()
    quote = quotes.get(day_lower, "No quote found for this day.")
    return f"""
    <html>
      <body style="background-color:#fff8dc; font-family: Verdana; text-align: center;">
        <h1 style="color:#222;">Quote for {day_lower.title()}</h1>
        <p style="font-size: 24px; color: #444;">"{quote}"</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
