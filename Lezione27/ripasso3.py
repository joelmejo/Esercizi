# Progettare un sistema di videonoleggio con i seguenti requisiti:

# 1. Classe Movie:

# Attributi:

#     movie_id: str - Identificatore di un film.
#     title: str - Titolo del film.
#     director: str - Regista del film.
#     is_rented: boolean - Booleano che indica se il film è noleggiato o meno.

# Metodi:

#     rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film non è già noleggiato imposta
#        is_rented a True, altrimenti stampa il messaggio "Il film '{self.title}' è già noleggiato."
#     return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato imposta is_rented a False,
#        altrimenti stampa il messaggio "Il film '{self.title}' non è stato noleggiato da questo cliente."

# 2. Classe Customer:

# Attributi:

#     customer_id: str - Identificativo del cliente.
#     name: str - Nome del cliente.
#     rented_movies: list[Movie] - Lista dei film noleggiati.

# Metodi:

#     rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già stato noleggiato, altrimenti
#        stampa il messaggio "Il film '{movie.title}' è già noleggiato."
#     return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già presente, altrimenti stampa
#        il messaggio "Il film '{movie.title}' non è stato noleggiato da questo cliente."

# 3. Classe VideoRentalStore:

# Attributi:

#     movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore l'oggetto Movie.
#     customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per valore l'oggetto Customer.

# Metodi:

#     add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel videonoleggio se non è già
#        presente, altrimenti stampa il messaggio "Il film con ID '{movie_id}' esiste già."
#     register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel videonoleggio se non è già
#        presente, altrimenti stampa il messaggio "Il cliente con ID '{customer_id}' è già registrato."
#     rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un film se entrambi esistono
#        nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
#     return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un film se entrambi esistono
#        nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
#     get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film noleggiati dal client
#        (customer.rented_movies) se il cliente esiste nel videonoleggio, altrimenti stampa il messaggio
#        "Cliente non trovato." e ritorna una lista vuota.

# Creazione di un nuovo videonoleggio
videonoleggio = VideoRentalStore()

# Aggiunta di nuovi film
videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")

# Registrazione di nuovi clienti
videonoleggio.register_customer("101", "Alice")
videonoleggio.register_customer("102", "Bob")

# Noleggio di film
videonoleggio.rent_movie("101", "1")
videonoleggio.rent_movie("102", "2")

# Tentativo di noleggiare un film già noleggiato
videonoleggio.rent_movie("101", "1")

# Restituzione di film
videonoleggio.return_movie("101", "1")

# Tentativo di restituire un film non noleggiato
videonoleggio.return_movie("101", "1")

# Ottenere la lista dei film noleggiati da un cliente
rented_movies_alice = videonoleggio.get_rented_movies("101")
print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

rented_movies_bob = videonoleggio.get_rented_movies("102")
print(f"Film noleggiati da Bob: {[movie.title for movie in rented_movies_bob]}")

	
# Expected
# Il film 'Inception' è già noleggiato.
# Il film 'Inception' non è stato noleggiato da questo cliente.
# Film noleggiati da Alice: []
# Film noleggiati da Bob: ['The Matrix']

# Creazione di un nuovo videonoleggio
videonoleggio = VideoRentalStore()

# Aggiunta di nuovi film
videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")
videonoleggio.add_movie("3", "Interstellar", "Christopher Nolan")

# Registrazione di nuovi clienti
videonoleggio.register_customer("101", "Alice")

# Noleggio di più film
videonoleggio.rent_movie("101", "1")
videonoleggio.rent_movie("101", "2")

# Verifica dei film noleggiati da Alice
rented_movies_alice = videonoleggio.get_rented_movies("101")
print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

	
# Expected
# Film noleggiati da Alice: ['Inception', 'The Matrix']