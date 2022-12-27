#!/usr/bin/python3
""" This module writes from an API to JSON file """
import json
import requests

if __name__ == '__main__':
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    url = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(user_url).json()
    file = '{}.json'.format(id)
    tasks = requests.get(url).json()
    username = {}
    employee = {}

    for user in users:
        employee[user.get('id')] = []
        username[user.get('id')] = user.get('username')
    for task in tasks:
        collect = {}
        collect['task'] = task.get('title')
        collect['completed'] = task.get('completed')
        collect['username'] = username.get(task.get('userId'))
        employee.get(task.get('userId')).append(collect)

    with open('todo_all_employees.json', 'w') as everything:
        json.dump(employee, everything)
