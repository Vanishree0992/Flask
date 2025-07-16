from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Route: /
@app.route('/')
def home():
    now = datetime.now()
    current_hour = now.hour

    # Business hours: 9 AM to 5 PM
    if 9 <= current_hour < 17:
        status = "<h1>We are open!</h1>"
    else:
        status = "<h1>Closed</h1>"

    return f"""
        <html>
            <body>
                {status}
                <p>Current server time: {now.strftime('%Y-%m-%d %H:%M:%S')}</p>
                <hr>
                <p>Thank you for visiting our business hours page.</p>
            </body>
        </html>
    """

# Route: /contact
@app.route('/contact')
def contact():
    return """
        <html>
            <body>
                <h1>Contact Us</h1>
                <p><b>Email:</b> contact@mybusiness.com</p>
                <p><b>Phone:</b> +1-234-567-890</p>
                <hr>
                <p>We look forward to hearing from you!</p>
            </body>
        </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
