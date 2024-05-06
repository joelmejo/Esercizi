#Scrivi una funzione che accetta una stringa come input, rimuove le parole non significative
# comuni stop_words e restituisce un dizionario in cui le chiavi sono parole univoche nel testo rimanente
# (ignorando la distinzione tra maiuscole e minuscole e la punteggiatura) e i valori sono le frequenze di quelle parole.

def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    # eliminare il pass ed inserire il codice
    words: dict = {}
    text = text.lower()
    text = text.split()
    for i in range(len(text)):
        text[i] = text[i].strip('.')
        deleted_sw: int= 0
    for i in stopwords:
        for j in range(len(text)):
            if i == text[j - deleted_sw]:
                text.pop(j - deleted_sw)
                deleted_sw += 1
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words




text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
word_frequency(text, stopwords)
# Test 	
# stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
# text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
# print(word_frequency(text, stopwords))
	
# Result
# {'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 2, 'dog': 2, 'very': 1}