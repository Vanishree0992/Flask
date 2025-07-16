from flask import Flask

app = Flask(__name__)

@app.route('/wordcount/help')
def help_page():
    return """
    <html>
      <body style="font-family: Arial; text-align: center;">
        <h1 style="color: #333;">Word Counter Help</h1>
        <p style="font-size: 18px;">
          Use this format: <strong>/wordcount/&lt;text&gt;</strong><br>
          Example: <i>/wordcount/Hello world this is Flask</i>
        </p>
      </body>
    </html>
    """

@app.route('/wordcount/<string:text>')
def word_counter(text):
    words = text.split()
    count = len(words)

    return f"""
    <html>
      <body style="font-family: Arial; text-align: center;">
        <h1 style="color: #2c3e50;">Word Counter</h1>
        <p style="font-size: 20px;">
          Original Text: <strong>{text}</strong><br>
          Word Count: <strong>{count}</strong>
        </p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
