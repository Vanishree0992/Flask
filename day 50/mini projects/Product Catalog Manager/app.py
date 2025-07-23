# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import db, Product

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    products = Product.query.order_by(Product.id.desc()).all()
    return render_template('index.html', products=products)

@app.route('/in-stock')
def in_stock():
    products = Product.query.filter_by(in_stock=True).all()
    return render_template('index.html', products=products, in_stock=True)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        in_stock = 'in_stock' in request.form
        description = request.form['description']
        new_product = Product(name=name, price=price, in_stock=in_stock, description=description)
        db.session.add(new_product)
        db.session.commit()
        flash('Product added!', 'success')
        return redirect(url_for('index'))
    return render_template('add_product.html')

@app.route('/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = float(request.form['price'])
        product.in_stock = 'in_stock' in request.form
        product.description = request.form['description']
        db.session.commit()
        flash('Product updated!', 'info')
        return redirect(url_for('index'))
    return render_template('edit_product.html', product=product)

@app.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted.', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
