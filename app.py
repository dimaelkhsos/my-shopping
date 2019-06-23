from flask import *
import sqlite3
import os
from users import *
from db import *
from cart import *
from auxiliary import *


application = Flask(__name__)
application.config['SECRET_KEY'] = 'devkey'

port = int(os.getenv('PORT',8000))


@application.route("/")
def index():
    flag, firstName, cart_total = login_info()
    itemData = display_item_data()
    itemData = get_info(itemData)
    categoryData = display_category_data()
    return render_template('index.html', itemData=itemData, loggedIn=flag, firstName=firstName, noOfItems=cart_total, categoryData=categoryData)

@application.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        address = request.form['address']
        zipcode = request.form['zipcode']
        city = request.form['city']
        state = request.form['state']

        if validate_form(email, first_name, last_name, zipcode):
            add_user(email, password, first_name, last_name, address, city, state, zipcode)
            message = "You were successfully registered."
            return render_template("signin.html", error = message)
        else:
            message = "Registration failed. Your email should contain @, your first name and last name should only contain letters, and your zipcode should only contain numerical values. Please try again."
            return render_template("create-account.html", error = message)
        
@application.route("/registration")
def registrationForm():
    return render_template("create-account.html")

@application.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

@application.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if db.valid_login(email, password):
            session['email'] = email
            return redirect(url_for('index'))
        else:
            error = 'Invalid UserId / Password'
            return render_template('signin.html', error=error)

@application.route("/loginForm")
def loginForm():
    if 'email' in session:
        return redirect(url_for('index'))
    else:
        return render_template('signin.html', error='')

    
@application.route("/remove")
def removeFromCart():
    if 'email' not in session:
        return redirect(url_for('loginForm'))
    email = session['email']
    product_id_to_delete = int(request.args.get('productId'))
    delete_from_cart(email, product_id_to_delete)
    return redirect(url_for('cart'))

@application.route("/cart")
def cart():
    if 'email' not in session:
        return redirect(url_for('loginForm'))
    flag, firstName, cart_total = login_info()
    email = session['email']
    products = get_cart (email)
    totalPrice = 0
    for row in products:
        totalPrice += row[2]
    totalPrice = round(totalPrice, 2)
    return render_template("shopping_cart.html", products = products, totalPrice=totalPrice, loggedIn=flag, firstName=firstName, noOfItems=cart_total)

@application.route("/addToCart")
def addToCart():
    if 'email' not in session:
        return redirect(url_for('loginForm'))
    else:
        product_id = int(request.args.get('productId'))
        e_mail = session['email']
        add_to_cart(e_mail, product_id)
        return redirect(url_for('index'))

@application.route("/display_cat")
def displayCategory():
        flag, firstName, cart_total = login_info()
        categoryId = request.args.get("categoryId")
        data = display_by_category(categoryId)
        categoryName = data[0][4]
        data = get_info(data)
        categoryData = display_category_data()
        return render_template('products_by_category.html', categoryData = categoryData, data=data, loggedIn=flag, firstName=firstName, noOfItems=cart_total, categoryName=categoryName)


if __name__ == "__main__":
    if os.getenv('PORT') is None:
        application.run()
    else:
        application.run(host='0.0.0.0', port=port, debug=True)
                    


    
