# Scrivi una funzione prime_factors(n: int) -> list[int] che trova i fattori primi di un numero n dato in input

# print(prime_factors(4)) #[2, 2]
# print(prime_factors(60)) #[2, 2, 3, 5]
# print(prime_factors(627)) #[3, 11, 19]
# print(prime_factors(622919)) #[11, 56629]
# print(prime_factors(99999999999999999999)) #[3, 3, 11, 41, 101, 271, 3541, 9091, 27961]

def prime_factors(n: int) -> list:
    # elimina il pass e implementa la tua soluzione
    factors: list = []
    divisore: int = 2

    while divisore <= n:
        if n%divisore == 0:
            factors.append(divisore)
            n //= divisore
        else:
            divisore += 1
    return factors
