# from pprint import pprint



# interiorul clasei
class BankAccount:
    bank = "ING"

    def __init__(self, name, balance=300):
        self.name = name
        self.__balance = balance                 # proprietate privata
        self.number_of_deposits = 0

    def __str__(self):
        return f"{self.name} has an account balance of ${self.__balance}"


    # getter:
    @property
    def balance(self):
        return self.__balance

    # setter:
    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self.__balance = amount
            self.number_of_deposits += 1


    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough money")
        else:
            self.__balance -= amount

    @staticmethod
    def is_valid_amount(amount):
        # isinstance() checks if "amount" is of type "int" or "float"
        if not isinstance(amount, bool) and isinstance(amount, (int, float) )and amount > 0:
            return True
        else:
            return False

    @classmethod
    def construct_from_string(cls, account_data):
        # account_data = "John:300"
        # cls == clasa == BankAccount
        # owner recieves "John" and amount receives "300"
        owner, amount = account_data.split(":")
        obj1 = cls(owner, int(amount))
        return obj1


# "@staticmethod" ->  E o metoda care are legatura cu contrui bancare
# dar nu are legatura cu un cont anume sau informatii dintr-un "self" anume

# "@classmethod" -> E o metoda care opereaza pe clasa si are o actiune la nivel de clasa.



# exteriorul clasei
ing1 = BankAccount("Adi")
ing1.withdraw(10)

print(ing1.balance)
# syntactic sugar
ing1.balance += 300
ing1.balance += 300
ing1.balance += 300

new_amount = True
print(BankAccount.is_valid_amount(new_amount))

print(ing1.balance)
print(ing1.number_of_deposits)








