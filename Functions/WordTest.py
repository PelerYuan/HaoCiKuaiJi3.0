import logging
import os

def delete_test_data(group_name):
    try:
        os.remove(f'./data/words/{group_name}.csv')
    except FileNotFoundError as e:
        logging.log(logging.ERROR, e)

def rename_group(old_group_name, new_group_name):
    new_group_name = check_name(new_group_name)
    try:
        os.rename(f'./data/words/{old_group_name}.csv', f'./data/words/{new_group_name}.csv')
    except FileNotFoundError as e:
        logging.log(logging.ERROR, e)

def new_group(group_name):
    group_name = check_name(group_name)
    with open(f'./data/words/{group_name}.csv', 'w', newline='') as file:
        group = WordGroup(group_name)

def open_group(group_name):
    return WordGroup(group_name)

def check_name(group_name):
    while group_name in get_all_group():
        group_name += '_'
    return group_name
