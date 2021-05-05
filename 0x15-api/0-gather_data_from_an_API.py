#!/usr/bin/python3
""" using the REST API for a given employee ID """

import json
import requests
import sys

if __name__ == "__main__":
    employee_ID = sys.argv[1]
    to_do = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        employee_ID)
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_ID)

    todo_req = requests.get(to_do)
    user_req = requests.get(user).json()
    employee_name = user_req['name']
    check = 0
    total = 0
    todo_list = []

    for task in todo_req.json():
        done = task['completed']
        item = task['title']
        total = total + 1
        if done:
            todo_list.append(item)
            check = check + 1

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done, total))

    for item in todo_list:
        print("\t {}".format(item))
