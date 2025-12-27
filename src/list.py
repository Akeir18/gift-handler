import json

from flask_login import current_user

# lists = {'admin': {'iPhone', 'mac'}}
lists = {}

def show_list():
    my_list = list(lists[current_user.id])
    return json.dumps(my_list)

def create_list(items):
    lists[current_user.id] = set()
    for item in items:
        lists[current_user.id].add(item)


def add_to_list(items):
    if current_user.id not in items:
        lists[current_user.id] = set()
    for item in items:
        lists[current_user.id].add(item)

def remove_from_list(items):
    if current_user.id not in items:
        lists[current_user.id] = set()
    for item in items:
        if item in lists[current_user.id]:
            lists[current_user.id].remove(item)

def show_user_list(username):
    my_list = list(lists[username])
    return json.dumps(my_list)