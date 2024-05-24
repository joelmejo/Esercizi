# Sistema di Prenotazione Cinema

# Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale,
# ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili e
# prenotare posti per un determinato spettacolo.

# Classi:
# - Film: Rappresenta un film con titolo e durata.
# - Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

#     Metodi:
#     - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili.
#            Restituisce un messaggio di conferma o di errore.
#     - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
# - Cinema: Gestisce le operazioni legate alla gestione delle sale.

#     Metodi:
#     - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
#     - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti.
#            Restituisce un messaggio di stato.

# Test case:
# - Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.

# - Un cliente sceglie un film e prenota un certo numero di posti.

# - Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

class Film:
    def __init__(self, titolo: str, durata: int) -> None:
        self.titolo = titolo
        self.durata = durata

class Sala:
    def __init__(self, numero: int, film: Film, posti_totali: int) -> None:
        self.numero = numero
        self.film = film
        self.posti_totali = posti_totali
        self.posti_prenotati = 0

    def prenota_posti(self, num_posti: int):
        if self.posti_totali >= (self.posti_prenotati + num_posti):
            self.posti_prenotati += num_posti
            return f"Posti prenotati: {num_posti}"
        else:
            return "Posti non disponibili."
    
    def posti_disponibili(self):
        return self.posti_totali - self.posti_prenotati
    
class Cinema:
    def __init__(self) -> None:
        self.sale = []
    
    def aggiungi_sala(self, sala: Sala):
        self.sale.append(sala)

    def prenota_film(self, titolo_film: str, num_posti: int):
        for sala in self.sale:
            if sala.film.titolo == titolo_film:
                return sala.prenota_posti(num_posti)
        return "Film non disponibile."

# Create an instance of Cinema
cinema = Cinema()

# Create instances of Film
film1 = Film("Film1", 120)
film2 = Film("Film2", 180)

# Create instances of Sala
sala1 = Sala(1, film1, 100)
sala2 = Sala(2, film2, 200)

# Add the salas to the cinema
cinema.aggiungi_sala(sala1)
cinema.aggiungi_sala(sala2)

# A customer chooses a movie and books a certain number of seats.
print(cinema.prenota_film("Film1", 70))
print(cinema.prenota_film("Film1", 30))
print(cinema.prenota_film("Film1", 1))

# The system checks availability and confirms or rejects the booking.
# This is done inside the prenota_film method.
