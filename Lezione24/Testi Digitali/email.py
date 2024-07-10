from documento import *
class Email(Documento):
    def __init__(self, mittente: str, destinatario: str, titolo: str, testo: str = "") -> None:
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo = titolo
    
    def getMittente(self) -> str:
        return self.mittente
    
    def setMittente(self, mittente: str) -> None:
        self.mittente = mittente

    def getDestinatario(self) -> str:
        return self.destinatario
    
    def setDestinatario(self, destinatario: str) -> None:
        self.destinatario = destinatario
    
    def getTitolo(self) -> str:
        return self.titolo
    
    def setTitolo(self, titolo: str) -> None:
        self.titolo = titolo

    def getText(self) -> str:
        return f"Da: {self.mittente}, A: {self.destinatario}\nTitolo: {self.titolo}\nMessagio: {self.testo}"
    
    def setText(self, testo: str) -> None:
        return super().setText(testo)
    
    def isInText(self, parola: str) -> bool:
        return super().isInText(parola)
    
    def writeToFile(self, path: str) -> None:
        with open(path, 'w') as eb:
            eb.write(self.getText())