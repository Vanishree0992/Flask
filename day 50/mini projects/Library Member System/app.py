from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Member
from forms import MemberForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def add_member():
    form = MemberForm()
    if form.validate_on_submit():
        member = Member(name=form.name.data, email=form.email.data)
        db.session.add(member)
        db.session.commit()
        flash("Member added successfully!", "success")
        return redirect(url_for('add_member'))
    return render_template('add.html', form=form)

@app.route('/members')
def view_members():
    members = Member.query.order_by(Member.join_date.desc()).all()
    return render_template('view.html', members=members)

@app.route('/delete/<int:id>')
def delete_member(id):
    member = Member.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    flash("Member deleted!", "danger")
    return redirect(url_for('view_members'))

if __name__ == '__main__':
    app.run(debug=True)
