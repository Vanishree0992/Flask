from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Contact
from forms import ContactForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    contacts = Contact.query.all()
    return render_template('list_contacts.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            address=form.address.data
        )
        db.session.add(contact)
        db.session.commit()
        flash("Contact added!", "success")
        return redirect(url_for('home'))
    return render_template('add_contact.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    contact = Contact.query.get_or_404(id)
    form = ContactForm(obj=contact)
    if form.validate_on_submit():
        contact.name = form.name.data
        contact.phone = form.phone.data
        contact.email = form.email.data
        contact.address = form.address.data
        db.session.commit()
        flash("Contact updated!", "info")
        return redirect(url_for('home'))
    return render_template('edit_contact.html', form=form)

@app.route('/delete/<int:id>')
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    flash("Contact deleted!", "danger")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
