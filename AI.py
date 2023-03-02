class AI:

    # mnożenie skalara przez wektor
    @staticmethod
    def multiply_vectors_by_scalar(scalar, vector):
        return [x * scalar for x in vector]
    



def main():
    print(AI.multiply_vectors_by_scalar(2, [3, 0, 5]))


if __name__ == '__main__':
    main()