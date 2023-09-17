# Python program to calculate sum of each row and sum of each column in a matrix

# Function to calculate the sum of each row in a matrix
def row_sum(matrix):
    row_sums = []
    for row in matrix:
        row_sum = sum(row)
        row_sums.append(row_sum)
    return row_sums

# Function to calculate the sum of each column in a matrix
def column_sum(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])  
    col_sums = [0] * num_cols

    for i in range(num_rows):
        for j in range(num_cols):
            col_sums[j] += matrix[i][j]

    return col_sums

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calculate and print the sum of each row
row_sums = row_sum(matrix)
print("Sum of each row:", row_sums)

# Calculate and print the sum of each column
col_sums = column_sum(matrix)
print("Sum of each column:", col_sums)
