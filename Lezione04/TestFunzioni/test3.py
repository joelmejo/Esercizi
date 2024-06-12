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
        text[i] = text[i].strip(',')
        text[i] = text[i].strip('?')
    for i in stopwords:
        for j in reversed(range(len(text))):
            if i == text[j]:
                text.pop(j)
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words




text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
print(word_frequency(text, stopwords))
# Test 	
# stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
# text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
# print(word_frequency(text, stopwords))
	
# Result
# {'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 2, 'dog': 2, 'very': 1}

stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
text2 = "The cat in the hat. The hat is blue and red. The cat and the dog."
print(word_frequency(text2, stopwords)) 
# Result
#{'cat': 2, 'hat': 2, 'blue': 1, 'red': 1, 'dog': 1}

stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
text3 = "I am I because I think I am. If I am not I, who am I?"
print(word_frequency(text3, stopwords))
# Result
# {'i': 7, 'am': 4, 'because': 1, 'think': 1, 'if': 1, 'not': 1, 'who': 1}

stopwords = ['be']
text4 = "To be, or not to be, that is the question."
print(word_frequency(text4, stopwords))
# Result
# {'to': 2, 'or': 1, 'not': 1, 'that': 1, 'is': 1, 'the': 1, 'question': 1}