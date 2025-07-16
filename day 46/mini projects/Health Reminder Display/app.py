from flask import Flask

app = Flask(__name__)

@app.route('/reminder/<int:hour>')
def reminder(hour):
    if hour < 0 or hour > 23:
        message = "Invalid hour. Please use an hour between 0 and 23."
    elif 5 <= hour < 10:
        message = "Good Morning! Remember to eat a healthy breakfast."
    elif 10 <= hour < 14:
        message = "Time to drink some water and stay hydrated!"
    elif 14 <= hour < 18:
        message = "Take a short walk or stretch to keep your energy up!"
    elif 18 <= hour < 22:
        message = "Relax and avoid screens before bedtime."
    else:
        message = "Get some good sleep! Your body needs rest."

    return f"""
    <html>
      <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>Health Reminder</h1>
        <p style="font-size: 22px;">{message}</p>
      </body>
    </html>
    """

@app.route('/reminder/help')
def reminder_help():
    return """
    <html>
      <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>Health Reminder Help</h1>
        <p>Use this format: <strong>/reminder/&lt;hour&gt;</strong></p>
        <p>Example: <i>/reminder/9</i> or <i>/reminder/15</i></p>
        <p>Hour should be in 24-hour format (0–23).</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
