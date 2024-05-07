# Date due stringhe note e magazine, restituisci true se note può essere costruita utilizzando
#  le lettere di magazine e false in caso contrario. Ogni lettera nella magazine può essere utilizzata solo una volta in note.

def ransom(note: str, magazine: str) -> bool:
    if note == "":
        return True
    note_char_count: dict = {}
    magazine_char_count: dict = {}
    note_list: list= list(note)
    for i in note_list:
        if i in note_char_count:
            note_char_count[i] += 1
        else:
            note_char_count[i] = 1
            magazine_char_count[i] = 0
    magazine_list: list= list(magazine)
    for i in magazine_list:
        if i in magazine_char_count:
            magazine_char_count[i] += 1
    for key in magazine_char_count.keys():
        if magazine_char_count[key] < note_char_count[key]:
            return False
    return True

print(ransom("a","b")) #False
print(ransom("aa", "ab")) #False
print(ransom("aa","aab")) #True
print(ransom("tu sei un figo", "bella per te stai zitto. figo di qua e di là")) #False
print(ransom("","ciao")) #True
print(ransom("tu sei un figo", "bella per te! ne vuoi stare zitto? figo di qua e di là... senza offesa")) #True