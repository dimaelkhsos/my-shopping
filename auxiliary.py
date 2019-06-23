from flask import *
import sqlite3
import os
from users import *
from db import *


def validate_form(email, first_name, last_name, zipcode):
    e_mail = email.strip()
    firstname = first_name.strip()
    lastname = last_name.strip()
    zip_code = zipcode.strip()

    at_index = e_mail.find("@")
    if at_index!=-1:
        flag1= True
    else:
        flag1=False

    if firstname.isalpha():
        flag2 = True
    else:
        flag2 = False

    if lastname.isalpha():
        flag3 = True
    else:
        flag3 = False

    if zipcode.isdigit():
        flag4 = True
    else:
        flag4 = False

    if flag1 and flag2 and flag3 and flag4:
        return True
    else:
        return False
    
def login_info():
    flag, name, cart_total = db.get_user_details()
    return (flag, name, cart_total)


def get_info(data):
    info = []
    i = 0
    while i < len(data):
        curr = []
        for j in range(7):
            if i >= len(data):
                break
            curr.append(data[i])
            i += 1
        info.append(curr)
    return info  
    
