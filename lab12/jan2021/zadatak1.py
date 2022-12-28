import json
from pathlib import Path
from sys import stderr
from pprint import pprint
from collections import defaultdict
from random import randint, seed
import csv
from zadatak2 import execution_logger


def read_from_json(fpath):
    try:
        with open(fpath, 'r') as fobj:
            return json.load(fobj)
    except FileNotFoundError:
        stderr.write(f"File {fpath} cannot be found\n")
    except OSError as err:
        stderr.write(f"The following error occurred while reading from {fpath}\n{err}\n")


@execution_logger
def top_achievers(fpath):

    todos = read_from_json(fpath)

    users_dict = defaultdict(int)
    for todo in todos:
        if todo['completed']:
            users_dict[todo['userId']] += 1

    max_completed = max(users_dict.values())
    # Option 1
    # return [user_id for user_id, completed_cnt in users_dict.items() if completed_cnt==max_completed]
    # Option 2
    return list(filter(lambda user_id: users_dict[user_id] == max_completed, users_dict.keys()))


@execution_logger
def add_task_priorities(fpath):

    todos = read_from_json(fpath)
    seed(2021)
    for t in todos:
        # Option 1
        # t.update({'priority':randint(1,5)})
        # Option 2
        t['priority'] = randint(1,5)

    write_to_json(Path.cwd() / 'prioritised_todos.json', todos)


def write_to_json(fpath, obj):
    try:
        with open(fpath, 'w') as fobj:
            json.dump(obj, fobj, indent=4)
    except OSError as err:
        stderr.write(f"The following error occurred while writing to {fpath}\n{err}\n")


@execution_logger
def incomplete_tasks(fpath):

    prioritised_todos_list = read_from_json(fpath)

    users_dict = defaultdict(list)
    for todo in prioritised_todos_list:
        if not todo['completed']:
            users_dict[todo['userId']].append(todo)

    todos_dir = Path.cwd() / 'member_assignments'
    todos_dir.mkdir(exist_ok=True)

    for user_id, todos in users_dict.items():
        fpath = todos_dir / f"{user_id}.csv"
        todos.sort(key=lambda todo: todo['priority'])
        write_to_csv(todos, fpath)


def write_to_csv(todos, fpath):
    try:
        with open(fpath, 'w', newline='') as fobj:
            csv_writer = csv.writer(fobj)
            csv_writer.writerow(('task_id', 'task_priority', 'task_title'))
            for todo in todos:
                csv_writer.writerow((todo['id'], todo['priority'], todo['title']))
    except OSError as err:
        stderr.write(f"The following error occurred while writing to {fpath}\n{err}\n")


if __name__ == '__main__':

    todos_file = Path.cwd() / 'data' / 'todos.json'

    top_team_members = top_achievers(todos_file)
    print("Team members with the highest number of completed tasks:")
    for member in top_team_members:
        print(member)

    add_task_priorities(todos_file)
    for task in read_from_json(Path.cwd() / 'prioritised_todos.json'):
        pprint(task)

    incomplete_tasks(Path.cwd() / 'prioritised_todos.json')