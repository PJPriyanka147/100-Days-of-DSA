#Using Brute force -- inefficient
def lenOfLongSubarr(arr, k):
        n = len(arr)
        max_len = 0
        for start in range(n):
            curr_sum = 0
            for end in range(start, n):
                curr_sum += arr[end]
                if curr_sum == k:
                    current_length = end - start + 1
                    max_len = max(max_len, current_length)
        return max_len

arr = list(map(int,input("Enter the elements: ").split()))
k = int(input("Enter the value of k: "))
result = lenOfLongSubarr(arr, k)
print(result)

#Using dictionary --
