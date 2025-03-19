from datetime import date
from typing import Self


class Calculator:
    def __init__(self, version):
        self.version = version

    def description(self):
        print(f"This is a {self.version} calculator")

    # will not use class variable nor instance variable - we can call it my Calculator.add_numbers(1, 2, 3)
    # might or miht not releated to class itself
    @staticmethod
    def add_numbers(*numbers: float) -> float:
        return sum(numbers)


class Person:
    # class vraibale can be used throughout the class
    city = "Bangalore"
    p = 2

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def description(self):
        print(
            f"{self.name} is {self.age} years old. Lives in {self.city}, p = {self.p}"
        )

    # we can call it my Person.age_from_birthyear("Yash", 1996) - this will create a persone but by input name and birth_year
    # class method is going to affect the actual class
    @classmethod
    def age_from_birthyear(clc, name: str, birth_year: int) -> Self:
        current_year: int = date.today().year
        age: int = current_year - birth_year + clc.p
        return clc(name, age)


if __name__ == "__main__":
    c1 = Calculator(10)
    c2 = Calculator(20)

    c1.description()
    print(Calculator.add_numbers(1, 2, 3))

    yash = Person("Yash", 25)
    yash.description()

    # we craeted instance of the class but this thime using class method
    yash2 = Person.age_from_birthyear("Yash", 1996)
    yash2.description()
    print(yash2.city)
    print(Person.city)
