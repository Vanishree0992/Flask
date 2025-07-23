from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Item
from forms import ItemForm, UpdateForm

from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data, quantity=form.quantity.data)
        db.session.add(item)
        db.session.commit()
        flash("Item added to inventory.", "success")
        return redirect(url_for('index'))
    items = Item.query.order_by(Item.updated_on.desc()).all()
    return render_template('index.html', form=form, items=items)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_item(id):
    item = Item.query.get_or_404(id)
    form = UpdateForm()
    if form.validate_on_submit():
        new_qty = form.quantity.data
        if new_qty == 0:
            db.session.delete(item)
            flash("Item deleted due to zero stock.", "warning")
        else:
            item.quantity = new_qty
            flash("Quantity updated.", "info")
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', item=item, form=form)

@app.route('/delete/<int:id>')
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash("Item deleted.", "danger")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
