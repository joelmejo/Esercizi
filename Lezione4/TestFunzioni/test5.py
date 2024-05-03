# Sei un detective esperto nel mondo dei testi e un caso sconcertante è arrivato sulla tua scrivania.
# Due stringhe, s e t, sono i tuoi sospettati. La tua missione: determinare se s
#  si nasconde in bella vista all'interno di t, ma con una svolta!

# Qual è il problema?

# Non puoi semplicemente confrontare le stringhe lettera per lettera.
#  Immagina che s sia un personaggio subdolo che cerca di confondersi tra la folla (t).
#  Potrebbero camuffarsi nascondendosi tra altri personaggi, ma non cambiano mai il loro ordine!
#  Quindi, "ace" può intrufolarsi in "abcde" (rimuove semplicemente "b" e "d"), ma "aec" non funzionerebbe (l'ordine cambia).

# Scrivi una funzione di interruzione del codice che prenda la stringa s (il carattere subdolo)
#  e t (la folla) come input. Se è possibile trovare s in agguato all'interno di t
#  mantenendo il suo travestimento (ordine), restituisce True. Altrimenti restituisce False.
#  Dimostra le tue abilità da detective e svela la verità nascosta!

def is_subsequence(s: str, t: str) -> bool:
    # elimina pass e inserisci il tuo codice
    s_list = list(s)
    t_list = list(t)

    if s == "":
        return True

    for i in range(len(s_list)):
        exists_flag = False
        for j in range(len(t_list)):
            if s_list[i] == t_list[j]:
                exists_flag = True
                for g in range(len(t_list) -j):
                    if s_list[i +1] == t_list[g + j]:
                        for f in range(len(t_list) -j -g):
                            if s_list[i + f] == t_list[g + j]:
                                return True
        return False
        if exists_flag is False:
            return False


    return False

print(is_subsequence("abc", "ahbgdc")) #True
print(is_subsequence("axc", "ahbgdc")) #False
print(is_subsequence("abc", "abcde")) #True
print(is_subsequence("abc", "cab")) #False
print(is_subsequence("", "ahbgdc")) #True
print(is_subsequence("abc", "")) #False