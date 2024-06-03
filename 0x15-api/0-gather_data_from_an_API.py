#!/usr/bin/python3
"""Script that using REST API, for a given employee ID
returns information about his/her todo list progress."""
import requests
import sys


def get_todo_list_progress(emp_id):
    """Method to get todo_list data from api"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    user_data = requests.get(user_url).json()

    todos_url = f"https://jsonplaceholder.typicode.com/todos"
    todos_data = requests.get(todos_url, params={"userId": emp_id}).json()

    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks\
({number_of_done_tasks}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    emp_id = sys.argv[1]
    get_todo_list_progress(emp_id)
