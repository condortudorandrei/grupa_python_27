from pprint import pprint

print("=================Classes course start:=================")


class Cat:
    # constructor
    def __init__(self, name, owner, temperament="Loving"):
        self.name = name
        self.owner = owner
        self.temperament = temperament

    def __str__(self):
        return f"Cat: name is {self.name}, owner is {self.owner}, and its temperament is {self.temperament}"

    def speak(self):
        print(f"{self.name} says \"Meow\"")

    def eat(self, food):
        print(f"{self.name} eats \"{food}\"")

    def __repr__(self):
        return f"Cat(\"{self.name}\",\"{self.owner}\",\"{self.temperament}\")"


cat1 = Cat("Shadow", "Johnny")
cat2 = Cat("Spot", "Yuda", "Shy")
# cat1 = Cat.__init__(cat1)

# print(cat1)
# print(cat2)

# cat1.name = "Shadow"
# cat2.name = "Spot"

# print(cat1)
# print(str(cat2))


print(cat1.name)
cat2.name = "Ouroboros"
cat2.speak()
cat2.eat(cat2)

cats = [cat1, cat2]
pprint(cats)

stray_cats = [Cat("Shadow", "Johnny", "Loving"), Cat("Ouroboros", "Yuda", "Shy")]

print(stray_cats)


class BankAccount:
    bank = "ING"
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name} has an account balance of ${self.balance}"

    def depozit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount


acc1 = BankAccount("Johnny")

acc1.depozit(200)
acc1.withdraw(400)
print(acc1)

acc2 = BankAccount("Ellie", 12000)
acc2.bank = "BT"
print(acc2)

print("\n")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle has a width of {self.width}, and a height of {self.height}"

    def area(self):
        return f"Rectangle has an area of {self.width * self.height}"

    def perimeter(self):
        return f"Rectangle has an perimeter of {2 * (self.width + self.height)}"


rec1 = Rectangle(10, 20)
print(rec1.area())
print(rec1.perimeter())
