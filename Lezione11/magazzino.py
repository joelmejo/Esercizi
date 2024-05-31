# Gestione di un magazzino
# Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere
# prodotti al magazzino, cercare prodotti per nome e verificare la disponibilità di un prodotto.

# Definisci una classe Prodotto con i seguenti attributi:
# - nome (stringa)
# - quantità (intero)

class Prodotto:
    def __init__(self, nome: str, quantità: int) -> None:
        self.nome = nome
        self.quantità = quantità
 
# Definisci una classe Magazzino con i seguenti metodi:
# - aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
# - cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
# - verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.

class Magazzino:
    def __init__(self) -> None:
        self.prodotti = []
    
    def aggiungi_prodotto(self, prodotto: Prodotto) -> None:
        self.prodotti.append(prodotto)
    
    def cerca_prodotto(self, nome: str):
        for prodotto in self.prodotti:
            if prodotto.nome == nome:
                return prodotto
        return None
    
    def verifica_disponibilità(self, nome: str) -> str:
        prodotto = self.cerca_prodotto(nome)
        if prodotto is None:
            return f"{nome} non trovato."
        if prodotto.quantità > 0:
            return f"{prodotto.nome} disponibile."
        else:
            return f"{prodotto.nome} non disponibile."