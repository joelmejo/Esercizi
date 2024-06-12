# ### CLASSE: Film
# In un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio.
#  In tale classe, definire un codice identificativo (int) ed un titolo (string). Entrambi gli attributi
#  sono da considerarsi privati.
 
# - Definire i seguenti metodi:

#     init(id, title): metodo costruttore.

#     setID(id): che consente di impostare il codice identificativo del film, modificando il valore del
#        relativo attributo.

#     setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore
#        del relativo attributo.

#     getID(): che consente di ritornare il valore del codice identificativo di un film.

#     getTitle(): che consente di ritornare il valore del titolo di un film.

#     isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.  

class Film:
    def __init__(self, id: int, title: str) -> None:
        self._id = id
        self._title = title

    def setID(self, id: int) -> None:
        self._id = id

    def setTitle(self, title: str) -> None:
        self._title = title

    def getID(self) -> int:
        return self._id
    
    def getTitle(self) -> str:
        return self._title
    
    def isEqual(self, otherFilm: 'Film') -> bool:
        return self._id == otherFilm._id