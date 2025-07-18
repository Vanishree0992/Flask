from flask import Flask, render_template, request
from jinja2 import Template, Markup

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def email_preview():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")

        # Dummy data for placeholders
        context = {
            "name": "John Doe",
            "product": "Flask App",
            "date": "July 18, 2025"
        }

        rendered_body = Markup(Template(body).render(context))
        return render_template("preview.html", title=title, body=rendered_body)

    return render_template("email_form.html")

if __name__ == "__main__":
    app.run(debug=True)
