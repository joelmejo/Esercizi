# Dato un numero intero, restituisce una stringa che ne rappresenta la rappresentazione esadecimale.
# Per gli interi negativi viene utilizzato il metodo del complemento a due.

# Tutte le lettere nella stringa di risposta dovrebbero essere caratteri minuscoli
# e non dovrebbero esserci zeri iniziali nella risposta tranne lo zero stesso.

# Nota: non è consentito utilizzare alcun metodo di libreria integrato per risolvere direttamente questo problema.

def to_hex(num: int) -> str:
    resto: list= []
    while num //16 == 0:
        resto.append(num % 16)
    

print(to_hex(26)) #1a
print(to_hex(-1)) #ffffffff
print(to_hex(1261)) #4ed