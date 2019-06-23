class User:
    def __init__(self, user_id=1, email=None, password=None, first_name=None, last_name=None, address=None, city=None, state=None, zipcode=None):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
