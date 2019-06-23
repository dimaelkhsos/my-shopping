import db
import sys
import os
import sqlite3
from contextlib import closing

def delete_from_cart(email, product_id):
    db.delete_product(email, product_id)

def get_cart(email):
    products = db.display_cart(email)
    return products

def add_to_cart(e_mail, product_id):
    db.add_in_cart(e_mail, product_id)

def description(productId):
    productData = db.get_description (productId)
    return productData

def display_by_category(categoryId):
    data = db.display_categories(categoryId)
    return data

def display_item_data():
    data = db.display_all_data()
    return data

def display_category_data():
    catData = db.display_cat_data()
    return catData


