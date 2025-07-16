#main.py

from task_manager import TaskManager
from utils import get_input,validate,get_last_id
from task import Task



if __name__ == "__main__":
    DummyTask = Task(0,'','','','','')
    manager = TaskManager(DummyTask)

    print("Your Todo List")

    while True:
        print('-' * 30)
        try:
            choice = int(input("1.Add Task\n2.Update Task\n3.Delete Task\n4.View Tasks\n5.Mark As Done\n6.Mark As Pending\n0.Exit\nYour Choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            last_id = get_last_id()
            task = get_input(last_id)
            manager = TaskManager(task)
            manager.addtask()
        elif choice == 2:
            while True:
                print('-' * 30)
                try:
                    second_choice = int(input("1.Update Due Date\n2.Update Name\n3.Update Desc\n0.Exit\nYour Choice: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if second_choice == 1:
                    try:
                        task_id = int(input("Enter the task id of the task you want to update: "))
                        manager.updateduedate(task_id)
                    except ValueError:
                        print("Invalid task ID.")
                elif second_choice == 2:
                    try:
                        task_id = int(input("Enter the task id of the task you want to update: "))
                        new_name = input("Enter the new name: ")
                        manager.updatename(task_id, new_name)
                    except ValueError:
                        print("Invalid task ID.")
                elif second_choice == 3:
                    try:
                        task_id = int(input("Enter the task id of the task you want to update: "))
                        new_desc = input("Enter the new description: ")
                        manager.updatedesc(task_id, new_desc)
                    except ValueError:
                        print("Invalid task ID.")
                elif second_choice == 0:
                    break
                else:
                    print("Invalid input.")
        elif choice == 3:
            try:
                task_tobe_deleted = int(input("Enter the id of the task to be deleted: "))
                manager.deletetask(task_tobe_deleted)
            except ValueError:
                print("Invalid task ID.")
        elif choice == 4:
            while True:
                try:
                    third_choice = int(input("1.All\n2.Completed\n3.Pending\n0.Exit\nYour Choice: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if third_choice == 1:
                    manager.viewtasks()
                elif third_choice == 2:
                    manager.view_completed_tasks()
                elif third_choice == 3:
                    manager.view_pending_tasks()
                elif third_choice == 0:
                    break
                else:
                    print("Invalid input.")
        elif choice == 5:
            try:
                mark = int(input("Enter the task ID of the task you want to mark as complete: "))
                manager.markasdone(mark)
            except ValueError:
                print("Invalid task ID.")
        elif choice == 6:
            try:
                pmark = int(input("Enter the task ID of the task you want to mark as pending: "))
                manager.markaspending(pmark)
            except ValueError:
                print("Invalid task ID.")
        elif choice == 0:
            break
        else:
            print("Invalid input.")
