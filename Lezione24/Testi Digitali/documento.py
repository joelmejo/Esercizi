class Documento:
    def __init__(self, testo: str) -> None:
        self.testo: str= testo

    def getText(self) -> str:
        return self.testo
    
    def setText(self, testo: str) -> None:
        self.testo = testo

    def isInText(self, parola: str) -> bool:
        return parola in self.testo