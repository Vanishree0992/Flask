from flask import Flask

app = Flask(__name__)

# Dummy Zodiac mapping by month
zodiac_by_month = {
    1: "Capricorn",
    2: "Aquarius",
    3: "Pisces",
    4: "Aries",
    5: "Taurus",
    6: "Gemini",
    7: "Cancer",
    8: "Leo",
    9: "Virgo",
    10: "Libra",
    11: "Scorpio",
    12: "Sagittarius"
}

@app.route('/zodiac/help')
def help_page():
    return """
    <html>
      <body style="font-family: Arial; text-align: center;">
        <h1>Zodiac Sign Generator - Help</h1>
        <hr>
        <p>To get your Zodiac sign, use the format: <strong>/zodiac/YYYY-MM-DD</strong></p>
        <p>Example: <i>/zodiac/2000-12-25</i></p>
      </body>
    </html>
    """

@app.route('/zodiac/<string:date>')
def get_zodiac(date):
    try:
        parts = date.split('-')
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        sign = zodiac_by_month.get(month, "Unknown")

        return f"""
        <html>
          <body style="font-family: Arial; text-align: center;">
            <h1>Your Zodiac Sign</h1>
            <hr>
            <p>Date Entered: <strong>{date}</strong></p>
            <p>Your sign is: <i>{sign}</i></p>
          </body>
        </html>
        """
    except Exception as e:
        return f"""
        <html>
          <body style="font-family: Arial; text-align: center;">
            <h1>Error</h1>
            <hr>
            <p>Invalid date format. Use <strong>YYYY-MM-DD</strong>.</p>
          </body>
        </html>
        """

if __name__ == '__main__':
    app.run(debug=True)
