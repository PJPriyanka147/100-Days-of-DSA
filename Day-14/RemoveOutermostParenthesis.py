#Brute force --
def remove_outermost(str):
    result = []
    balance = 0
    start = 0

    for i, char in enumerate(str):
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1

        if balance == 0:
            result.append(str[start + 1:i])
            start = i + 1

    return ''.join(result)

user_input = input("Enter a valid parentheses string: ")
output_string = remove_outermost(user_input)
print("String after removing outermost parentheses:", output_string)