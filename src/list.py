import json

from flask_login import current_user

lists = {'admin': {'iphone', 'mac'}}

def show_list():
    my_list = list(lists[current_user.id])
    return json.dumps(my_list)