# f(n) = f(n-1) + f(n-2)
# [f0, f1, f2, f3, f4...]
# f0 = 1, f1 = 1
# [1, 1]
# f2 = 1 + 1 = 2
# [1, 1, 2] 
# f3 = 2 + 1
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
# f0 f1 f2 f3 f4 f5 f6 f7


def fibonacci_for(n: int) -> int:
    num1 = 1
    num2 = 1
    somma = 1
    for i in range(n-1):
        somma = num1 + num2
        num1 = num2
        num2 = somma
    return somma

def fibonacci_for_short(n: int) -> int:
    num1 = 1
    num2 = 1
    for i in range(n-1):
        num1, num2 = num2, num1 + num2
    return num2


print(fibonacci_for_short(12))

