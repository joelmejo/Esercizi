import unittest
from movie_genre import *
from noleggio import *
# ### Creazione di Test Case con UnitTest

# Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto
#  funzionamento delle classi Film, Azione, Commedia, Dramma, e Noleggio. 
# Istruzioni
# Creare un nuovo file Python denominato "test_blockbuster.py".
# Importare il modulo unittest e tutte le classi definite.
# Creare una sola classe di test chiamata TestFilm che eredita da unittest.TestCase.

class TestFilm(unittest.TestCase):
 
# Configurazione Iniziale:
# - Utilizzare il metodo setUp per creare l'ambiente di test:
#    - In setUp, istanziare 10 film (5 di azione, 4 commedie e 1 drammatico) e aggiungerli a una lista di film.
#    - Creare un oggetto Noleggio utilizzando la lista di film creata.

    def setUp(self) -> None:
        # Creazione di 5 film di Azione
        self.azione_film1 = Azione(1, "Azione Film 1")
        self.azione_film2 = Azione(2, "Azione Film 2")
        self.azione_film3 = Azione(3, "Azione Film 3")
        self.azione_film4 = Azione(4, "Azione Film 4")
        self.azione_film5 = Azione(5, "Azione Film 5")

        # Creazione di 4 film di Commedia
        self.commedia_film1 = Commedia(6, "Commedia Film 1")
        self.commedia_film2 = Commedia(7, "Commedia Film 2")
        self.commedia_film3 = Commedia(8, "Commedia Film 3")
        self.commedia_film4 = Commedia(9, "Commedia Film 4")

        # Creazione di 1 film di Drama
        self.drama_film = Drama(10, "Drama Film 1")

        # Unisci tutte le istanze di film in una lista
        self.films = [self.azione_film1, self.azione_film2, self.azione_film3, self.azione_film4, self.azione_film5, 
                self.commedia_film1, self.commedia_film2, self.commedia_film3, self.commedia_film4, 
                self.drama_film]

        self.noleggio = Noleggio(self.films)
        

# Testare la Disponibilità di un Film (isAvaible):
# - Scrivere un test per verificare che un film disponibile ritorni True.
# - Scrivere un test per verificare che un film non disponibile ritorni False.

    def test_availability(self):
        self.assertTrue(self.noleggio.isAvailable(self.commedia_film1))
        self.assertFalse(self.noleggio.isAvailable(Drama(10, 'Drama Film 2')))

# Testare il Noleggio di un Film (rentAMovie):
# - Scrivere un test per verificare che un film disponibile possa essere noleggiato correttamente.
# - Dopo il noleggio, verificare che il film non sia più disponibile.
# - Verificare che il film noleggiato appaia nella lista dei film noleggiati dal cliente.

    def test_rent(self):
        self.noleggio.rentAMovie(self.commedia_film1, 1)
        self.assertNotIn(self.commedia_film1, self.noleggio.film_list)
        self.assertIn(self.commedia_film1, self.noleggio.rented_film[1])

# Testare il Noleggio di un Film Non Disponibile:
# - Noleggiare un film con un cliente.
# - Provare a noleggiare lo stesso film con un altro cliente e verificare che non sia possibile.

    def test_unavailability(self):
        self.noleggio.rentAMovie(self.commedia_film1, 1)
        self.noleggio.rentAMovie(self.commedia_film1, 2)
        self.assertNotIn(self.commedia_film1, self.noleggio.rented_film.get(2, []))

# Testare la Restituzione di un Film (giveBack):
# - Noleggiare un film e poi restituirlo.
# - Verificare che il film restituito sia nuovamente disponibile.
# - Verificare che il film restituito non sia più nella lista dei film noleggiati dal cliente.

    def test_give_back(self):
        self.noleggio.rentAMovie(self.commedia_film1, 1)
        self.noleggio.giveBack(self.commedia_film1, 1, 3)
        self.assertNotIn(self.commedia_film1, self.noleggio.rented_film[1])

# Testare il Calcolo della Penale di Ritardo (calcolaPenaleRitardo):
# - Scrivere test per verificare il calcolo della penale di ritardo per film di diversi generi
#    (azione, commedia, dramma).

    def test_penale(self):
        self.noleggio.rentAMovie(self.commedia_film1, 1)
        self.assertEqual(self.noleggio.giveBack(self.commedia_film1, 1, 3), 7.5)
        self.noleggio.rentAMovie(self.azione_film1, 1)
        self.assertEqual(self.noleggio.giveBack(self.azione_film1, 1, 3), 9)
        self.noleggio.rentAMovie(self.drama_film, 1)
        self.assertEqual(self.noleggio.giveBack(self.drama_film, 1, 3), 6)

# Testare la Stampa dei Film Disponibili (printMovies):
# - Verificare che la lista dei film disponibili contenga i titoli corretti.

# Testare la Stampa dei Film Noleggiati da un Cliente (printRentMovies):
# - Noleggiare uno o più film per un cliente.
# - Verificare che la stampa dei film noleggiati contenga i titoli corretti.

if __name__ == '__main__':
    unittest.main()