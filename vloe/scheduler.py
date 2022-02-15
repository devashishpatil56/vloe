import logging

LOG_LEVEL = logging.INFO


class Task:
    def __init__(self, name: str) -> None:
        self.name = name
        self.dependencies = []
        self.dependents = []
        self.dependencies_met = False
        self.dependents_met = False

    def add_dependency(self, task: 'Task') -> None:
        self.dependencies.append(task)
        task.dependents.append(self)

    def run(self):
        logging.info("Running task: %s", self.name)

class Scheduler:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def run(self) -> None:
        while len(self.tasks) > 0:
            for task in self.tasks:
                if task.dependencies_met and not task.dependents_met:
                    task.run()
                    self.tasks.remove(task)
                    for dependent in task.dependents:
                        dependent.dependencies_met = True
                    break
