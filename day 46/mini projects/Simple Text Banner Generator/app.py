from flask import Flask

app = Flask(__name__)

# Route: /
@app.route('/')
def home():
    return """
        <html>
          <body>
            <p>Enter your banner text:</p>
            <a href="/banner/Hello">Try Banner: Hello</a>
          </body>
        </html>
    """

# Route:
@app.route('/banner/<string:text>')
def banner(text):
    return f"""
        <html>
          <body>
            <h1>{text}</h1>
            <p>Want a different size? Try /banner/{text}/3 for h3!</p>
          </body>
        </html>
    """

@app.route('/banner/<string:text>/<int:size>')
def banner_with_size(text, size):
    if size < 1 or size > 6:
        return "<p>Invalid size. Use 1–6.</p>"

    return f"""
        <html>
          <body>
            <h{size}>{text}</h{size}>
            <p>This is an h{size} heading.</p>
          </body>
        </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
