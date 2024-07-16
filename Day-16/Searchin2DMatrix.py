#Brute force --
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

def searchMatrix(matrix, target):
    for row in matrix:
        for element in row:
            if element == target:
                return True
    return False

matrix = input_matrix()
target = int(input("Enter target:"))
result = searchMatrix(matrix, target)
print(result)
