#task.py


class Task:
    def __init__(self, id, name, desc, cdate, ddate, status):
        self.id = id + 1
        self.name = name
        self.desc = desc
        self.cdate = cdate
        self.ddate = ddate
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "task name": self.name,
            "task description": self.desc,
            "Date Created": self.cdate,
            "Due Date": self.ddate,
            "status": self.status
        }