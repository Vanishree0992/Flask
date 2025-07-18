from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route('/weather')
def weather():
    weather_info = {
        "date": date.today().strftime("%B %d, %Y"),
        "location": "Bangalore",
        "temperature": 34,
        "condition": "Sunny", 
        "hourly_temps": [28, 30, 32, 34, 33, 31, 29]  # for chart
    }
    return render_template("weather.html", weather=weather_info)

if __name__ == '__main__':
    app.run(debug=True)
