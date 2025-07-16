#task_manager.py

import json
import datetime
from utils import validate

class TaskManager():
    def __init__(self,task):
        self.task = task

    def addtask(self):
        try:
            with open('tasklist.json', 'r') as file:
                content = file.read()
                tasks = json.loads(content) if content.strip() else []
        except FileNotFoundError:
            tasks = []

        tasks.append(self.task.to_dict())

        with open('tasklist.json', 'w') as file:
            json.dump(tasks, file, indent=4)

    def viewtasks(self):
        try:
            with open('tasklist.json', 'r') as file:
                content = file.read().strip()
                if not content:
                    print("Task list is empty")
                    return
                tasks = json.loads(content)

            if not tasks:
                print('-' * 30)
                print("No tasks found.")
                print('-' * 30)
            else:
                for task in tasks:
                    print("-" * 30)
                    print(f"ID: {task['id']}")
                    print(f"Name: {task['task name']}")
                    print(f"Description: {task['task description']}")
                    print(f"Created On: {task['Date Created']}")
                    print(f"Due Date: {task['Due Date']}")
                    print(f"Status: {task['status']}")
                    print("-" * 30)


        except FileNotFoundError:
            print("No tasklist found.")

    def view_completed_tasks(self):
        try:
            with open('tasklist.json', 'r') as file:
                content = file.read().strip()
                if not content:
                    print("Task list is empty")
                    return
                tasks = json.loads(content)

            found=False
            if not tasks:
                print('-' * 30)
                print("No tasks found.")
                print('-' * 30)
            else:
                for task in tasks:
                    if task['status'] == 'completed':
                        print('-' * 30)
                        print(f"ID: {task['id']}")
                        print(f"Name: {task['task name']}")
                        print(f"Description: {task['task description']}")
                        print(f"Created On: {task['Date Created']}")
                        print(f"Due Date: {task['Due Date']}")
                        print(f"Status: {task['status']}")
                        print("-" * 30)
                        found=True

            if not found:
                print("No tasks completed")

        except FileNotFoundError:
            print("No tasklist found.")

    def view_pending_tasks(self):
        try:
            with open('tasklist.json', 'r') as file:
                content = file.read().strip()
                if not content:
                    print("Task list is empty")
                    return
                tasks = json.loads(content)

            found = False
            if not tasks:
                print('-' * 30)
                print("No tasks found.")
                print('-' * 30)
            else:
                for task in tasks:
                    if task['status'] == 'pending':
                        print('-' * 30)
                        print(f"ID: {task['id']}")
                        print(f"Name: {task['task name']}")
                        print(f"Description: {task['task description']}")
                        print(f"Created On: {task['Date Created']}")
                        print(f"Due Date: {task['Due Date']}")
                        print(f"Status: {task['status']}")
                        print("-" * 30)
                        found = True

            if not found :
                print("Yayyy no tasks pending!!!")


        except FileNotFoundError:
            print("No tasklist found.")

    def markasdone(self,task_id):

        try:
            with open('tasklist.json','r') as file:
                content = json.load(file)
            if not content:
                print('no task found')
            else:
                for task in content:
                    if task['id'] == task_id:
                        task['status'] = 'completed'

                with open('tasklist.json','w') as wfile:
                    json.dump(content,wfile,indent = 4)
        except FileNotFoundError:
            print("No tasklist found")

    def deletetask(self, task_id):
        try:
            with open('tasklist.json', 'r') as file:
                content = file.read().strip()
                if not content:
                    print(" File is empty. Nothing to delete.")
                    return
                tasks = json.loads(content)
        except FileNotFoundError:
            print("File does not exist.")
            return
        except json.JSONDecodeError:
            print("JSON is invalid.")
            return

        found = False
        updated_tasks = []

        for task in tasks:
            if task['id'] == task_id:
                found = True
            else:
                updated_tasks.append(task)

        if found:
            with open('tasklist.json', 'w') as file:
                json.dump(updated_tasks, file, indent=4)
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            print("No such task found.")

    def updatedesc(self,task_id,new_desc):
        try:
            with open("tasklist.json" , 'r') as file:
                content = file.read().strip()
                if not content:
                    print("This File is empty")
                    return
                tasks = json.loads (content)

            found = False
            for task in tasks:
                if task['id'] == task_id:
                    task['task description'] = new_desc
                    found = True
            if not found:
                print("task not found")

            with open('tasklist.json','w') as file:
                json.dump (tasks,file,indent = 4)
        except FileNotFoundError:
            print("File Not Found")

    def updatename(self,task_id,new_name):
        try:
            with open("tasklist.json" , 'r') as file:
                content = file.read().strip()
                if not content:
                    print("This File is empty")
                    return
                tasks = json.loads (content)

            found = False
            for task in tasks:
                if task['id'] == task_id:
                    task['task name'] = new_name
                    found = True
            if not found:
                print("task not found")

            with open('tasklist.json','w') as file:
                json.dump (tasks,file,indent = 4)
        except FileNotFoundError:
            print("File Not Found")

    def updateduedate(self,task_id):
            try:
                with open("tasklist.json" , 'r') as file:
                    content = file.read().strip()
                    if not content:
                        print("This File is empty")
                        return
                    tasks = json.loads (content)

                found = False
                for task in tasks:
                    if task['id'] == task_id:
                        while True:
                            tempduedate = input("enter the new date: ")
                            parsed_date = validate(tempduedate)
                            if not parsed_date:
                                print("Invalid date format. Please use YYYY-MM-DD.")
                                continue

                            today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                            if parsed_date < today:
                                print("Date must be today or in the future.")
                            else:
                                break

                        task['Due Date'] = parsed_date.strftime("%Y-%m-%d")
                        found = True
                if not found:
                    print("task not found")

                with open('tasklist.json','w') as file:
                    json.dump (tasks,file,indent = 4)
            except FileNotFoundError:
                print("File Not Found")

    def markaspending(self,task_id):

        try:
            with open('tasklist.json','r') as file:
                content = json.load(file)
            if not content:
                print('no task found')
            else:
                for task in content:
                    if task['id'] == task_id:
                        task['status'] = 'pending'

                with open('tasklist.json','w') as wfile:
                    json.dump(content,wfile,indent = 4)
        except FileNotFoundError:
            print("No tasklist found")




