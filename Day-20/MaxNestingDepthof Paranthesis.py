#Brute force --
def maxDepth(str):
    current_depth = 0
    max_depth = 0

    for char in str:
        if char == '(':
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        elif char ==')':
            current_depth -= 1
    return max_depth

str = input("Enter string:")
result = maxDepth(str)
print(result)
