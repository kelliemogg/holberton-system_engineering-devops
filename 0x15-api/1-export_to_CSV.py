#!/usr/bin/python3
""" using the REST API and exporting data to a CSV """

import csv
import requests
from sys import argv

if __name__ == "__main__":

    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        argv[1])
    employee = requests.get(user).json()
    employee_name = employee.get('name')

    to_do = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    todo_list = requests.get(to_do).json()

    new_file = "{}.csv".format(argv[1])
    row_list = []
    with open(new_file, 'w') as f:
        f.write("")
    for task in todo_list:
        status = task.get('complete')
        task_name = task.get('title')
        with open(new_file, 'a') as f:
            new_csv = csv.writer(f)
            row_list.append("{}".format(argv[1]))
            row_list.append("{}".format(employee_name))
            row_list.append("{}".format(status))
            row_list.append("{}".format(task_name))
            new_csv.writerow(row_list)