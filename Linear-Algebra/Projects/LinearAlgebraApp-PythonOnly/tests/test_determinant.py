# cases of matrix that are not square 
# casees of matrix with zero determinant


# supposed the given matrix is all valid to calculate determinant

def determinant(matrix):

    len_matrix = len(matrix)

    #! not square matrix 
    if any(len(row) != len_matrix for row in matrix):
        raise ValueError("Matrix must be square to calculate determinant.")
    
    #! determinant equals zero cases
    if(any(all(element == 0 for element in row) for row in matrix) or
       any(all(matrix[j][i] == 0 for j in range(len_matrix)) for i in range(len_matrix))):
        return 0

    # if the matrix has a row or column that is a multiple of another row or column
    for i in range(len_matrix):
        for j in range(i + 1, len_matrix):
            if all(matrix[i][k] * matrix[j][0] == matrix[j][k] * matrix[i][0] for k in range(len_matrix)):
                return 0
            
    
    det = 0
    row_length = len_matrix

    if row_length == 1:
        return matrix[0]
    
    if row_length == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    
    for k in range(row_length):
       # select the sub matrix
        sub_matrix = [row[:k] + row[k+ 1: ] for row in matrix[1:]]
        sign = (-1) ** (k)
        det += matrix[0][k] * sign * determinant(sub_matrix)

    return det


# Example usage:
matrix_2x2 = [[4, 6],
              [3, 8]]
matrix_3x3 = [[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]]

print(determinant(matrix_2x2))  # Output: 14

print(determinant(matrix_3x3))  # Output: -306

# test cases for
# matrix not square
try:
    non_square_matrix = [[1, 2, 3],
                         [4, 5, 6]]
    print(determinant(non_square_matrix))

except ValueError as e:
    print(e)  # Output: Matrix must be square to calculate determinant.



# calculate the co-factor matrix
def cofactor_matrix(matrix):
    len_matrix = len(matrix)

    #! not square matrix 
    if any(len(row) != len_matrix for row in matrix):
        raise ValueError("Matrix must be square to calculate cofactor matrix.")

    cofactor_mat = []

    for i in range(len_matrix):
        cofactor_row = []
        
        for j in range(len_matrix):
            # create sub-matrix
            sub_matrix = [row[:j] + row[j+1:] for k, row in enumerate(matrix) if k != i]
            sign = (-1) ** (i + j)
            cofactor_value = sign * determinant(sub_matrix)
            cofactor_row.append(cofactor_value)

        cofactor_mat.append(cofactor_row)

    return cofactor_mat

    
