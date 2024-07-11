from time import time
# Esercizio 1 - Crea un decorator  che stampa n volte l'output della funzione decorata chiamandola due volte.

def tenprints(n):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(2):
                result = func(*args, **kwargs)
            for _ in range(n):
                print(result)
        return wrapper
    return actual_decorator

@tenprints(n=3)
def test_function():
    return "Hello World!"

test_function()


# Esercizio 2 - Crea un decorator che calcola il tempo di esecuzione della funzione che viene decorata.

def performance(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        finish = time()
        elapsed_time = finish - start
        print(elapsed_time)
    return wrapper


# Esercizio 3 - Crea un decorator che permette di memorizzare informazioni sulla fibonacci in modo tale che non
#  sia necessario ricalcolare i valori gia calcolati