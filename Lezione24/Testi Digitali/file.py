from documento import *

class File(Documento):
    def __init__(self, path: str, testo: str = "") -> None:
        super().__init__(testo)
        self.path = path
        with open(self.path, 'w') as t:
            t.write(testo)

    def leggiTestoDaFile(self) -> str:
        with open(self.path, 'r') as f:
            testo: str= f.read()
        return f"Percorso: {self.path}\nTesto: {testo}"