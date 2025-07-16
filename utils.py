#utils.py
import json
import datetime

def validate(date_text):
    try:
        return datetime.datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        return None

def get_input(last_id):
    name = input("Please Enter the name of the task you want to create: ")
    desc = input("Please enter the details of the task: ")
    cdate = datetime.datetime.now().strftime("%Y-%m-%d")

    while True:
        tempduedate = input("Please enter the due date of this task (YYYY-MM-DD): ")
        parsed_date = validate(tempduedate)
        if not parsed_date:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue

        today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if parsed_date < today:
            print("Date must be today or in the future.")
        else:
            break

    duedate = parsed_date.strftime("%Y-%m-%d")
    status = 'pending'
    return Task(last_id, name, desc, cdate, duedate, status)


def get_last_id():
    try:
        with open('tasklist.json', 'r') as file:
            tasks = json.load(file)
            if tasks:
                return max(task['id'] for task in tasks)
    except (FileNotFoundError,json.JSONDecodeError):
        pass
    return 0


