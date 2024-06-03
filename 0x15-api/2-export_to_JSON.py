#!/usr/bin/python3
"""Script that using REST API, for a given employee ID
returns information about his/her todo list progress."""
import requests
import json
import sys


def get_todo_list_progress(emp_id):
    """Method to get todo_list data from api"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    user_data = requests.get(user_url).json()

    todos_url = f"https://jsonplaceholder.typicode.com/todos"
    todos_data = requests.get(todos_url, params={"userId": emp_id}).json()
    return user_data, todos_data


def export_to_json(user_data, todos_data):
    """Method to export data to JSON format"""
    user_id = user_data.get("id")
    username = user_data.get("username")
    json_filename = f"{user_id}.json"

    tasks_list = []
    for task in todos_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        tasks_list.append(task_dict)

    data = {user_id: tasks_list}
    with open(json_filename, "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    emp_id = sys.argv[1]
    user_data, todos_data = get_todo_list_progress(emp_id)
    export_to_json(user_data, todos_data)
