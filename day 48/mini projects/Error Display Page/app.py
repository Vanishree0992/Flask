from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Home Page</h1>"

@app.route("/cause-500")
def cause_500():
    # Force an error to trigger the 500 page
    raise Exception("Internal server error occurred.")

@app.errorhandler(404)
def not_found_error(e):
    return render_template("404.html", error_message=str(e)), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html", error_message=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True)
