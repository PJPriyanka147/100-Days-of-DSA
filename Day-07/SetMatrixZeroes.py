def input_matrix():
    m = int(input("Enter no of rows: "))
    n = int(input("Enter no of columns: "))
    
    matrix = []
    print("Enter the elements row-wise(space-seperated): ")
    for i in range(m):
        row  = list(map(int, input().split()))
        if len(row) != n:
            raise ValueError("Incorrect number of elements in the row")
        matrix.append(row)
    
    return matrix

def set_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])

    zero_positions = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_positions.append((i, j))
    
    #print("Zero positions: ", zero_positions)

    for i, j in zero_positions:
        #Set the entire row i to 0
        for col in range(n):
            matrix[i][col] = 0
        #Set the entire col j to 0
        for row in range(m):
            matrix[row][j] = 0
        
    return matrix

matrix = input_matrix()
modified_matrix = set_zeroes(matrix)
print(modified_matrix)


