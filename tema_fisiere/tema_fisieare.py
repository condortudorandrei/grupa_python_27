import os
import datetime as dt


class Task:
    def __init__(self, name, date, person, category):
        self.name = name
        self.date = date
        self.person = person
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.date}, {self.person}, {self.category}"

    def __repr__(self):
        return f'"{self.name}", "{self.date}", "{self.person}", "{self.category}"'


class ToDoList:
    def __init__(self):
        self.task_file = "tema_fisiere_taskuri.txt"
        self.category_file = "tema_fisiere_category.txt"
        self.categories = []
        self.load_categories()

    def load_categories(self):
        with open(self.category_file, "r") as file:
            for line in file:
                if line.strip() != "":
                    self.categories.append(line.strip())

    def write_categories(self):
        with open(self.category_file, "w", encoding="utf-8") as f:
            for category in self.categories:
                f.write(f"{category}\n")

    def add_category(self):
        category = input("Enter category name: ")
        if category in self.categories:
            print("Category already exists")
        else:
            self.categories.append(category)
            self.write_categories()
            print(f"Category added: {category}")

    def show_categories(self):
        if not (os.path.exists(self.category_file)):
            print("Category file does not exist")
            return
        if os.path.getsize(self.category_file) == 0:
            print("Category file empty")
            return
        print("\nCategories:")
        for category in self.categories:
            print(f"- {category}")

    def add_task(self):
        task = input("Enter task name: ")
        date = dt.date.fromisoformat(input("Enter date of task(YYYY-MM-DD || EX: 2025-12-24): "))
        person = input("Enter person responsible: ")
        category = input("Enter category responsible: ")

        if category not in self.categories:
            print("Category does not exist")
            return

        new_task = Task(task, date, person, category)

        with open(self.task_file, "a", encoding="utf-8") as f:
            f.write(str(new_task) + "\n")
            print(f"Task added: {task}")

    def show_tasks(self):
        if not (os.path.exists(self.task_file)):
            print("Task file does not exist")
            return
        if os.path.getsize(self.task_file) == 0:
            print("Task file empty")
            return
        with open(self.task_file, "r", encoding="utf-8") as f:
            for line in f:
                print(f"{line}")

    def load_tasks(self):
        tasks = []
        if os.path.exists(self.task_file):
            with open(self.task_file, "r", encoding="utf-8") as f:
                for line in f:
                    onetask = line.strip().split(",")
                    if len(onetask) == 4:
                        t1 = Task(onetask[0], onetask[1], onetask[2], onetask[3])
                        tasks.append(t1)
        return tasks

    def sort_tasks(self):
        tasks = self.load_tasks()
        if len(tasks) == 0:
            print("Task file empty")
            return

        print("\n===== SORT TASKS =====")
        print("1. Ascending Tasks")
        print("2. Descending Tasks")
        print("3. Ascending Date")
        print("4. Descending Date")
        print("5. Ascending Person")
        print("6. Descending Person")
        print("7. Ascending Category")
        print("8. Descending Category\n")

        i = input("Enter Function: ")

        if i == "1":
            tasks.sort(key=lambda x: x.name.lower())
        elif i == "2":
            tasks.sort(key=lambda x: x.name.lower(), reverse=True)
        elif i == "3":
            tasks.sort(key=lambda x: x.date.lower())
        elif i == "4":
            tasks.sort(key=lambda x: x.date.lower(), reverse=True)
        elif i == "5":
            tasks.sort(key=lambda x: x.person.lower())
        elif i == "6":
            tasks.sort(key=lambda x: x.person.lower(), reverse=True)
        elif i == "7":
            tasks.sort(key=lambda x: x.category.lower())
        elif i == "8":
            tasks.sort(key=lambda x: x.category.lower(), reverse=True)
        else:
            print("Invalid input, please try again!")
            return
        print("\n===== SORT TASKS =====")
        for task in tasks:
            print(f"Task: {task.name}")
            print(f"Date: {task.date}")
            print(f"Person: {task.person}")
            print(f"Category: {task.category}")
            print("----------------------")

    def menu(self):
        while True:
            print("\n======: Function Menu :======")
            print("1. Add task")
            print("2. Show tasks")
            print("3. Add category")
            print("4. Show categories")
            print("5. Deep Menu")
            print("0. Exit")

            i = input("Enter function: ")
            if i == "1":
                print("\n")
                self.add_task()
            elif i == "2":
                print("\n")
                self.show_tasks()
            elif i == "3":
                print("\n")
                self.add_category()
            elif i == "4":
                print("\n")
                self.show_categories()
            elif i == "5":
                print("\n")
                (self.sort_tasks())
            elif i == "0":
                print("\n")
                print("Exiting...")
                break
            else:
                print("\n")
                print("Invalid input, please try again!")


test = ToDoList()
test.menu()
