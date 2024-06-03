#!/usr/bin/python3
"""Script that using REST API, for a given employee ID
returns information about his/her todo list progress."""
import requests
import sys
import csv


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
    return user_data, todos_data


def export_to_csv(user_data, todos_data):
    """Method to export data to CSV format"""
    user_id = user_data.get("id")
    username = user_data.get("username")
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow(
                [user_id, username, task.get("completed"), task.get("title")]
            )


if __name__ == "__main__":
    emp_id = sys.argv[1]
    user_data, todos_data = get_todo_list_progress(emp_id)
    export_to_csv(user_data, todos_data)
