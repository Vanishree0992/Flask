from flask import Flask,request
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "This is the about page"

print("Starting Flask server...")

# /hello route
@app.route("/hello")
def hello():
    return "Welcome to Flask!"

# Dynamic route
@app.route("/user/<username>")
def user(username):
    return f"Hello, {username}!"

#Multiple routes, same function
@app.route("/hi")
@app.route("/hey")
def greet():
    return "Hi there!"

#Different HTTP methods
@app.route("/submit", methods=["GET", "POST"])
def submit():
    return f"Method used: {request.method}"

#Return basic HTML
@app.route("/html")
def html():
    return "<h1>Hello HTML</h1>"

#Inline CSS
    return "<h1 style='color:blue;'>Blue Heading</h1>"

# Multiline HTML
    return """
<h1>Welcome</h1>
<p>This is multiline HTML</p>
"""

#Unordered list
    return """
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
"""
#<h1> — big heading

# <p> — paragraph

# <br> — line break

# <hr> — horizontal line

@app.route("/")
def home():
    return """
    <h1>Welcome to My Flask Page</h1>
    <p>This is a paragraph explaining what this page is about.</p>
    <hr>
    <p>Here is another line.<br>And this text appears on a new line because of &lt;br&gt;.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
