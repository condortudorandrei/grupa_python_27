
class Observer:
    def update(self, msg):
        pass

    def cleanup(self):
        pass


class EventBus:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def unregister_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, msg):
        for observer in self.observers:
            observer.update(msg)

    def finish_for_all(self):
        for observer in self.observers:
            observer.cleanup()


# Creati o clasa care mosteneste din Observer
# suprascrieti metoda update sa printeze acel msg
# creati o instanta a acestei clase
# scrieti bus.register_observer si folositi acea instanta a clasei respective
# rulati codul


class Printer(Observer):
    def update(self, msg):
        print(msg)


class ToFile(Observer):
    def __init__(self):
        self.f = open("logs.txt", "w")

    def update(self, msg):
        self.f.write(msg)
        self.f.write("\n")

    def cleanup(self):
        self.f.close()


bus = EventBus()
hp_420 = Printer()
file_writer = ToFile()
bus.register_observer(hp_420)
bus.register_observer(file_writer)

while True:
    var1 = input("Message: \n")
    if var1 == "x":
        print("Exiting...")
        break
    bus.notify(var1)

bus.finish_for_all()











