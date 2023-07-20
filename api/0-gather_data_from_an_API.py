#!/usr/bin/python3
"""
Script that retrieves TODO list progress for a given employee ID from a REST API.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])

    # Fetch employee data
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response_user = requests.get(url_user)
    employee_data = response_user.json()

    # Fetch TODO list data
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response_todo = requests.get(url_todo)
    todo_data = response_todo.json()

    # Get completed tasks and total tasks count
    completed_tasks = [task for task in todo_data if task['completed']]
    total_tasks = len(todo_data)

    # Print employee progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_data['name'], len(completed_tasks), total_tasks)
    )

    # Print completed task titles
    for task in completed_tasks:
        print("\t{}".format(task['title']))
