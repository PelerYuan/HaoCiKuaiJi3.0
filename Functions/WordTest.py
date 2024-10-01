import logging
import os


def new_test_data(test_name):
    test_name = check_name(test_name)
    with open(f'./data/test/{test_name}.csv', 'w', newline='') as file:
        ...


def delete_test_data(test_name):
    try:
        os.remove(f'./data/test/{test_name}.csv')
    except FileNotFoundError as e:
        logging.log(logging.ERROR, e)


def rename_group(old_test_name, new_test_name):
    new_test_name = check_name(new_test_name)
    try:
        os.rename(f'./data/test/{old_test_name}.csv', f'./data/test/{new_test_name}.csv')
    except FileNotFoundError as e:
        logging.log(logging.ERROR, e)


def check_name(test_name):
    while f'{test_name}.csv' in os.listdir(f'./data/test/'):
        test_name += '_'
    return test_name
