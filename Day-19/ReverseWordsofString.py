#Brute force --
def reverseWords(s):
    s = s.strip()
    words = s.split()
    words.reverse()
    reversed_s = ' '.join(words)

    return reversed_s

s = input("Enter string:")
result = reverseWords(s)
print(result)