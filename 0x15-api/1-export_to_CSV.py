#!/usr/bin/python3
""" using the REST API and exporting data to a CSV """

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv


    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        argv[1])
    employee = requests.get(user).json()
    employee_name = employee.get('username')

    to_do = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    todo_list = requests.get(to_do).json()

    new_file = "{}.csv".format(argv[1])
    with open(new_file, 'w') as f:
        f.write("")
    for task in todo_list:
        status = task.get('completed')
        task_name = task.get('title')
        id_num = argv[1]
        with open(new_file, 'a', newline='') as f:
            new_csv = csv.writer(f, quoting=csv.QUOTE_ALL)
            row_list = []
            row_list.append(id_num)
            row_list.append(employee_name)
            row_list.append(status)
            row_list.append(task_name)
            new_csv.writerow(row_list)