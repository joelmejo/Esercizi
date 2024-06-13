from abc import ABC, abstractmethod
# 2. RENDERING GRAFICO
# Si vuole sviluppare un sistema in Python per gestire il rendering di diverse forme geometriche.
#  Il sistema dovrà supportare almeno tre tipi di forme: quadrati, rettangoli, e triangoli rettangoli.

# Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome
#  della forma e le funzionalità base di ogni forma, come i metodi astratti getArea() per calcolare
#  l'area e render() per disegnare su schermo la forma.

class Forma(ABC):
    @abstractmethod
    def __init__(self, nome: str) -> None:
        self.nome = nome

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def render(self):
        pass

# Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza
#  di un suo lato.
# Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare
#  il nome della forma su "Quadrato".

class Quadrato(Forma):
    def __init__(self, lato: float) -> None:
        super().__init__('Quadrato')
        self.lato = lato

# Il metodo getArea() deve calcolare l'area del quadrato.

    def getArea(self) -> float:
        return self.lato * self.lato

# Il metodo render() deve stamapre su schermo un quadrato avente lato pari al valore passato nel
#  costruttore. Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi
#  ("*") lungo il suo perimetro. (Vedi Esempio di output)

    def render(self) -> None:
        for i in range(self.lato):
            slice: str= ""
            if i == 0 or i == self.lato - 1:
                slice = '* ' * self.lato
            else:
                slice = '* ' + '  ' * (self.lato -2) + '*'
            print(slice)

x = Quadrato(5)
x.render()


# Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza
#  della sua base e della sua altezza.
# Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo,
#  ed impostare il nome della forma su "Rettangolo".

class Rettangolo(Forma):
    def __init__(self, base: float, altezza: float) -> None:
        super().__init__('Rettangolo')
        self.base = base
        self.altezza = altezza

# Il metodo getArea() deve calcolare l'area del rettangolo.

    def getArea(self) -> float:
        return self.base * self.altezza

# Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori
#  passati nel costruttore. Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente
#  degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

    def render(self) -> None:
        for i in range(self.altezza):
            slice: str= ""
            if i == 0 or i == self.altezza - 1:
                slice = '* ' * self.base
            else:
                slice = '* ' + '  ' * (self.base - 2) + '*'
            print(slice)

y = Rettangolo(10,5)
y.render()


# Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione
#  di un lato del trinagolo (per semplicità, si suppone che il triangolo in questione sia un
#  triangolo rettangolo).
# Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare
#  il nome della forma su "Triangolo".

class Triangolo(Forma):
    def __init__(self, base: float, altezza: float) -> None:
        super().__init__('Triangolo')
        self.base = base
        self.altezza = altezza

# Il metodo getArea() deve calcolare l'area del triangolo.

    def getArea(self) -> float:
        return self.base * self.altezza / 2

# Il metodo render() deve stamapre su schermo un triangolo rettangolo avente i due cateti di lunghezza
#  pari ai valori passati nel costruttore. Il traingolo da stampare deve essere un traingolo vuoto (" "),
#  avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

    def render(self) -> None:
        for i in range(self.altezza):
            slice: str= ""
            if i == 0:
                slice = '*'
            elif i == self.altezza - 1:
                slice = '* ' * self.base
            elif self.base > self.altezza:
                rapporto: float = self.base // self.altezza
                slice = '* ' + '  ' * (i *(self.base // self.altezza) - 1) + '*'
            else:
                rapporto: float = self.altezza // self.base
                slice = '* ' + '  ' * (i *(self.altezza // self.base) - 1) + '*'
            print(slice)

z = Triangolo(10, 6)
z.render()
        
 
# Hint: per il disegno utilizzare print("*", end=" "), dato che l'argomento end = " " permette di controllare
#  come termina ogni chiamata a print, e impostandolo a uno spazio si può fare in modo che tutte le stampe
#  successive siano sulla stessa riga, separate da uno spazio.

# Esempi di output:
# Ecco un Quadrato di lato 4!

# * * * *
# *      *
# *      *
# * * * *
# L'area di questo quadrato vale: 16

# Ecco un Rettangolo avente base 8 ed altezza 4!
# * * * * * * * *
# *                *
# *                *
# * * * * * * * *
# L'area di questo rettangolo vale: 32

# Ecco un Triangolo avente base 4 ed altezza 4!
# *      
# * *    
# *   *  
# * * * *
# L'area di questo triangolo vale: 8.0
