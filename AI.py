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

    # iloczyn skalarny
    @staticmethod
    def dot_product(vector_1, vector_2):
        if len(vector_1) != len(vector_2):
            print('Vectors are not equals!')
        else:
            answer = 0
            for i in range(len(vector_1)):
                answer += vector_1[i] * vector_2[i]
        return answer

    # mnożenie wektorów przez skalar
    @staticmethod
    def multiply_matrix_by_skalar(matrix, scalar):
        return [AI.multiply_vectors_by_scalar(scalar, x) for x in matrix]

    # transpozycja macierzy
    def matrix_transposition(array_1):
        return [[array_1[j][i] for j in range(len(array_1))] for i in range(len(array_1[0]))]

    # mnożenie macierzy
    @staticmethod
    def matrix_multiplication(matrix_1, matrix_2):
        if len(matrix_1[0]) == len(matrix_2):
            transposed_matrix = AI.matrix_transposition(matrix_2)
            result = []
            for row in matrix_1:
                tmp = []
                for col in transposed_matrix:
                    tmp.append(AI.dot_product(row, col))
                result.append(tmp)
            return result
        else:
            print('The number of columns of the first matrix is not equal to the number of rows of the second matrix.')

    # wyznacznik macierzy
    @staticmethod
    def matrix_determinant(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0

        for i in range(len(matrix)):
            sign = (-1) ** i
            sub_matrix = []
            for j in range(1, len(matrix)):
                row = []
                for k in range(len(matrix)):
                    if k != i:
                        row.append(matrix[j][k])
                sub_matrix.append(row)
            sub_det = AI.matrix_determinant(sub_matrix)
            det += sign * matrix[0][i] * sub_det
        return det

    # odwrotność macierzy 3x3 - macierz dopelnien
    @staticmethod
    def invert_matrix_3x3(matrix):
        det = AI.matrix_determinant(matrix)

        if det == 0:
            print('Matrix can not be invert')
        else:
            inverted_matrix = [[0 for j in range(3)] for i in range(3)]
            inverted_matrix[0][0] = (
                matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2]) / det
            inverted_matrix[0][1] = (
                matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) / det
            inverted_matrix[0][2] = (
                matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) / det
            inverted_matrix[1][0] = (
                matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) / det
            inverted_matrix[1][1] = (
                matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) / det
            inverted_matrix[1][2] = (
                matrix[1][0] * matrix[0][2] - matrix[0][0] * matrix[1][2]) / det
            inverted_matrix[2][0] = (
                matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1]) / det
            inverted_matrix[2][1] = (
                matrix[2][0] * matrix[0][1] - matrix[0][0] * matrix[2][1]) / det
            inverted_matrix[2][2] = (
                matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]) / det

            return inverted_matrix


def main():
    # print(AI.multiply_vectors_by_scalar(2, [3, 0, 5]))
    # print(AI.add_vectors([3, 0, 5], [6, 4, -2]))
    # print(AI.dot_product([3, 0, 5], [6, 4, -2]))
    # print(AI.multiply_matrix_by_skalar(
    #     matrix=[
    #         [1, 2, 3],
    #         [4, 5, 6],
    #         [7, 8, 9],
    #     ],
    #     scalar=2
    # ))

    matrix_1 = [
        [-1, -2, 3],
        [0, 2, -1],
        [-1, 3, 0]
    ]
    # matrix_2 = [
    #     [1, 5, 1],
    #     [2, 1, 2],
    #     [3, 2, 3]
    # ]
    # print(AI.matrix_multiplication(matrix_1, matrix_2))
    # print(AI.matrix_determinant(matrix_2))
    print(AI.invert_matrix_3x3(matrix_1))

if __name__ == '__main__':
    main()
