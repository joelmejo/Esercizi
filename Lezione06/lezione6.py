import pandas as pd

# source: https://www.agenziaentrate.gov.it/portale/web/guest/schede/istanze/richiesta-ts_cf/informazioni-codificazione-pf
# Il calcolo del codice fiscale consta di 16 caratteri alfanumerici per i privati e di 11 per le persone giuridiche.

# Per le persone fisiche, i primi 15 caratteri si ottengono a partire dai dati personali:

#   Tre caratteri alfabetici composti dalle prime tre consonanti del cognome.
#   Tre caratteri alfabetici composti dalle prime tre consonanti del nome.
#       Nel caso in cui si abbiano più di tre consonanti, si usano la prima, la terza e la quarta.

# Sia per i caratteri del cognome che per quelli del nome, se hanno meno di tre consonanti,
# si inseriscono prima le vocali, fino ad arrivare ai tre caratteri. Se hanno meno di tre caratteri, si riempie con X.

# Due caratteri numerici che rappresentano le ultime due cifre dell’anno di nascita.
# Un carattere alfabetico che indica il mese di nascita
#       (A - Gennaio, B - Febbraio, C - Marzo, D - Aprile, E - Maggio, H - Giugno, L - Luglio,
#        M - Agosto, P - Settembre, R - Ottobre, S - Novembre, T - Dicembre).
# Due caratteri numerici per il giorno di nascita. Per la donna, si somma 40 a tale numero.
# Quattro caratteri che rappresentano la città di nascita (1 alfabetico e 3 numerici).
# L’ultimo carattere, alfabetico, ha una funzione di verifica.
#  L’esattezza di questa cifra fiscale dipenderà dall’esistenza o meno di due persone
#  con nome e cognome molto simili nati nello stesso giorno e nello stesso municipio.
#  In simili casi di 'omocodia', l’Agenzia delle Entrate darà a questo carattere una lettera assegnata progressivamente.
#
# Convertire in numeri i caratteri di posizione pari;
# Convertire in numeri i caratteri di posizione dispari;
# Addizionare tutti i valori ottenuti e dividerli per 26;
# Determinare una lettera alfabetica corrispondente al resto dell’operazione.


class Person:

    def __init__(self, name: str, surname: str, birth_date: str, birth_place: str, gender: str) -> None:

        self._name: str = name
        self._surname: str = surname
        self._birth_date: str = birth_date
        self._birth_place: str = birth_place
        self._gender = gender
        self._ssn: str = self.compute_ssn()

    def compute_name_consonants(self, uppercase_char_list: list) -> list:
        uppercase_consonants: list = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 
                                        'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
        
        uppercase_vowels = ['A', 'E', 'I', 'O', 'U']
        
        upper_consonants: list = []

        for char in uppercase_char_list:
            for consonant in uppercase_consonants:
                if char == consonant:
                    upper_consonants.append(char)
                    break
            if len(upper_consonants) == 4:
                upper_consonants.pop(1)
                break
        if len(upper_consonants) < 3:
            add_count: int = 0
            for char in uppercase_char_list:
                for vowel in uppercase_vowels:
                    if char == vowel:
                        upper_consonants.insert(add_count, char)
                        add_count += 1
                        break
                if len(upper_consonants) == 3:
                    break
        while len(upper_consonants) < 3:
            upper_consonants.append('X')
        
        return upper_consonants

    def compute_surname_consonants(self, uppercase_char_list: list) -> list:
        uppercase_consonants: list = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 
                                        'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
        
        uppercase_vowels = ['A', 'E', 'I', 'O', 'U']
        
        upper_consonants: list = []

        for char in uppercase_char_list:
            for consonant in uppercase_consonants:
                if char == consonant:
                    upper_consonants.append(char)
                    break
            if len(upper_consonants) == 3:
                break
        if len(upper_consonants) < 3:
            add_count: int = 0
            for char in uppercase_char_list:
                for vowel in uppercase_vowels:
                    if char == vowel:
                        upper_consonants.insert(add_count, char)
                        add_count += 1
                        break
                if len(upper_consonants) == 3:
                    break
        while len(upper_consonants) < 3:
            upper_consonants.append('X')
        
        return upper_consonants

    
    def compute_ssn(self) -> bool:
        """
        This function computes the ssn
        """
        ssn: str = ''

        months: dict =  {
                            "01": "A",
                            "02": "B",
                            "03": "C",
                            "04": "D",
                            "05": "E",
                            "06": "H",
                            "07": "L",
                            "08": "M",
                            "09": "P",
                            "10": "R",
                            "11": "S",
                            "12": "T"
                        }
        
        cities_data = pd.read_csv(filepath_or_buffer='Lezione6/data/codici_comuni_10-05-2024.csv', sep=';', header=0, usecols=['DESCRIZIONE COMUNE', 'CODICE BELFIORE'], index_col='DESCRIZIONE COMUNE', encoding='latin-1')

        uppercase_surname_characters: list = list(self._surname.upper())
        ssn += (''.join(self.compute_surname_consonants(uppercase_surname_characters)))

        uppercase_name_characters: list = list(self._name.upper())
        ssn += (''.join(self.compute_name_consonants(uppercase_name_characters)))

        birth_day, birth_month, birth_year = self._birth_date.split('/')
        year: list = list(birth_year)
        ssn += (''.join(year[-2:]))

        ssn += months[birth_month]

        day: int= int(birth_day)
        if self._gender == 'F':
            day += 40

        ssn += str(day)

        cadastral_code: str = cities_data.loc[self._birth_place.upper()]['CODICE BELFIORE']

        ssn += cadastral_code

        conversion_table_odds: dict = {
                                    '0': 0, '1': 1, '2': 5, '3': 7, '4': 9, '5': 13, '6': 15, '7': 17, '8': 19, '9': 21,
                                    'A': 1, 'B': 0, 'C': 5, 'D': 7, 'E': 9, 'F': 13, 'G': 15, 'H': 17, 'I': 19, 'J': 21,
                                    'K': 2, 'L': 4, 'M': 18, 'N': 20, 'O': 11, 'P': 3, 'Q': 6, 'R': 8, 'S': 12,
                                    'T': 14, 'U': 16, 'V': 10, 'W': 22, 'X': 25, 'Y': 24, 'Z': 23
                                    }
        
        conversion_table_even: dict = {
                                    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                                    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
                                    'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
                                    }
            
        conversion_table_remainder: dict = {
                                        '0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J',
                                        '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T',
                                        '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z'
                                        }
        
        odd_even_flag: bool = False
        compute_check_digit: list =[]
        for char in ssn:
            if odd_even_flag == True:
                compute_check_digit.append(conversion_table_even[char])
                odd_even_flag = False
            else:
                compute_check_digit.append(conversion_table_odds[char])
                odd_even_flag = True

        check_digit: int = conversion_table_remainder[str(sum(compute_check_digit) % 26)]

        ssn += check_digit

        return ssn


    def get_name(self) -> str:
        """
        This function returns a person's name
        input: none
        return: self._name: str, the function returns the person's name        
        """

        return self._name
    
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


person_1: Person = Person(name='Mario', surname='Rossi', birth_date='11/11/1999', birth_place='Roma', gender='M')

print(person_1.get_ssn())