# app.py
from flask import Flask, render_template, redirect, url_for, request, flash
from datetime import datetime
from config import Config
from models import db, Task

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks = Task.query.order_by(Task.due_date).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d').date()
        new_task = Task(title=title, due_date=due_date)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added!', 'success')
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.is_done = not task.is_done
    db.session.commit()
    flash('Task updated!', 'info')
    return redirect(url_for('index'))

@app.route('/delete-done', methods=['POST'])
def delete_done():
    Task.query.filter_by(is_done=True).delete()
    db.session.commit()
    flash('Completed tasks deleted!', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
