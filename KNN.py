import csv
import math
import random
from operator import itemgetter
from typing import List, TextIO


def read_data(path: TextIO) -> List:
    array: List = []
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")

        next(reader)  # skip the first line (data header)

        for row in reader:
            values: List = [int(value) for value in row]
            array.append(values)

    return array


def prepare_set(data_length: int, percent: float) -> int:
    return int(data_length * percent)


def add_data_to_the_train_set(data_set: List, how_many: int) -> List:
    train_set: List = []

    while len(train_set) < how_many:
        rand_id: int = random.randint(0, len(data_set) - 1)
        train_set.append(data_set.pop(rand_id))

    return train_set


def add_data_to_the_test_set(data_set: List, how_many: int) -> List:
    test_set: List = []

    while len(test_set) < how_many:
        rand_id: int = random.randint(0, len(data_set) - 1)
        test_set.append(data_set.pop(rand_id)[:4])

    return test_set


def euklides(array_1: List, array_2: List) -> float:
    dimension: int = len(array_1)
    return math.sqrt(sum((array_1[i] - array_2[i]) ** 2 for i in range(1, dimension))) 
    # range(1, dimension) 1 not 0 because identifier is in the 0 place


def manhattan(array_1: List, array_2: List) -> float:
    dimension: int = len(array_1)
    return sum(abs(array_1[i] - array_2[i]) for i in range(1, dimension))


def cosine_similarity(array_1: List, array_2: List) -> float:
    dimension: int = len(array_1)

    dot_product: float = sum(array_1[i] * array_2[i] for i in range(1, dimension))
    magnitude_1: float = math.sqrt(sum(array_1[i] ** 2 for i in range(1, dimension)))
    magnitude_2: float = math.sqrt(sum(array_2[i] ** 2 for i in range(1, dimension)))

    similarity: float = dot_product / (magnitude_1 * magnitude_2)

    return 1 - similarity


def k_nearest_neighbors(train_set: List, test_sample: List, k: int, metric: int):
    distances: List = []

    for train_sample in train_set:
        if metric == 1:
            dist: float = euklides(test_sample, train_sample)
        if metric == 2:
            dist: float = manhattan(test_sample, train_sample)
        if metric == 3:
            dist: float = cosine_similarity(test_sample, train_sample)

        distances.append((train_sample, dist))

    distances.sort(key=itemgetter(1))
    neighbours: List = [(dist[0]) for dist in distances[:k]]

    return neighbours


def predicted_price(neighbors: List, k: int):
    return sum(neighbor[-1] for neighbor in neighbors) / k


def calculate_percentage_coverage(array: List, test_sample: List, predicted_price: float):
    for item in array:
        if item[:4] == test_sample:
            dimension: int = len(item) - 1
            return round((predicted_price / item[dimension]) * 100)


if __name__ == "__main__":
    array: List = read_data("data.csv")
    tmp_array = array.copy()

    train_count: int = prepare_set(len(array), 0.7)
    test_count: int = prepare_set(len(array), 0.3)

    # print(train_count, test_count)

    train_set: List = add_data_to_the_train_set(array, train_count)
    test_set: List = add_data_to_the_test_set(array, test_count)

    # print("length: ", len(train_set))
    # print("length: ", len(test_set))

    print("Available metrics:")
    print("1 - Euklides")
    print("2 - Manhattan")
    print("3 - Cosine similarity")

    metric: int = int(input("Input a number: "))

    k: int = int(input("Input k-neighbors: "))

    for test_sample in test_set:
        neighbors: List = k_nearest_neighbors(train_set, test_sample, k, metric)

        print(f"\nPróbka testowa: {test_sample}")
        print(f"Najbliżsi sąsiedzi:")
        for neigbor in neighbors:
            print(neigbor)
        pred_price = predicted_price(neighbors, k)
        print("Przewidywana cena (tys PLN): ", pred_price)
        print("Pokrycie: {}%".format(calculate_percentage_coverage(tmp_array, test_sample, pred_price)))
        for i in range(len(neighbors) * 15):
            print("-", end="")
