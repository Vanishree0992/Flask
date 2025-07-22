from flask import Flask, render_template, request, redirect, flash, url_for
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])  # Home page
def index():
    form = ContactForm()

    if form.validate_on_submit():
        print("Form Data Submitted:", form.data)  # 1.2, 4.4
        flash(f"Form submitted successfully! Hello, {form.name.data}", "success")  # 3.1, 3.6
        if form.age.data > 60:
            flash("You're above 60! Be sure to take it easy!", "info")  # 3.7
        return render_template("success.html", form=form)
    elif request.method == "POST":
        flash("There were errors in the form. Please fix them.", "error")  # 3.4
        print("Form Errors:", form.errors)  # 4.4

    return render_template("form.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
