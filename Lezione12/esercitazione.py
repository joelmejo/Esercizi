
# Sistema Avanzato di Gestione Biblioteca

# Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve
# permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi.
# Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli
# e visualizzare quali libri sono disponibili in un dato momento.

# Classi:
# - Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente
#            disponibile (non prestato).

# - Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

#     Metodi:
#     - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca.
#                            Restituisce un messaggio di conferma.

#     - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato,
#                            lo segna come disponibile. Restituisce un messaggio di stato.

#     - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile.
#                                    Restituisce un messaggio di stato.

#     - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili.
#                                    Se non ci sono libri disponibili, restituisce un messaggio di errore.

# Test Cases:
# - Un amministratore della biblioteca aggiunge alcuni libri all'inventario.

# - Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.

# - L'utente restituisce il libro, che viene marcato di nuovo come disponibile.

# - In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.

class Libro:
    def __init__(self, titolo: str, autore: str) -> None:
        self.titolo = titolo
        self.autore = autore
        self.prestato: bool = False
    
    def cambia_stato_prestito(self):
        if self.prestato == True:
            self.prestato = False
        else:
            self.prestato = True
    
    def __str__(self) -> str:
        return f"{self.titolo} di {self.autore}"

class Biblioteca:
    def __init__(self) -> None:
        self.libri: list[Libro] = []
    
    def aggiungi_libro(self, libro: Libro) -> str:
        self.libri.append(libro)
        return "Libro aggiunto correttamente."
    
    def presta_libro(self, titolo: Libro) -> str:
        for libro in self.libri:
            if titolo == libro.titolo:
                if libro.prestato == False:
                    libro.cambia_stato_prestito()
                    return "Libro prestato correttamente."
                else:
                    return "Libro non disponibile."
        else:
            return "Libro non presente a catalogo."
    
    def restituisci_libro(self, titolo) -> str:
        for libro in self.libri:
            if titolo == libro.titolo:
                if libro.prestato == True:
                    libro.cambia_stato_prestito()
                    return "Libro restituito correttamente."
        else:
            return "Libro non presente a catalogo."
    
    def mostra_libri_disponibili(self):
        for libro in self.libri:
            if libro.prestato == False:
                print(libro)

# # Create a new library
# biblio = Biblioteca()

# # Create new books
# libro1 = Libro("Il nome della rosa", "Umberto Eco")
# libro2 = Libro("1984", "George Orwell")

# # Add books to the library
# assert biblio.aggiungi_libro(libro1) == "Libro aggiunto correttamente."
# assert biblio.aggiungi_libro(libro2) == "Libro aggiunto correttamente."

# # Borrow a book
# assert biblio.presta_libro("1984") == "Libro prestato correttamente."
# assert libro2.prestato == True

# # Return a book
# assert biblio.restituisci_libro("1984") == "Libro restituito correttamente."
# assert libro2.prestato == False

# # Show available books
# biblio.mostra_libri_disponibili()


############################################################

# Catalogo Film

# Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere
# e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare tutti i registi
# e i loro film.

# Classe:
# - MovieCatalog(): Gestisce tutte le operazioni legate al catalogo dei film.

#     Metodi:
#     - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo.
#                    Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista
#                    di film viene aggiornata.

#     - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista.
#                    Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

#     - list_directors(): Elenca tutti i registi presenti nel catalogo.

#     - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

#     - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo.
#                    Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata
#                    o un messaggio di errore se nessun film contiene la parola cercata nel titolo.

class MovieCatalog:
    def __init__(self) -> None:
        self.directors_dict: dict[str, list[str]] = {}
    
    def add_movie(self, director_name: str, movies: list[str]) -> None:
        if director_name not in self.directors_dict:
            self.directors_dict[director_name] = movies
        else:
            for movie in movies:
                self.directors_dict[director_name].append(movie)

    def remove_movie(self, director_name, movie_name) -> None:
        if director_name in self.directors_dict:
            if movie_name in self.directors_dict[director_name]:
                self.directors_dict[director_name].remove(movie_name)
            if self.directors_dict[director_name] == []:
                self.directors_dict.pop(director_name)

    def list_directors(self) -> None:
        for director in self.directors_dict.keys():
            print(director)

    def get_movies_by_director(self, director_name) -> list:
        if director_name in self.directors_dict:
            return self.directors_dict[director_name]
        
    def search_movies_by_title(self, title) -> dict:
        result: dict[str, list[str]] = {}
        for director in self.directors_dict.keys():
            for movie in self.directors_dict[director]:
                if title in movie:
                    if director not in result:
                        result[director] = [movie]
                    else:
                        result[director].append(movie)
        return result
    

# Create a new movie catalog
catalog = MovieCatalog()

# Add movies to a director
catalog.add_movie("Christopher Nolan", ["Inception", "The Dark Knight", "Interstellar"])
assert catalog.get_movies_by_director("Christopher Nolan") == ["Inception", "The Dark Knight", "Interstellar"]

# Add movies to another director
catalog.add_movie("Quentin Tarantino", ["Pulp Fiction", "Reservoir Dogs", "Kill Bill"])
assert catalog.get_movies_by_director("Quentin Tarantino") == ["Pulp Fiction", "Reservoir Dogs", "Kill Bill"]

# Remove a movie from a director
catalog.remove_movie("Christopher Nolan", "Inception")
assert catalog.get_movies_by_director("Christopher Nolan") == ["The Dark Knight", "Interstellar"]

# Try to remove a movie that doesn't exist
catalog.remove_movie("Christopher Nolan", "Memento")
assert catalog.get_movies_by_director("Christopher Nolan") == ["The Dark Knight", "Interstellar"]

# Try to remove a movie from a director that doesn't exist
catalog.remove_movie("Steven Spielberg", "Jaws")
assert catalog.get_movies_by_director("Steven Spielberg") is None

# Get all movies by a director
assert catalog.get_movies_by_director("Christopher Nolan") == ["The Dark Knight", "Interstellar"]

# Try to get movies by a director that doesn't exist
assert catalog.get_movies_by_director("Steven Spielberg") is None

# Search for movies by title
assert catalog.search_movies_by_title("Dark") == {"Christopher Nolan": ["The Dark Knight"]}

# Search for a title that doesn't exist
assert catalog.search_movies_by_title("Alien") == {}

# Search for a title that exists in multiple director's movies
catalog.add_movie("Ridley Scott", ["Alien", "Blade Runner"])
assert catalog.search_movies_by_title("Alien") == {"Ridley Scott": ["Alien"]}

