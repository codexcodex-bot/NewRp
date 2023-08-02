from flask import render_template, redirect, url_for, flash, request
from website_project import app
from website_project.models.User import User
from website_project.models.Product import Product
from website_project.models.Order import Order
from website_project.utils.database import db_session
from website_project.utils.helpers import login_required, logout_user, login_user

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            flash('loginSuccess')
            return redirect(url_for('dashboard'))
        else:
            flash('loginFailure')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_user = User(request.form['email'], request.form['password'])
        db_session.add(new_user)
        db_session.commit()
        flash('registerSuccess')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/product/<int:product_id>')
def product(product_id):
    product = Product.query.get(product_id)
    return render_template('product.html', product=product)

@app.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    if request.method == 'POST':
        order = Order(user_id=current_user.id, product_id=request.form['product_id'])
        db_session.add(order)
        db_session.commit()
        flash('addToCartSuccess')
    return render_template('cart.html')

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    if request.method == 'POST':
        flash('orderPlaced')
        return redirect(url_for('index'))
    return render_template('checkout.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))