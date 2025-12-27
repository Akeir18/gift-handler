from flask import Flask, request
from flask_login import LoginManager, login_required

from src.classes.User import User
from src.list import show_list, add_to_list, remove_from_list, create_list
from src.user_authentication import authenticate, disauthenticate

app = Flask(__name__)
app.secret_key = 'secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

# Load user by ID
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# User login
@app.route('/login', methods=['POST'])
def login():
    # if request.method == 'POST':
    body = request.get_json()
    username = body.get('username')
    password = body.get('password')
    return authenticate(username, password)

# User logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    return disauthenticate()

@app.route('/list', methods=['GET'])
@login_required
def get_list():
    return show_list()

@app.route('/list', methods=['PUT'])
@login_required
def put_list():
    body = request.get_json()
    create_list(body.get('list'))
    return show_list()

@app.route('/list', methods=['PATCH'])
@login_required
def update_list():
    body = request.get_json()
    add = body.get('add')
    if add:
        add_to_list(body.get('add'))
    remove = body.get('remove')
    if remove:
        remove_from_list(body.get('remove'))
    return show_list()


if __name__ == '__main__':
    app.run(debug=True)