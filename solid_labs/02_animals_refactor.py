from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self) -> str:
        return "woof-woof"


class Cat(Animal):
    def make_sound(self) -> str:
        return "meow"


class Turtle(Animal):
    def make_sound(self) -> str:
        return "turtle sound"


class Chicken(Animal):
    def make_sound(self) -> str:
        return "chicken sound"


class Pig(Animal):
    def make_sound(self) -> str:
        return "pig sound"


def animal_sound(animals: List[Animal]) -> None:
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Turtle(), Chicken(), Pig()]
animal_sound(animals)
