#!/usr/bin/python3
""" using the REST API and export data in JSON format
    output desired is a dictionary of 10 users where the key
    is their USER ID and the values are a dictionary list of
    tasks and details """

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    """ detailed records of all 10 users """
    all_users = 'https://jsonplaceholder.typicode.com/users'
    empl_names = requests.get(all_users).json()
    filename = "todo_all_employees.json"
    """ a dict of 10 users whos values are a dictionary list
    of to do lists for each of those 10 users """
    big_dict = {}
    for employee in empl_names:
        """ searches through for the key 'id' """
        user_ID = employee.get('id')
        todos = 'https://jsonplaceholder.typicode.com/todos'
        """ records of 10 users to do lists """
        todo_list = requests.get(todos).json()
        big_dict[user_ID] = {} 
        """ list of task, task status, and the owner of task
        to be the values to the key aka USER_ID """
        values_list = []
        by_id_dict = {}
        for item in todo_list:
            values_dict = {}
            """ getting items from to do list to populate values_dict """
            values_dict["task"] = item.get('title')
            values_dict["completed"] = item.get('completed')
            values_dict["username"] = empl_names
            """ each task is its own dictionary / now compiling a list of key
            value pairs for each task and its status / ownership """
            values_list.append(values_dict)
            by_id_dict[user_ID] = values_list
            """ dumps data into json string """
            big_dict[user_ID] = by_id_dict
            
            
        convert_to_json = json.dumps(big_dict)

    with open(filename, 'w') as f:
        f.write(convert_to_json)
