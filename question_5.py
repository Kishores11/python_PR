def palindrome(str1):
    str2 = str1[::-1]
    if str1 == str2:
        return "It is palindrome"
    else:
        return "It is not palindrome"
    
result = palindrome("malayalam")
print(result)