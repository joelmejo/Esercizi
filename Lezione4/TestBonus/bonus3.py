# Dato un numero intero, restituisce una stringa che ne rappresenta la rappresentazione esadecimale.
# Per gli interi negativi viene utilizzato il metodo del complemento a due.

# Tutte le lettere nella stringa di risposta dovrebbero essere caratteri minuscoli
# e non dovrebbero esserci zeri iniziali nella risposta tranne lo zero stesso.

# Nota: non è consentito utilizzare alcun metodo di libreria integrato per risolvere direttamente questo problema.

def to_hex(num: int) -> str:
    hexa: str= ''
    hx: dict= {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f'
    }
    if num >= 0:
        resto: list= []
        while num //16 > 0:
            resto.append(num % 16)
            num //= 16
        resto.append(num)
        resto.reverse()
        for i in resto:
            hexa += hx[i]
        return hexa

print(to_hex(26)) # 1a
print(to_hex(-1)) # ffffffff
print(to_hex(1261)) # 4ed