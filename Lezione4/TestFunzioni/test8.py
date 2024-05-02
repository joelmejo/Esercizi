# Immagina di avere uno scrigno pieno di gioielli (rappresentati da una lista di numeri interi).
# Questi gioielli hanno vari valori, alcuni più preziosi di altri.
# Il tuo compito è trovare il terzo gioiello distinto più prezioso nello scrigno.
# Qual è la svolta?
# Nello scrigno possono esserci gioielli duplicati (numeri con lo stesso valore).
# A noi però interessano solo valori distinti, ovvero gioielli con valori unici.
# Scrivi una funzione che prenda come input questo array di valori di gioielli (numeri).
# Se nello scrigno sono presenti almeno tre valori distinti,
# la funzione dovrebbe restituire il valore del terzo gioiello distinto di maggior valore.
# Ma c'è un problema!
# Se non ci sono tre valori distinti (ad esempio, solo due valori univoci o tutti i valori sono uguali),
# la funzione dovrebbe restituire il valore del gioiello più prezioso nello scrigno.

def third_max(nums: list[int]) -> int:
    # elimina il pass e inserisci il tuo codice
    # potete utilizzare queste tre variabili di comodo
    first_max = second_max = third_max = float('-inf')
    pass