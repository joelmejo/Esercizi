# 1. GESTIONALE PAGAMENTO
# Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza
#  l'importo del pagamento e si definiscano appropriati metodi get() e set(). L'importo non è un parametro
#  da passare in input alla classe Pagamento ma deve essere inizializzato utilizzando il metodo set() dove
#  opportuno. Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive l'importo
#  del pagamento, ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con
#  2 cifre decimali.

class Pagamento:
    def __init__(self) -> None:
        self._importo = None

    def getImporto(self) -> float:
        return self._importo
    
    def setImporto(self, importo: float) -> None:
        self._importo = importo

    def dettagliPagamento(self) -> None:
        print(f"Importo del pagamento: {self._importo:.2f}")

# Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo.
#  Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti.
#  Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro,
#  50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro,
#  0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.

class PagamentoContanti(Pagamento):
    def __init__(self) -> None:
        super().__init__()

    def dettagliPagamento(self) -> None:
        print(f"Pagamento in contanti di: €{self._importo:.2f}")

    def inPezziDa(self) -> None:
        denominations = {
            500: [0, 'banconota', 'banconote'],
            200: [0, 'banconota', 'banconote'],
            100: [0, 'banconota', 'banconote'],
            50: [0, 'banconota', 'banconote'],
            20: [0, 'banconota', 'banconote'],
            10: [0, 'banconota', 'banconote'],
            5: [0, 'banconota', 'banconote'],
            2: [0, 'moneta', 'monete'],
            1: [0, 'moneta', 'monete'],
            0.50: [0, 'moneta', 'monete'],
            0.20: [0, 'moneta', 'monete'],
            0.10: [0, 'moneta', 'monete'],
            0.05: [0, 'moneta', 'monete'],
            0.01: [0, 'moneta', 'monete']
        }
        resto: float = self._importo
        while resto > 0:
            for d in denominations.keys():
                while resto >= d:
                    resto = round(resto - d, 2)
                    denominations[d][0] += 1

        for d in denominations.keys():
            if denominations[d][0] != 0:
                if denominations[d][0] > 1:
                    print(f"{denominations[d][0]} {denominations[d][2]} da {d} euro")
                else:
                    print(f"{denominations[d][0]} {denominations[d][1]} da {d} euro")

# Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo.
#  Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza,
#  e il numero della carta di credito. Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte
#  le informazioni della carta di credito oltre all'importo del pagamento.

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, titolare: str, scadenza: str, numero_carta: int) -> None:
        super().__init__()
        self._titolare = titolare
        self._scadenza = scadenza
        self._numero_carta = numero_carta
    
    def dettagliPagamento(self) -> None:
        print(f"Pagamento di: €{self._importo:.2f} effettuato con la carta di credito\nTitolare: {self._titolare}\nNumero carta: {self._numero_carta}\nScadenza carta: {self._scadenza}")


# Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito
#  con valori differenti e si invochi dettagliPagamento() per ognuno di essi.

# Create PagamentoContanti objects
pagamento_contanti1 = PagamentoContanti()
pagamento_contanti1.setImporto(150)
pagamento_contanti2 = PagamentoContanti()
pagamento_contanti2.setImporto(95.25)

# Call dettagliPagamento and inPezziDa methods
pagamento_contanti1.dettagliPagamento()
pagamento_contanti1.inPezziDa()
pagamento_contanti2.dettagliPagamento()
pagamento_contanti2.inPezziDa()

# Create PagamentoCartaDiCredito objects
pagamento_carta1 = PagamentoCartaDiCredito("Mario Rossi", "12/24", 1234567890123456)
pagamento_carta1.setImporto(200)
pagamento_carta2 = PagamentoCartaDiCredito("Luigi Bianchi", "01/25", 6543210987654321)
pagamento_carta2.setImporto(500)

# Call dettagliPagamento method
pagamento_carta1.dettagliPagamento()
pagamento_carta2.dettagliPagamento()

# Esempio di output:
# Pagamento in contanti di: €150.00
# 150.00 euro da pagare in contanti con:
# 1 banconota da 100 euro
# 1 banconota da 50 euro

# Pagamento in contanti di: €95.25
# 95.25 euro da pagare in contanti con:
# 1 banconota da 50 euro
# 2 banconote da 20 euro
# 1 banconota da 5 euro
# 1 moneta da 0.2 euro
# 1 moneta da 0.05 euro

# Pagamento di: €200.00 effettuato con la carta di credito
# Nome sulla carta: Mario Rossi
# Data di scadenza: 12/24
# Numero della carta: 1234567890123456

# Pagamento di: €500.00 effettuato con la carta di credito
# Nome sulla carta: Luigi Bianchi
# Data di scadenza: 01/25
# Numero della carta: 6543210987654321