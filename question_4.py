def countVowels(str1):
    count = 0
    vowels = ['a','e','i','o','u']
    list1 = list(str1)
    for char in list1:
        if char in vowels:
            count += 1
    return count

result = countVowels("kishore")
print(result)