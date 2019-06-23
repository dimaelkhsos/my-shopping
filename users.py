import db
from objects import User

def add_user(email, password, first_name, last_name, address, city, state, zipcode):
    db.connect()
    user = User(email=email, password=password, first_name=first_name, last_name=last_name, address=address, city=city, state=state, zipcode=zipcode)
    db.register(user)
    print ("You were successfully registered!")
    
