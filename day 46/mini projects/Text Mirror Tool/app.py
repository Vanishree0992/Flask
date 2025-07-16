from flask import Flask

app = Flask(__name__)

@app.route('/mirror/<string:text>')
def mirror_text(text):
    reversed_text = text[::-1]
    length = len(text)

    return f"""
    <html>
      <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>Text Mirror Tool</h1>
        <pre>
Original Text: {text}
Reversed Text: {reversed_text}
Length: {length}
        </pre>
        <table border="1" cellpadding="10" cellspacing="0" style="margin: 20px auto;">
          <tr>
            <th>Original</th>
            <th>Reversed</th>
            <th>Length</th>
          </tr>
          <tr>
            <td>{text}</td>
            <td>{reversed_text}</td>
            <td>{length}</td>
          </tr>
        </table>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
