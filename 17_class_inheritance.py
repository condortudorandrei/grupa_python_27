

class AnimalPark:
    def __init__(self):
        self.animals  = []

    def add_animal(self, animal):
        if isinstance(animal,Animal):
            self.animals.append(animal)

    def make_noise(self):
        for animal in self.animals:
            animal.speak()


class Animal:
    def __init__(self, name = "Generic", age = 1):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Animal: {self.name}"

    def __repr__(self):
        return f"Animal(\"{self.name}\")"


    def speak(self):
        print("I am animal")


class Dog(Animal):
    def __init__(self, name, age = 1 , breed = "Corcitura"):
        super().__init__(name, age)
        self.breed = breed


    def speak(self):
        print("Woof!")

    def lick(self):
        print("Dog licks")

    def __str__(self):
        return f"Dog: {self.name}"

    def __repr__(self):
        return f"Dog(\"{self.name}\")"



class Cat(Animal):
    def speak(self):
        print("Meow!")

    def __str__(self):
        return f"Cat: {self.name}"

    def __repr__(self):
        return f"Cat(\"{self.name}\")"


class Bat(Dog):
    def __str__(self):
        return f"Bat: {self.name}"

    def __repr__(self):
        return f"Bat(\"{self.name}\")"

# anim1 = Animal()
# anim1.speak()

dog1 = Dog("Spot", 7, "Bishop")
cat1 = Cat("Shadow")

dog1.speak()
dog1.lick()
cat1.speak()

print("=============== :Animal park: ==============")

cat2 = Cat("Paw")
bat1 = Bat("Batman", 37, "Batman")


park = AnimalPark()
park.add_animal(dog1)
park.add_animal(cat1)
park.add_animal(cat2)
park.add_animal(bat1)

print(park.animals)
park.make_noise()

print(dog1.breed)






