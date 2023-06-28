def largest(a,b,c):
    if a > b and a > c:
        return f'{a} is largest'
    if b > a and b > c:
        return f'{b} is largest'
    if c > a and c > b:
        return f'{c} is largest'



result = largest(15,1,39)
print(result)