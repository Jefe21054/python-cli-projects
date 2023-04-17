def factorial(num):
    if type(num) is not int:
        return None
    if num == 0:
        return 1
    if num < 0:
        return None
    if num > 0 and type(num) is int:
        i = 0
        aux = 1
        for i in range(num):
            i = i + 1
            aux = aux * i
        return aux

res = factorial(5)
print(res)
