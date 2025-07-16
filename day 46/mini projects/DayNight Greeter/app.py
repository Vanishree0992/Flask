from flask import Flask

app = Flask(__name__)

@app.route('/greet/<int:hour>')
def greet(hour):
    if hour < 0 or hour > 23:
        message = "Invalid hour. Use 0–23."
    elif 5 <= hour < 12:
        message = "Good Morning!"
    elif 12 <= hour < 18:
        message = "Good Afternoon!"
    else:
        message = "Good Night!"
    
    return f"""
    <html>
      <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>Day/Night Greeter</h1>
        <p style="font-size: 24px;">{message}</p>
      </body>
    </html>
    """

@app.route('/greet/info')
def info():
    return """
    <html>
      <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>Greeter Info</h1>
        <p>Use the route format: <strong>/greet/&lt;hour&gt;</strong></p>
        <p>Valid hours are from 0 to 23 (24-hour format).</p>
        <p>Examples:</p>
        <ul style="list-style: none;">
          <li>/greet/9 → Good Morning!</li>
          <li>/greet/15 → Good Afternoon!</li>
          <li>/greet/22 → Good Night!</li>
        </ul>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
