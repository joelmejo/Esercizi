# Il calcolo del codice fiscale consta di 16 caratteri alfanumerici per i privati e di 11 per le persone giuridiche.

# Per le persone fisiche, i primi 15 caratteri si ottengono a partire dai dati personali:

#   Tre caratteri alfabetici composti dalle prime tre consonanti del cognome.
#   Tre caratteri alfabetici composti dalle prime tre consonanti del nome.
#   Nel caso in cui si abbiano più di tre consonanti, si usano la prima, la terza e la quarta.

# Sia per i caratteri del cognome che per quelli del nome, se hanno meno di tre consonanti,
# si inseriscono prima le vocali, fino ad arrivare ai tre caratteri. Se hanno meno di tre caratteri, si riempie con X.

#   Due caratteri numerici che rappresentano le ultime due cifre dell’anno di nascita.
#   Un carattere alfabetico che indica il mese di nascita
#       (A - Gennaio, B - Febbraio, C - Marzo, D - Aprile, E - Maggio, H - Giugno, L - Luglio,
#        M - Agosto, P - Settembre, R - Ottobre, S - Novembre, T - Dicembre).
#   Due caratteri numerici per il giorno di nascita. Per la donna, si somma 40 a tale numero.
#   Un carattere alfabetico per indicare il sesso.
#   Quattro caratteri che rappresentano la città di nascita (1 alfabetico e 3 numerici).
# L’ultimo carattere, alfabetico, ha una funzione di verifica.
#  L’esattezza di questa cifra fiscale dipenderà dall’esistenza o meno di due persone
#  con nome e cognome molto simili nati nello stesso giorno e nello stesso municipio.
#  In simili casi di 'omocodia', l’Agenzia delle Entrate darà a questo carattere una lettera assegnata progressivamente.


class Person:

    def __init__(self, name: str, surname: str, birth_date: str, birth_place: str, gender: str) -> None:

        self.__name: str = name
        self._surname: str = surname
        self._birth_date: str = birth_date
        self._birth_place: str = birth_place
        self._gender = gender
        self._ssn: str = ''
        self.compute_ssn()
        pass
    
    def compute_ssn(self) -> bool:
        """
        Compute the ssn
        """
        ssn: str = ''
        uppercase_consonants: list = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 
                                        'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
        
        uppercase_vowels = ['A', 'E', 'I', 'O', 'U']


        birth_month: dict = {
        "Gennaio": "A",
        "Febbraio": "B",
        "Marzo": "C",
        "Aprile": "D",
        "Maggio": "E",
        "Giugno": "H",
        "Luglio": "L",
        "Agosto": "M",
        "Settembre": "P",
        "Ottobre": "R",
        "Novembre": "S",
        "Dicembre": "T"
        }


        surname_characters: list = list(self._surname.upper)
        upper_surname_consonants: list = []
        for char in surname_characters:
            for consonant in uppercase_consonants:
                if char == consonant:
                    upper_surname_consonants.append(char)
                    break
            if len(upper_surname_consonants) == 3:
                break
        if len(upper_surname_consonants) < 3:
            add_count: int = 0
            for char in surname_characters:
                for consonant in uppercase_consonants:
                    if char != consonant:
                        upper_surname_consonants.insert(add_count, char)
                        add_count += 1
                        break
                if len(upper_surname_consonants) == 3:
                    break
        while len(upper_surname_consonants) < 3:
            upper_surname_consonants.append('X')

        ssn += (''.join(upper_surname_consonants))

        name_characters: list = list(self._name.upper)
        upper_name_consonants: list = []

        for char in name_characters:
            for consonant in uppercase_consonants:
                if char == consonant:
                    upper_name_consonants.append(char)
                    break
            if len(upper_name_consonants) == 3:
                break
        if len(upper_name_consonants) < 3:
            add_count: int = 0
            for char in name_characters:
                for consonant in uppercase_consonants:
                    if char != consonant:
                        upper_name_consonants.insert(add_count, char)
                        add_count += 1
                        break
                if len(upper_name_consonants) == 3:
                    break
        while len(upper_name_consonants) < 3:
            upper_name_consonants.append('X')

        


    def get_name(self) -> str:
        """
        This function returns a person's name
        input: none
        return: self._name: str, the function returns the person's name        
        """

        return self.__name
    
    def set_name(self, name: str) -> None:
        """
        This function set the attribute name
        input: name : str, the parameter contains the user's name
        return: None
        """

        raise Exception("You cannot modify the name!")
    
    def get_ssn(self) -> str:
        """
        This function return the ssn value
        input: none
        return: self._ssn: str, the function returns the ssn value
        """

        return self._ssn
    
    def set_ssn(self, ssn: str) -> None:
        """
        This function set the ssn
        input: name : str, the parameter contains the user's ssn
        return: None
        """

        raise Exception("You cannot modify the ssn!")


person_1: Person = Person(name='Valentino', surname='Rossi', birth_date='11/11/1999', birth_place='Roma', gender='Male')
