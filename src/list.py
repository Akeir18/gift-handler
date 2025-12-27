import json

from flask_login import current_user

lists = {'admin': {'iPhone', 'mac'}}

def show_list():
    my_list = list(lists[current_user.id])
    return json.dumps(my_list)

def add_to_list(items):
    for item in items:
        lists[current_user.id].add(item)

def remove_from_list(items):
    for item in items:
        if item in lists[current_user.id]:
            lists[current_user.id].remove(item)