from project.task import Task
from typing import List

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for t in self.tasks:
            if t == task_name:
                t.completed = True
                return
        return f"Could not find task with name {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        info = [f"Section {self.name}:"]
        for task in self.tasks:
            info.append(task.details())
        return '\n'.join(info)

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
