# Scrivi una funzione prime_factors(n: int) -> list[int] che trova i fattori primi di un numero n dato in input
from time import time



def make_prime(num: int) -> list:
    prime_numbers: list= []
    for i in range(2, (num//2) +1):
        prime_numbers.append(i)
    c: int= 0
    for x in range(c, len(prime_numbers)):
        popped_nums: int= 0
        for y in range(len(prime_numbers) -1 -c):
            num1: int = prime_numbers[y +1 +c -popped_nums]
            num2: int = prime_numbers[x]
            temp: float = num1%num2
            if  temp == 0:
                prime_numbers.pop(y +1 +c -popped_nums)
                popped_nums += 1
        c += 1
    return prime_numbers



def prime_factors(n: int) -> list:
    # elimina il pass e implementa la tua soluzione
    prime_list = make_prime(100000)
    factors: list = []
    divisore: int = 2
    i = 0

    while prime_list[i] <= 50000:
        if n%prime_list[i] == 0:
            factors.append(prime_list[i])
            n /= prime_list[i]
            print(n, prime_list[i])
        else:
            i += 1
    return factors

print(prime_factors(99999999999999999999))
        
# start1 = time()
# print(make_prime(100000))
# print(f"{time() - start1} -- PRIMA VERSIONE")



# print(prime_factors(4)) #[2, 2]
# print(prime_factors(60)) #[2, 2, 3, 5]
# print(prime_factors(627)) #[3, 11, 19]
# print(prime_factors(622919)) #[11, 56629]
# print(prime_factors(99999999999999999999)) #[3, 3, 11, 41, 101, 271, 3541, 9091, 27961]

# def prime_factors(n: int) -> list:
#     # elimina il pass e implementa la tua soluzione
#     factors: list = []
#     divisore: int = 2

#     while divisore <= n:
#         if n%divisore == 0:
#             factors.append(divisore)
#             n //= divisore
#         else:
#             divisore += 1
#     return factors