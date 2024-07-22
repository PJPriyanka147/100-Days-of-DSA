#Brute force  --
def isPalindrome(substring):
    return substring == substring[::-1]

def longest_Palindrome(string):
    n = len(string)

    if n == 0:
        return ""
    
    longest = ""

    for i in range(n):
        for j in range(i, n):
            substring = string[i:j+1]
            if isPalindrome(substring) and len(substring) > len(longest):
                longest = substring
    
    return longest


string = input("Enter string: ")
result = longest_Palindrome(string)
print(result)