#!/usr/bin/python3
""" This module exports to json string """
import json
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
    users = requests.get(user_url).json()
    file = '{}.json'.format(id)
    tasks = requests.get(url).json()
    retrieve = []

    for task in tasks:
        collect = {}
        collect['task'] = task.get('title')
        collect['completed'] = task.get('completed')
        collect['username'] = users.get('username')
        retrieve.append(collect)
    collected = {}
    collected[id] = retrieve

    with open(file, 'w') as f:
        json.dump(collected, f)
