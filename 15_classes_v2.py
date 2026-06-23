from pprint import pprint
from enum import Enum


# clase, liste de obiecte ale claselor si actiuni comune ale claselor

# categories = ["curs", "cumparaturi"]


class Categories(Enum):
    COURSE = "Course"
    SHOPPING = "Shopping"
    WORK = "Work"
    PRESENTS = "Presents"


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


# print(Categories.WORK.value)
# print(Categories.COURSE.name)

# current_category = Categories.WORK
# if current_category == Categories.WORK:
#     print("Work")
# else:
#     print("Presents")


class Task:
    def __init__(self, title, date, owner, category):
        self.title = title
        self.date = date
        self.owner = owner
        self.category = category

    def __str__(self):
        return f"{self.title}, {self.date}, {self.owner}, {self.category}"

    def __repr__(self):
        return f"Task(\"{self.title}\", \"{self.date}\", \"{self.owner}\", {self.category})"


task1 = Task("Homework", "23.June", "John", Categories.COURSE)
print(task1)

task2 = Task("Wash Dishes", "23.June", "John", Categories.WORK)

task3 = Task("Buy Shoes", "24.June", "Ellie", Categories.SHOPPING)


# todo_list = [task1, task2, task3]


class Todos:
    def __init__(self):
        self.todos_list = []

    def add_task(self, task):
        x = 1
        for elem in self.todos_list:
            if elem.title == task.title:
                x = 0
        if x == 1:
            self.todos_list.append(task)
        else:
            print(f"\n\nTask with this title already exists! ({elem.title})\n\n")

    def remove_task(self, task):
        for elem in self.todos_list:
            if elem.title == task.title:
                self.todos_list.remove(task)

    def filter_by_category(self, category):
        results = []
        for elem in self.todos_list:
            if elem.category == category:
                results.append(elem)
        return results

    def filter_by_owner(self, owner):
        results = []
        for elem in self.todos_list:
            if elem.owner == owner:
                results.append(elem)
        return results

    def number_of_categories(self, category):
        increment_number = 0
        for elem in self.todos_list:
            if elem.category == category:
                increment_number += 1
        return increment_number

    def __str__(self):
        return f"{self.todos_list}"

    def display_categories(self):
        for c in Categories:
            print(c)
            #pprint(todos1.filter_by_category(c))
            for elem in self.todos_list:
                if elem.category == c:
                    print(elem)
            print("\n")


todos1 = Todos()
todos1.add_task(task1)
todos1.add_task(task2)
todos1.add_task(task3)
todos1.add_task(Task("Go to second-hand store", "25.June", "Ellie", Categories.SHOPPING))
todos1.add_task(Task("Go to second-hand store", "25.July", "Ellie", Categories.SHOPPING))
todos1.add_task(Task("Get Books", "25.July", "John", Categories.SHOPPING))
todos1.add_task(Task("Cut Grass", "23.June", "Cena", Categories.WORK))
todos1.add_task(Task("Christmas prep even tho it's summer ", "25.July", "Douglas", Categories.PRESENTS))

print(todos1)

todos1.remove_task(task2)

print(todos1)

print(todos1.filter_by_category(Categories.SHOPPING))

# scrieti o metoda in clasa Todos pentru a filtra dupa owner.
# acea metoda va returna toate task-urile ale unui owner, ce-l primim ca parametru al acelei metode.

# scrieti o metoda in clasa Todos care numara toate task-urile ale unei anumite categorii,
# si returneaza cate task-uri sunt pentru acea categorie.
# Daca sunt 3 taskuri in total pe categoria Category.COURSE de exemplu, metoda returneaza numarul 3.

# modificati metoda add_task, sa nu permita adaugarea unui task cu titlu duplicat.
# Daca exista deja un task cu acel titlu, sa printeze "Task with this title already exists!"

print("\n")

pprint(todos1.filter_by_owner("Ellie"))

print("\n")

test = Categories.SHOPPING

print(f"Number of tasks with the category: {test} is {todos1.number_of_categories(test)}")

print("\n")
# creaza o metoda care printeaza task-urile, organizate dupa categorie. de exemplu, acea metoda ar printa:

# """
# Tasks by category:
# Category.COURSE:
# Rezolvare Tema, 23.Iunie, John, Categories.COURSE
# Rezolvare Tema 2, 24.Iunie, John, Categories.COURSE
#
# Category.SHOPPING:
# Go to second-hand store, 23.Iunie, John, Category.SHOPPING
# Buy shoes, 23.Iunie, John, Category.SHOPPING
# """

todos1.display_categories()

print("\n")
