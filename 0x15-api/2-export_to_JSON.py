#!/usr/bin/python3
""" using the REST API and exporting data to a CSV """

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    """ User ID, employee info, and employee name """
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    employee = requests.get(user).json()
    employee_name = employee.get('username')
    """ To do list data based on user ID """
    to_do = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    todo_list = requests.get(to_do).json()

    """ json file format per task req """
    J_file = "{}.json".format(argv[1])

    """ list of task, tast status, and the owner of task
        to be the values to the key aka USER_ID """
    values_list = []
    by_id_dict = {}
    values_dict = {}
    for item in todo_list:
        """ getting items from to do list to populate values_dict """
        values_dict["task"] = item.get('title')
        values_dict["completed"] = item.get('completed')
        values_dict["username"] = employee_name
        """ each task is its own dictionary / now compiling a list of key
        value pairs for each task and its status / ownership """
        values_list.append(values_dict)
        by_id_dict[argv[1]] = values_list

        """ dumps data into json string """
    convert_to_json = json.dumps(by_id_dict)

    with open(J_file, 'w') as f:
        """ writes json string to a file """
        f.write(convert_to_json)
