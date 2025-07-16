from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/age/<string:name>/<int:year>')
def age_checker(name, year):
    current_year = datetime.now().year

    if year >= current_year:
        return f"""
        <html>
          <body>
            <h1>Error</h1>
            <p>The year must be less than {current_year}.</p>
          </body>
        </html>
        """

    age = current_year - year

    return f"""
    <html>
      <body style="font-family: Arial; text-align: center;">
        <h1>Age Checker</h1>
        <p>Hi {name.title()}, you are {age} years old.</p>
      </body>
    </html>
    """

if __name__ == '__main__':
     app.run(debug=True, port=5050, host="0.0.0.0")
