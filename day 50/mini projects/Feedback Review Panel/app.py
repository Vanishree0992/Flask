from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Feedback
from forms import FeedbackForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback = Feedback(
            user_name=form.user_name.data,
            rating=form.rating.data,
            comment=form.comment.data
        )
        db.session.add(feedback)
        db.session.commit()
        flash("Thank you for your feedback!", "success")
        return redirect(url_for('index'))
    feedbacks = Feedback.query.all()
    return render_template('index.html', form=form, feedbacks=feedbacks)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_feedback(id):
    feedback = Feedback.query.get_or_404(id)
    form = FeedbackForm(obj=feedback)
    if form.validate_on_submit():
        feedback.user_name = form.user_name.data
        feedback.rating = form.rating.data
        feedback.comment = form.comment.data
        db.session.commit()
        flash("Feedback updated.", "info")
        return redirect(url_for('index'))
    return render_template('update.html', form=form)

@app.route('/delete/<int:id>')
def delete_feedback(id):
    feedback = Feedback.query.get_or_404(id)
    db.session.delete(feedback)
    db.session.commit()
    flash("Feedback deleted.", "danger")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
