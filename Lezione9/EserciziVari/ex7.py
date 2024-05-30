# Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

# Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, in genere utilizzando tutte le lettere originali esattamente una volta.

def anagram(s: str, t: str) -> bool:
    # scrivere qui il codice
    s = s.lower()
    t = t.lower()
    s = list(s)
    t = list(t)
    s_dict: dict= {}
    for char in s:
        if char not in s_dict.keys():
            s_dict[char] = 1
        else:
            s_dict[char] += 1
    t_dict: dict= {}
    for char in t:
        if char not in t_dict.keys():
            t_dict[char] = 1
        else:
            t_dict[char] += 1
    for key in s_dict.keys():
        if key not in t_dict:
            return False
        else:
            if s_dict[key] != t_dict[key]:
                return False
    return True

print(anagram("anagram","nagaram")) #True

print(anagram("rat", "car")) #False

print(anagram("silent","listen")) #True

print(anagram("NeurIPS","UniReps")) #True