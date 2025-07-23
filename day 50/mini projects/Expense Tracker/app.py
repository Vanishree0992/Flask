from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from models import db, Expense
from forms import ExpenseForm
from sqlalchemy import func

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def add_expense():
    form = ExpenseForm()
    if form.validate_on_submit():
        exp = Expense(
            name=form.name.data,
            amount=form.amount.data,
            category=form.category.data,
            date=form.date.data
        )
        db.session.add(exp)
        db.session.commit()
        flash("Expense added successfully!", "success")
        return redirect(url_for('add_expense'))
    return render_template('add.html', form=form)

@app.route('/expenses')
def view_expenses():
    group = request.args.get('group')
    if group == 'category':
        expenses = db.session.query(
            Expense.category,
            func.sum(Expense.amount).label('total')
        ).group_by(Expense.category).all()
        return render_template('view.html', group_by='Category', grouped=True, expenses=expenses)

    elif group == 'date':
        expenses = db.session.query(
            Expense.date,
            func.sum(Expense.amount).label('total')
        ).group_by(Expense.date).all()
        return render_template('view.html', group_by='Date', grouped=True, expenses=expenses)

    else:
        expenses = Expense.query.order_by(Expense.date.desc()).all()
        return render_template('view.html', expenses=expenses, grouped=False)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_expense(id):
    exp = Expense.query.get_or_404(id)
    form = ExpenseForm(obj=exp)
    if form.validate_on_submit():
        exp.name = form.name.data
        exp.amount = form.amount.data
        exp.category = form.category.data
        exp.date = form.date.data
        db.session.commit()
        flash("Expense updated!", "info")
        return redirect(url_for('view_expenses'))
    return render_template('update.html', form=form)

@app.route('/delete/<int:id>')
def delete_expense(id):
    exp = Expense.query.get_or_404(id)
    db.session.delete(exp)
    db.session.commit()
    flash("Expense deleted!", "danger")
    return redirect(url_for('view_expenses'))

if __name__ == '__main__':
    app.run(debug=True)
