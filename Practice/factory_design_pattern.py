from abc import ABC, abstractmethod


# step 1: defining the product interface
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass


# step 2: defining the concrete products
class Espresso(Coffee):
    def prepare(self):
        return "Preparing a rich and strong Espresso"


class Latte(Coffee):
    def prepare(self):
        return "Preparing a smooth and creamy Latte"


class Cappuccino(Coffee):
    def prepare(self):
        return "Preparing a frothy and delicious Cappuccino"


# step 3: defining the factory
class CoffeeMachine:
    def prepare_coffee(self, coffee_type):
        return coffee_type().prepare()


# step 4: using the factory to create product
if __name__ == "__main__":
    coffee_machine = CoffeeMachine()

    coffee_types = {1: Espresso, 2: Latte, 3: Cappuccino}

    try:
        coffee_type = int(
            input("1 = Espresso, 2 = Latte, 3 = Cappuccino\nEnter the coffee type: ")
        )
    except ValueError:
        print("Invalid coffee type")

    if coffee_type in [1, 2, 3]:
        print(coffee_machine.prepare_coffee(coffee_types[coffee_type]))
    else:
        print("Invalid coffee type")
