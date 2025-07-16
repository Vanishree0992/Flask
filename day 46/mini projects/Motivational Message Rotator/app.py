from flask import Flask
import random

app = Flask(__name__)

# Hardcoded list of motivational quotes
quotes = [
    "Believe in yourself and all that you are!",
    "Push yourself because no one else is going to do it for you.",
    "Success doesn’t just find you — you have to go out and get it.",
    "Great things never come from comfort zones.",
    "Dream bigger. Do bigger.",
    "Wake up with determination, go to bed with satisfaction.",
    "Don’t stop until you’re proud!"
]

# /message: random quote
@app.route('/message')
def random_message():
    quote = random.choice(quotes)
    return f"""
    <html>
      <body style="background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); 
                   color: #333; font-family: Arial; text-align: center; padding: 50px;">
        <h1 style="color: #fff;">Motivational Message</h1>
        <p style="font-size: 28px; color: #222;">"{quote}"</p>
        <p><i>Refresh for a new one!</i></p>
      </body>
    </html>
    """

# /message/<index>: manual select
@app.route('/message/<int:index>')
def message_by_index(index):
    if 0 <= index < len(quotes):
        quote = quotes[index]
    else:
        quote = "Oops! Invalid index. Try 0 to {}.".format(len(quotes) - 1)
    return f"""
    <html>
      <body style="background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%); 
                   color: #333; font-family: Arial; text-align: center; padding: 50px;">
        <h1 style="color: #222;">Your Selected Message</h1>
        <p style="font-size: 28px; color: #111;">"{quote}"</p>
        <p>Use /message/&lt;index&gt; (0-{len(quotes)-1})</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
