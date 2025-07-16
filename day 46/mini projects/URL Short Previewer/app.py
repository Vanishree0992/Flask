from flask import Flask

app = Flask(__name__)

@app.route('/preview/<string:site>')
def preview(site):
    site_name = site.capitalize()
    preview_text = f"This is {site}.com website. Here you might find a short description or thumbnail preview."

    return f"""
    <html>
      <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>{site_name} Preview</h1>
        <p style="font-size: 20px;">{preview_text}</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
