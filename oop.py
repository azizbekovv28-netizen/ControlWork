print("Задание 1")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self.__age = new_age


person = Person("Samat", 18)
print(person.get_age())
person.set_age(20)
print(person.get_age())

try:
    person.set_age(-5)
except ValueError as e:
    print(e)

print()
print("Задание 2")
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return"I am an animal!"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Рекс")
print(dog.name, dog.speak())
cat = Cat("Рыжик")
print(cat.name, cat.speak())

print()
print("Задание 3")

class Vehicle:
    def move(self):
        return "Vehicle is moving!"

class Car(Vehicle):
    def move(self):
        return "Car is moving!"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is moving!"

def move(vehicle):
    return vehicle.move()

car = Car()
bicycle = Bicycle()
vehicle = Vehicle()

print(move(car))
print(move(bicycle))
print(move(vehicle))

print()
print("Задание 4")
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(5, 10)
print(f'Площадь прямоуголника: {rectangle.area()}')
circle = Circle(7)
print(f'Площаль круга: {circle.area()}')