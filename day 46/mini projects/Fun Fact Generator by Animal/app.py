from flask import Flask

app = Flask(__name__)

fun_facts = {
    "cat": "Cats sleep for 70% of their lives!",
    "dog": "Dogs have three eyelids!",
    "elephant": "Elephants are the only animals that can't jump.",
    "dolphin": "Dolphins have names for each other!"
}

@app.route('/fact/<string:animal>')
def fact(animal):
    animal_lower = animal.lower()
    fact = fun_facts.get(animal_lower)

    if fact:
        return f"""
        <html>
          <body style="font-family: Arial; text-align: center; background-color: #f0f8ff; padding: 50px;">
            <h1 style="color: #2c3e50;">Fun Fact about {animal.capitalize()}</h1>
            <p style="font-size: 22px; color: #34495e;">{fact}</p>
            <p><a href="/fact/list">See All Animals</a></p>
          </body>
        </html>
        """
    else:
        return f"""
        <html>
          <body style="font-family: Arial; text-align: center; background-color: #ffe6e6; padding: 50px;">
            <h1 style="color: #c0392b;">Oops!</h1>
            <p style="font-size: 20px;">No fun fact found for <strong>{animal}</strong>.</p>
            <p><a href="/fact/list">See Available Animals</a></p>
          </body>
        </html>
        """

@app.route('/fact/list')
def list_animals():
    animal_list = "".join([f"<li>{animal.capitalize()}</li>" for animal in fun_facts.keys()])

    return f"""
    <html>
      <body style="font-family: Arial; text-align: center; background-color: #e8f5e9; padding: 50px;">
        <h1 style="color: #27ae60;">Available Animals</h1>
        <ul style="list-style: none; font-size: 20px; color: #2c3e50;">
          {animal_list}
        </ul>
        <p>Try: /fact/&lt;animal&gt; (example: <i>/fact/cat</i>)</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
