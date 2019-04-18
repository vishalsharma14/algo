"""
    LeetCode 566. Reshape the Matrix

    In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into
    a new one with different size but keep its original data.

    You're given a matrix represented by a two-dimensional array, and two positive integers r and c
    representing the row number and column number of the wanted reshaped matrix, respectively.

    The reshaped matrix need to be filled with all the elements of the original matrix in the same
    row-traversing order as they were.

    If the 'reshape' operation with given parameters is possible and legal, output the new
    reshaped matrix; Otherwise, output the original matrix.

    Example 1:

    Input:
    nums =
    [[1,2], [3,4]]
    r = 1, c = 4
    Output:
    [[1,2,3,4]]
    Explanation:
    The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix,
    fill it row by row by using the previous list.
    Example 2:

    Input:
    nums =
    [[1,2],
     [3,4]]
    r = 2, c = 4
    Output:
    [[1,2],
     [3,4]]
    Explanation:
    There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
    Note:

    The height and width of the given matrix is in range [1, 100].
    The given r and c are all positive.
"""


def reshape_matrix(matrix, new_rows, new_columns):
    """
        :param matrix: Original Matrix
        :param new_rows: Rows for new matrix
        :param new_columns: Columns for new matrix
        :return: Reshaped matrix if reshape is possible, original matrix otherwise
    """
    rows = len(matrix)
    columns = len(matrix[0])

    if rows * columns != new_rows * new_columns:
        return matrix

    new_matrix = [[] for _ in range(new_rows)]
    temp_arr = []
    for i in range(rows):
        for j in range(columns):
            temp_arr.append(matrix[i][j])

    for i in range(new_rows):
        temp = []
        for j in range(new_columns):
            temp.append(temp_arr.pop(0))
        new_matrix[i].extend(temp)
    return new_matrix


