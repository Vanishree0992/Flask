from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from models import db, Application
from forms import ApplicationForm, StatusForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def list_applications():
    status_filter = request.args.get('status')
    if status_filter:
        apps = Application.query.filter_by(status=status_filter).all()
    else:
        apps = Application.query.all()
    return render_template('list_applications.html', apps=apps)

@app.route('/add', methods=['GET', 'POST'])
def add_application():
    form = ApplicationForm()
    if form.validate_on_submit():
        app_data = Application(
            name=form.name.data,
            email=form.email.data,
            job_title=form.job_title.data,
            status=form.status.data
        )
        db.session.add(app_data)
        db.session.commit()
        flash('Application added successfully!', 'success')
        return redirect(url_for('list_applications'))
    return render_template('add_application.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_status(id):
    app_data = Application.query.get_or_404(id)
    form = StatusForm(status=app_data.status)
    if form.validate_on_submit():
        app_data.status = form.status.data
        db.session.commit()
        flash('Status updated successfully.', 'info')
        return redirect(url_for('list_applications'))
    return render_template('update_status.html', form=form, application=app_data)

@app.route('/delete/<int:id>')
def delete_application(id):
    app_data = Application.query.get_or_404(id)
    db.session.delete(app_data)
    db.session.commit()
    flash('Application deleted.', 'danger')
    return redirect(url_for('list_applications'))

if __name__ == '__main__':
    app.run(debug=True)
