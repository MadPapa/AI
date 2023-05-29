from typing import List
import math
import numpy as np

class Car:
    model: str
    speed: int
    prod_year: int
    category: str

    def __init__(self, model: str, speed: int, prod_year: int, category: str = None) -> None:
        self.model = model
        self.speed = speed
        self.prod_year = prod_year
        self.category = category

    def __str__(self) -> str:
        return f"{self.model}\n{self.prod_year}\n{self.speed}\n{self.category}\n"


def euklides(array: List, car: Car) -> List:
    return [
        [obj.category, math.sqrt(((obj.speed - car.speed) ** 2) + ((obj.prod_year - car.prod_year) ** 2))] for obj in array
    ]

def knn(values: List, k: int) -> List:
    new_list: List = []

    while len(new_list) < k:
        smaller: List = values[0]
        values.remove(values[0])
        for item in values:
            if item[1] < smaller[1]:
                smaller = item
        
        if smaller not in new_list:
            new_list.append(smaller)

    return new_list

def make_decision(values: List) -> str:
    fast: int = 0
    slow: int = 0

    for item in values:
        if item[0] == "fast":
            fast += 1
        if item[0] == "slow":
            slow += 1
        else:
            continue

    return "fast" if fast > slow else "slow"


cars: List = [
    Car("BMW", 100, 2018, "fast"),
    Car("Audi", 60, 2015, "slow"),
    Car("Fiat", 120, 2019, "fast"),
    Car("Mercedes", 220, 2012, "fast"),
    Car("Opel", 80, 1980, "slow"),
    Car("Mitsubishi", 200, 2019, "fast"),
]

new_car: Car = Car("Volkswagen", 90, 2017)

print("Distances:\n")
distances: List = euklides(cars, new_car)
print(np.asarray(distances))

print()

k: int = 3

print(f"Neighbors (k = {k}):\n")
answers: List = knn(distances, k)
print(np.asarray(answers))

print()
print("Decision:", make_decision(answers))
