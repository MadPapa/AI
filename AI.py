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
                matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2]) // det
            inverted_matrix[0][1] = (
                matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) // det
            inverted_matrix[0][2] = (
                matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) // det
            inverted_matrix[1][0] = (
                matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) // det
            inverted_matrix[1][1] = (
                matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) // det
            inverted_matrix[1][2] = (
                matrix[1][0] * matrix[0][2] - matrix[0][0] * matrix[1][2]) // det
            inverted_matrix[2][0] = (
                matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1]) // det
            inverted_matrix[2][1] = (
                matrix[2][0] * matrix[0][1] - matrix[0][0] * matrix[2][1]) // det
            inverted_matrix[2][2] = (
                matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]) // det

            return inverted_matrix

    # odwrotność macierzy 3x3 - metoda Gaussa
    @staticmethod
    def invert_matrix_3x3_gauss(matrix):
        if len(matrix) != 3 or len(matrix[0]) != 3:
            raise ValueError("The matrix must be 3x3.")

        identity = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        matrix_len = len(matrix)
        for col in range(matrix_len):
            if matrix[col][col] == 0:
                raise ValueError("The matrix has no inverse.")

            scalar = 1 / matrix[col][col]
            for row in range(matrix_len):
                matrix[row][col] *= scalar
                identity[row][col] *= scalar

            for row in range(matrix_len):
                if row != col:
                    scalar = matrix[col][row]
                    for i in range(matrix_len):
                        matrix[i][row] -= scalar * matrix[i][col]
                        identity[i][row] -= scalar * identity[i][col]

        return identity
    
    # odwrotność macierzy 5x5 i innych - metoda Gaussa
    @staticmethod
    def invert_matrix_5x5_gauss(matrix):

        identity = [[0 if j != i else 1 for j in range(len(matrix[0]))] for i in range(len(matrix))]

        matrix_len = len(matrix)
        for col in range(matrix_len):
            if matrix[col][col] == 0:
                raise ValueError("The matrix has no inverse.")

            scalar = 1 / matrix[col][col]
            for row in range(matrix_len):
                matrix[row][col] *= scalar
                identity[row][col] *= scalar

            for row in range(matrix_len):
                if row != col:
                    scalar = matrix[col][row]
                    for i in range(matrix_len):
                        matrix[i][row] -= scalar * matrix[i][col]
                        identity[i][row] -= scalar * identity[i][col]

        return identity

    # układ 2 równań z 2 niewiadomymi Cramer
    @staticmethod
    def system_of_equations_cramer(matrix):
        det = (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1]) # (a1 * b2) - (a2 * b1)
        det_x = (matrix[0][2] * matrix[1][1]) - (matrix[1][2] * matrix[0][1])# (c1 * b2) - (c2 * b1)
        det_y = (matrix[0][0] * matrix[1][2]) - (matrix[1][0] * matrix[0][2]) # (a1 * c2) - (a2 * c1)

        if det == 0 and (det_x or det_y) != 0:
            raise ValueError('no solutions')
        elif det == 0 and det_x == 0 and det_y == 0:
            raise ValueError('infinitely many solutions')
        else:
            x = det_x / det
            y = det_y / det

            return 'x = {}\ny = {}'.format(x, y)
        
    # rząd macierzy
    @staticmethod
    def matrix_rank(matrix):
        inverted_matrix = AI.invert_matrix_5x5_gauss(matrix)
        rank = len(matrix)

        for row in inverted_matrix:
            if all(elem == 0 for elem in row):
                rank -= 1
        
        return rank


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

    # matrix_1 = [
    #     [-1, -2, 3],
    #     [0, 2, -1],
    #     [-1, 3, 0]
    # ]
    # matrix_2 = [
    #     [1, 5, 1],
    #     [2, 1, 2],
    #     [3, 2, 3]
    # ]

    # matrix_3 = [
    #         [1, 2, 8],
    #         [2, -1, 1]
    #     ]

    matrix = [
        [1, 0, 0, 0, 2],
        [2, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1]
    ]

    matrix2 = [
        [1, 2, 0],
        [0, -1, 3],
        [2, 0, -2],
    ]

    # print(AI.matrix_multiplication(matrix_1, matrix_2))
    # print(AI.matrix_determinant(matrix_2))
    # print(AI.invert_matrix_3x3(matrix_1))
    # print(AI.invert_matrix_3x3_gauss(matrix_1))
    # print(AI.system_of_equations_cramer(matrix_3))

    # print([[round(el, 2) for el in row] for row in AI.invert_matrix_5x5_gauss(matrix)])
    print(AI.matrix_rank(matrix2))
    

if __name__ == '__main__':
    main()
