# Data una stringa s e una lista di stringhe wordDict, restituisce True se s può essere segmentato in una sequenza separata da spazi di una o più parole del dizionario; False altrimenti.

# Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.

def word_break(s: str, wordDict: list[str]) -> bool:
    for word in wordDict:
        if word in s:
            s = s.replace(word, '')
        else:
            return False
    return True

print(word_break("catsandog",["cats","dog","sand","and","cat"]))