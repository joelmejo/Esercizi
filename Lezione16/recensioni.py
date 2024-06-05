# Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e
# una classe derivata Film che rappresenti specificamente un film. Gli studenti dovranno anche creare oggetti
# di queste classi, aggiungere valutazioni e visualizzare le recensioni.

# Specifiche della Classe Media:
# Attributi:
# - title (stringa): Il titolo del media.
# - reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

# Metodi:
# - set_title(self, title): Imposta il titolo del media.
# - get_title(self): Restituisce il titolo del media.
# - aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
# - getMedia(self): Calcola e restituisce la media delle valutazioni.
# - getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle
#            valutazioni.
# - ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
# - recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo,
#            il voto medio, il giudizio e le percentuali di ciascun voto. Esempio:
 
# Titolo del Film: The Shawshank Redemption
# Voto Medio: 3.80
# Giudizio: Bello
# Terribile: 10.00%
# Brutto: 10.00%
# Normale: 10.00%
# Bello: 30.00%
# Grandioso: 40.00%

# Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film,
# aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().

class Media:
    def __init__(self, title: str, reviews: list[int]) -> None:
        self.title = title
        self.reviews = reviews

    def set_title(self, title: str) -> None:
        self.title = title

    def get_title(self) -> str:
        return self.title
    
    def aggiungiValutazione(self, voto: int) -> None:
        if 1 <= voto <= 5:
            self.reviews.append(voto)

    def getMedia(self) -> float:
        media: float = 0
        for voto in self.reviews:
            media += voto
        return media / len(self.reviews)
    
    def getRate(self) -> str:
        media = self.getMedia()
        if media >= 5:
            return "Giudizio: Grandioso"
        elif media >= 4:
            return "Giudizio: Bello"
        elif media >= 3:
            return "Giudizio: Normale"
        elif media >= 2:
            return "Giudizio: Brutto"
        else:
            return "Giudizio: Terribile"
        
    def getPercentage(self, voto: int) -> str:
        return len(self.reviews) / self.reviews.count(voto) * 100
    
    def recensione(self) -> None:
        pass

class Film(Media):
    def __init__(self, title: str, reviews: list[int]) -> None:
        super().__init__(title, reviews)
    
    def set_title(self, title: str) -> None:
        return super().set_title(title)
    
    def get_title(self) -> str:
        return super().get_title()
    
    def aggiungiValutazione(self, voto: int) -> None:
        return super().aggiungiValutazione(voto)
    
    def getMedia(self) -> float:
        return super().getMedia()
    
    def getRate(self) -> str:
        return super().getRate()
    
    def getPercentage(self, voto: int) -> str:
        return super().getPercentage(voto)
    
    def recensione(self) -> None:
        print(f"Titolo del Film: {self.title}")
        print(f"Voto Medio: {self.getMedia():.2f}")
        print(f"Giudizio: {self.getRate()}")
        print(f"Terribile: {self.getPercentage(1):.2f}%")
        print(f"Brutto: {self.getPercentage(2):.2f}%")
        print(f"Normale: {self.getPercentage(3):.2f}%")
        print(f"Bello: {self.getPercentage(4):.2f}%")
        print(f"Grandioso: {self.getPercentage(5):.2f}%")

# Create a Film object
film = Film("Test Film", [])
# Test set_title and get_title methods
film.set_title("New Film Title")
assert film.get_title() == "New Film Title", "Error in set_title or get_title method"

# Test aggiungiValutazione method
film.aggiungiValutazione(5)
assert film.reviews == [5], "Error in aggiungiValutazione method"

# Test getMedia method
film.aggiungiValutazione(5)
assert film.getMedia() == 5.0, "Error in getMedia method"

# Test getRate method
assert film.getRate() == "Giudizio: Grandioso", "Error in getRate method"

# Test getPercentage method
assert film.getPercentage(5) == 100.0, "Error in getPercentage method"