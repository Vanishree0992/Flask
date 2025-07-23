from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Complaint
from forms import ComplaintForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def submit_complaint():
    form = ComplaintForm()
    if form.validate_on_submit():
        complaint = Complaint(name=form.name.data, message=form.message.data)
        db.session.add(complaint)
        db.session.commit()
        flash("Complaint submitted successfully!", "success")
        return redirect(url_for('submit_complaint'))
    return render_template('submit.html', form=form)

@app.route('/admin')
def admin_dashboard():
    complaints = Complaint.query.all()
    total = Complaint.query.count()
    resolved = Complaint.query.filter_by(resolved=True).count()
    return render_template('admin.html', complaints=complaints, total=total, resolved=resolved)

@app.route('/resolve/<int:id>')
def mark_resolved(id):
    complaint = Complaint.query.get_or_404(id)
    complaint.resolved = True
    db.session.commit()
    flash("Marked as resolved", "info")
    return redirect(url_for('admin_dashboard'))

@app.route('/delete/<int:id>')
def delete_complaint(id):
    complaint = Complaint.query.get_or_404(id)
    db.session.delete(complaint)
    db.session.commit()
    flash("Complaint deleted", "danger")
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
