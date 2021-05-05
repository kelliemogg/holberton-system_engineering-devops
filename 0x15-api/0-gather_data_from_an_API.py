#!/usr/bin/python3
""" using the REST API for a given employee ID """

import requests
from sys import argv

if __name__ == "__main__":

    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        argv[1])
    employee = requests.get(user).json()

    to_do = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    todo_list = requests.get(to_do)
    
    employee_name = employee.get('name')
    done_list = []

    """ requests """
    for task in todo_list.json():
        if task.get('completed') is True:
            done_list.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_list), len(todo_list))

    for task in todo_list:
        print("\t {}".format(item))
