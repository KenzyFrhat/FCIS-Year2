from fractions import Fraction

def minor_matrix(matrix, row, col):
    """Return sub-matrix excluding row & column."""
    return [
        [matrix[i][j] for j in range(len(matrix)) if j != col]
        for i in range(len(matrix)) if i != row
    ]


def determinant(matrix):
    """Compute determinant recursively with exact Fractions."""
    n = len(matrix)

    # Matrix must be square
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square to calculate determinant.")

    # Base cases
    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    # Recursive Laplace expansion (first row)
    det = Fraction(0)
    for j in range(n):
        sub = minor_matrix(matrix, 0, j)
        sign = (-1) ** j
        det += sign * matrix[0][j] * determinant(sub)

    return det


def cofactor_matrix(matrix):
    """Return full cofactor matrix."""
    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square to calculate cofactor matrix.")

    C = []
    for i in range(n):
        row = []
        for j in range(n):
            sub = minor_matrix(matrix, i, j)
            sign = (-1) ** (i + j)
            cof = sign * determinant(sub)
            row.append(cof)
        C.append(row)

    return C
