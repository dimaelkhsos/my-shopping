from flask import *
import sys
import os
import sqlite3
from contextlib import closing


conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "shopping_cart_db.db"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()


def register(user):
     with sqlite3.connect('shopping_cart_db.db') as conn:
            cur = conn.cursor()
            sql = '''INSERT INTO Users (email, password, first_name, last_name, address, city, state, zipcode) 
             VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            cur.execute(sql, (user.email, user.password, user.first_name, user.last_name, user.address, user.city, user.state, user.zipcode))
            conn.commit()
     conn.close()

def valid_login(email, password):
        con = sqlite3.connect('shopping_cart_db.db')
        sql = '''SELECT email, password FROM Users'''
        cur = con.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        for row in data:
            if row[0] == email and row[1] == password:
                return True
        return False

def display_categories(categoryId):
    with sqlite3.connect('shopping_cart_db.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT Products.product_id, Products.name, Products.price, Products.picture, Products.description, Categories.category_name FROM Products, Categories WHERE Products.category_id = Categories.category_id AND Categories.category_id = " + categoryId)
        data = cur.fetchall()
    conn.close()
    return data

def display_all_data():
    with sqlite3.connect('shopping_cart_db.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT product_id, name, price, description, picture FROM Products')
        itemData = cur.fetchall()
        return itemData

def display_cat_data():
    with sqlite3.connect('shopping_cart_db.db') as conn:
            cur = conn.cursor()
            cur.execute('SELECT category_id, category_name FROM Categories')
            categoryData = cur.fetchall()
            return categoryData

def get_description(productId):
    with sqlite3.connect('shopping_cart_db.db') as conn:
            cur = conn.cursor()
            cur.execute('SELECT product_id, name, price, description, picture FROM Products WHERE product_id = ' + str(productId))
            productData = cur.fetchone()
    conn.close()
    return productData

def add_in_cart(e_mail, product_id):
    with sqlite3.connect('shopping_cart_db.db') as conn:
                cur = conn.cursor()
                cur.execute("SELECT user_id FROM Users WHERE email = '" + e_mail + "'")
                user_id = cur.fetchone()[0]
                try:
                    cur.execute("INSERT INTO Cart (user_id, product_id) VALUES (?, ?)", (user_id, product_id))
                    conn.commit()
                    msg = "Added successfully"
                except:
                    conn.rollback()
                    msg = "Error occured"
    conn.close()

def display_cart(email):
    with sqlite3.connect('shopping_cart_db.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT user_id FROM Users WHERE email = '" + email + "'")
        userId = cur.fetchone()[0]
        cur.execute("SELECT Products.product_id, Products.name, Products.price, Products.picture FROM Products, Cart WHERE Products.product_id = Cart.product_id AND Cart.user_id = " + str(userId))
        products = cur.fetchall()
    return products

def delete_product(email, product_id):
    with sqlite3.connect('shopping_cart_db.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT user_id FROM Users WHERE email = '" + email + "'")
            user_id = cur.fetchone()[0]
            try:
                cur.execute("DELETE FROM Cart WHERE user_id = " + str(user_id) + " AND product_id = " + str(product_id))
                conn.commit()
                msg = "removed successfully"
            except:
                conn.rollback()
                msg = "error occured"
    conn.close()

def get_user_details():
    with sqlite3.connect('shopping_cart_db.db') as conn:
        cur = conn.cursor()
        if 'email' not in session:
            flag = False
            name = ''
            cart_total = 0
        else:
            flag = True
            cur.execute("SELECT user_id, first_name FROM Users WHERE email = '" + session['email'] + "'")
            userId, name = cur.fetchone()
            cur.execute("SELECT count(product_id) FROM Cart WHERE user_id = " + str(userId))
            cart_total = cur.fetchone()[0]
    conn.close()
    return (flag, name, cart_total)



