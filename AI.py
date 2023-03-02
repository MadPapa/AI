class AI:

    # mnożenie skalara przez wektor
    @staticmethod
    def multiply_vectors_by_scalar(scalar, vector):
        return [x * scalar for x in vector]

    # dodawanie vectorów
    @staticmethod
    def add_vectors(vector_1, vector_2):
        if len(vector_1) != len(vector_2):
            print('Vectors are not equal!')
        else:
            return [vector_1[x] + vector_2[x] for x in range(len(vector_1))]


def main():
    print(AI.multiply_vectors_by_scalar(2, [3, 0, 5]))
    print(AI.add_vectors([3, 0, 5], [6, 4, -2]))


if __name__ == '__main__':
    main()
