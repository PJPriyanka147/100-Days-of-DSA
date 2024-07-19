#An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
#typically using all the original letters exactly once. For two strings to be anagrams, they
#must have the same characters with the same frequency in any order.

#Brute force --
def isAnagram(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    return sorted_s == sorted_t


s = input("Enter string 1:")
t = input("Enter string 2:")
result = isAnagram(s, t)
print(result)

#Optimized using hash map --
from collections import Counter

def isAnagram(s, t):
    if len(s)!= len(t):
        return False
    
    counter_s = Counter(s)
    counter_t = Counter(t)

    return counter_s == counter_t


s = input("Enter string 1:")
t = input("Enter string 2:")
result = isAnagram(s, t)
print(result)
