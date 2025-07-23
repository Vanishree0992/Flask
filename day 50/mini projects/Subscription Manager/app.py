from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Subscriber
from forms import SubscriptionForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def add_subscriber():
    form = SubscriptionForm()
    if form.validate_on_submit():
        subscriber = Subscriber(email=form.email.data, plan=form.plan.data)
        db.session.add(subscriber)
        db.session.commit()
        flash("Subscriber added!", "success")
        return redirect(url_for('list_subscribers'))
    return render_template('add.html', form=form)

@app.route('/subscribers')
def list_subscribers():
    subscribers = Subscriber.query.order_by(Subscriber.subscribed_on.desc()).all()
    return render_template('list.html', subscribers=subscribers)

@app.route('/delete/<int:id>')
def delete_subscriber(id):
    sub = Subscriber.query.get_or_404(id)
    db.session.delete(sub)
    db.session.commit()
    flash("Subscriber deleted!", "danger")
    return redirect(url_for('list_subscribers'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_subscriber(id):
    sub = Subscriber.query.get_or_404(id)
    form = SubscriptionForm(obj=sub)
    if form.validate_on_submit():
        sub.email = form.email.data
        sub.plan = form.plan.data
        db.session.commit()
        flash("Subscriber updated!", "info")
        return redirect(url_for('list_subscribers'))
    return render_template('add.html', form=form)
    
if __name__ == '__main__':
    app.run(debug=True)
