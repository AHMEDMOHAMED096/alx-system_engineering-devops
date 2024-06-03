#!/usr/bin/python3
"""Script that using REST API, retrieves information about
the todo list progress of all employees and exports it to JSON format."""
import json
import requests


def get_all_employees_todo_list():
    """Method to get todo_list data from API for all employees"""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_data = requests.get(users_url).json()
    todos_data = requests.get(todos_url).json()

    return users_data, todos_data


def export_all_to_json(users_data, todos_data):
    """Method to export all todo data to JSON format"""
    data = {}
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")
        data[user_id] = []
        for task in todos_data:
            if task.get("userId") == user_id:
                task_dict = {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                }
                data[user_id].append(task_dict)

    json_filename = "todo_all_employees.json"
    with open(json_filename, "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    users_data, todos_data = get_all_employees_todo_list()
    export_all_to_json(users_data, todos_data)
