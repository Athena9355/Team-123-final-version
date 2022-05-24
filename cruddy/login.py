from flask_login import logout_user, login_user, current_user

from __init__ import login_manager
from cruddy.model import Users
from cruddy.query import users_all, user_by_email


# check credentials in database
def is_user(email, password):
    # query email and return user record
    user_record = user_by_email(email)
    # if user record found, check if password is correct
    return user_record and Users.is_password_match(user_record, password)


# login user based off of email and password
def login(email, password):
    # sequence of checks
    if current_user.is_authenticated:  # return true if user is currently logged in
        return True
    elif is_user(email, password):  # return true if email and password match
        user_row = user_by_email(email)
        login_user(user_row)  # sets flask login_user
        return True
    else:  # default condition is any failure
        return False


# this function is needed for Flask-Login to work.

@login_manager.user_loader
def user_loader(user_id):
    """Check if user login status on each page protected by @login_required."""
    if user_id is not None:
        return Users.query.get(user_id)
    return None


# Authorise new user requires user_name, email, password
def authorize(name, email, password):
    if is_user(email, password):
        return False
    else:
        auth_user = Users(
            name=name,
            email=email,
            password=password,
            phone="1234567890"  # this should be added to authorize.html
        )
        # encrypt their password and add it to the auth_user object
        auth_user.create()
        return True


# logout user
def logout():
    logout_user()  # removes login state of user from session


# Test some queries from implementations above
if __name__ == "__main__":

    # Look at table
    print("Print all at start")
    for user in users_all():
        print(user)
    print()

    """ Password Lookup Sample Code """
    # Expected success on Email and Password lookup
    name = "Thomas Edison"
    email = "tedison@example.com"
    psw = "123toby"
    print(f"Check is_user with valid email and password {email}, {psw}", is_user(email, psw))

    # Expected failure on Email and Password lookup
    psw1 = "1234puffs"
    print(f"Check is_user with invalid password: {email}, {psw1}", is_user(email, psw1))

    """ Authorization Screen Sample Code"""
    # Expected failure as user exists
    print(f"Check authorize with existing email and password: {name}, {psw}", authorize(name, email, psw))

    # Expected success as user does not exist
    name1 = "Coco Puffs"
    email1 = "puffs@example.com"
    print(f"Check authorize with new email and password: {name1}, {psw1}", authorize(name1, email1, psw1))

    # Look at table
    print()
    print("Print all at end")
    for user in users_all():
        print(user)

    # Clean up data from run, so it can run over and over the same
    user_record = user_by_email(email1)
    user_record.delete()