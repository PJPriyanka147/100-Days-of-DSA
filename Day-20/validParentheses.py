#brute force --
def validParentheses(str):
    if not str:
        return False
    
    while '()' in str or '[]' in str or '{}' in str:
        print(f"Before replacement: {str}")
        str = str.replace('()', '')
        str = str.replace('[]', '')
        str = str.replace('{}', '')
        print(f"After replacement: {str}")

    return str == ''


str = input("Enter String: ")
result = validParentheses(str)
print(result)