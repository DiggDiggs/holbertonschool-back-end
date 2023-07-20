#!/usr/bin/python3
"""
Script that retrieves TODO list given employee ID from a REST API.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])

    # Fetch employee data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)
    employee_data = user_response.json()

    # Fetch TODO list data
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Get completed tasks and total tasks count
    completed_tasks = [task for task in todo_data if task['completed']]
    total_tasks = len(todo_data)

    # Print employee progress
    employee_progress = "Employee {} is done with tasks({}/{}):".format(
        employee_data['name'], len(completed_tasks), total_tasks
    )
    print(employee_progress)

    # Print completed task titles
    for task in completed_tasks:
        print("\t{}".format(task['title']))
