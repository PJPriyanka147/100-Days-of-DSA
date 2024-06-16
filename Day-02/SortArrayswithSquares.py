#Given a sorted array A containing N integers both positive and negative.
#You need to create another array containing the squares of all the elements in A and return it in non-decreasing order.

def sort_with_squares(A):
    N = len(A)
    result = [0] * N
    left, right = 0, N-1
    pos = N-1
       
    while left <= right:
        left_square = A[left] ** 2
        right_square = A[right] **2
           
        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1
                
        pos -= 1
            
    return result

A = list(map(int, input().split()))
result = sort_with_squares(A)
print(result)