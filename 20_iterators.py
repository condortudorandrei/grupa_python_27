
# fibonaci
# 0 1 1 2 3 5 8 13 21 34 55 89......
# 0 1 2 3 4 5 6  7  8  9 10 11


# un iterator poate explora un spatiu cu un sfarsit necunoscut unde e greu
# de stiut cati pasi se paote explora in acel spatiu
class Fibonacci:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.first + self.second
        self.first = self.second
        self.second = current
        return current


pas = 0
for i in Fibonacci():
    print(i)
    if pas >= 10:
        break
    pas = pas + 1
















