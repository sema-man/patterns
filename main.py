# Паттерн Компоновщик (Composite)

class TaskComponent:
    def __init__(self, name):
        self.name = name
        self.observers = []

    def add_task(self, task):
        pass

    def add_task_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, task):
        for observer in self.observers:
            observer.update(task)

    def display_info(self, indent=""):
        pass


class Task(TaskComponent):
    def __init__(self, name):
        super().__init__(name)

    def display_info(self, indent=""):
        print(f"{indent}- {self.name}")


class TaskGroup(TaskComponent):
    def __init__(self, name):
        super().__init__(name)
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_info(self, indent=""):
        print(f"{indent}* {self.name}")
        for task in self.tasks:
            task.display_info(indent + "  ")
            self.notify_observers(task)


# Паттерн Наблюдатель (Observer)

class Observer:
    def update(self, task):
        pass


class Developer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, task):
        print(f"[{self.name}] New task assigned: {task.name}")


class Tester(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, task):
        print(f"[{self.name}] New task assigned: {task.name}")


class Designer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, task):
        print(f"[{self.name}] New task assigned: {task.name}")


# Пример использования

# Создание задач и групп задач
task1 = Task("Implement login functionality")
task2 = Task("Fix bug in registration form")
task3 = Task("Write unit tests for API endpoints")

task4 = Task("Test page performance")
task5 = Task("Stree test database bandwidth")

group1 = TaskGroup("Backend Tasks")
group1.add_task(task1)
group1.add_task(task2)
group1.add_task(task3)

group2 = TaskGroup("Testing Tasks")
group2.add_task(task4)
group2.add_task(task5)

task6 = Task("Create landing page design")
task7 = Task("Design user interface mockups")

group3 = TaskGroup("Frontend Tasks")
group3.add_task(task6)
group3.add_task(task7)

# Добавление задач в группы
group1.add_task(group2)
group1.add_task(group3)

# Руководитель проекта добавляет новые задачи
task8 = Task("Create responsive layout")
task9 = Task("Implement data visualization")

group3.add_task(task8)
group3.add_task(task9)

# Разработчики, тестировщики и дизайнеры подписываются на уведомления о новых задачах
developer1 = Developer("John")
developer2 = Developer("Emily")
developer3 = Developer("Michael")
tester1 = Tester("Alex")
tester2 = Tester("Sophia")
designer1 = Designer("Oliver")
designer2 = Designer("Emma")

group1.add_task_observer(developer1)
group1.add_task_observer(developer2)
group1.add_task_observer(developer3)
group1.add_task_observer(tester1)
group1.add_task_observer(tester2)
group3.add_task_observer(designer1)
group3.add_task_observer(designer2)

# Руководитель проекта добавляет новые задачи в группу
task10 = Task("Implement user authentication")
task11 = Task("Write integration tests for login feature")

group1.add_task(task10)
group2.add_task(task11)

# Вывод информации о задачах
group1.display_info()
