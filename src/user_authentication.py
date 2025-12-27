from flask_login import login_user, logout_user, current_user

from src.classes.User import User

users = {'admin': {'password': 'admin'}, 'user1': {'password': 'pwd1'}, 'user2': {'password': 'pwd2'}}

def authenticate(username, password):
    if username in users and users[username]['password'] == password:
        user = User(username)
        login_user(user)
        return f'Welcome {current_user.id}. You were logged in.', 200
    else:
        return 'Incorrect username or password', 401

def disauthenticate():
    username = current_user.id
    logout_user()
    return f'Bye {username}. You were logged out.', 200