#Nel gioco del blackjack, il valore di una mano è determinato dalla somma dei valori delle carte.
#  Ogni carta ha un valore compreso tra 2 e 11 compresi. Tuttavia, se una mano contiene un asso,
#  il valore dell'asso può essere 1 o 11, a seconda di quale sia più favorevole al giocatore in quel momento.
#  Dato un elenco di valori delle carte che rappresentano una mano di blackjack,
#  scrivi una funzione per determinare il valore totale della mano.

def blackjack_hand_total(cards: list[int]) -> int:
    # elimina il pass e inserisci il tuo codice
    sum: int= 0
    aces: list =[]
    for x in cards:
        if x == 1:
            aces.append(x)
        elif x == 11:
            aces.append(x)
        else:
            sum += x
    if aces != []:
        if (sum + (11 * len(aces))) <= 21:
            sum = sum + (11 * len(aces))
        else:
            for x in aces:
                if (sum + 11) <= 20:
                    sum += 11
                else:
                    sum += 1
    return sum

print(blackjack_hand_total([2, 3, 5])) #10
print(blackjack_hand_total([11, 5, 5])) #21
print(blackjack_hand_total([1, 10, 11])) #12
print(blackjack_hand_total([1, 10, 5])) #16
print(blackjack_hand_total([11, 5, 3])) #19