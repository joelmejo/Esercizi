# Immaginiamo di avere un tipo speciale di sistema numerico in cui gli unici elementi
# costitutivi sono i numeri 2, 3 e 5. Chiamiamo questi elementi costitutivi "fattori primi"
# perché non possono essere ulteriormente scomposti. Un "numero brutto" in questo sistema è
# un numero costruito utilizzando solo questi fattori primi (2, 3 o 5).
# Ad esempio, 6 (che può essere costruito come 2 x 3) è un numero brutto, ma 7 (che ha un fattore primo pari a 7) non lo è.

def ugly_number(num: int) -> bool:
    factors: list = [2, 3, 5]
    if num <= 1:
        return True
    flag: bool= True
    while flag == True:
        flag = False
        for i in factors:
            if(num%i)==0:
                num //= i
                flag = True
                if num == 1:
                    return True
    return False
            

print(ugly_number(6)) #True
print(ugly_number(1)) #True
print(ugly_number(14)) #False
print(ugly_number(1524)) #False
print(ugly_number(127621378199)) #False