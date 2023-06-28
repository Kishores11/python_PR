def factorial(num):
    fact = 1
    if num < 0:
        return "Give number above zero"
    elif num == 0 or num == 1:
        return fact
    else:
        for i in range(1,num+1):
            fact = fact*i
        return fact
    
result = factorial(3)
print(result)