list1 = [1, 2, 3, 3, 4, 5, 5, 6, 6]
list2 = []

for num in list1:
    if num not in list2:
        list2.append(num)

print(list2)

