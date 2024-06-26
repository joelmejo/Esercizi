# Esercizio 1

# Crea un context manager usando una classe

# Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

# Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

# Esempio di funzionamento:

# Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

# with FileManager('example.txt', 'w') as f:

#     f.write('Hello, world!')

class Filemanager:
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type=None, exc_val=None, exc_tb=None):
        self.file.close()
        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            print(f"Traceback: {exc_tb}")
        

# with Filemanager('./Lezione15/example.txt', 'w') as f:
#     f.write('Hello, world!')

# Esercizio 2

# Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni
#     che si trovano nel with

# with Timer():

#     time.sleep(1)

# time elapsed: 1.00000

# in questo esempio il tempo passato non sarà mai uguale a 1
from time import time, sleep

class Perf:
    def __init__(self) -> None:
        self.t1 = 0
        self.t2 = 0
    
    def __enter__(self):
        self.t1 = time()
            
    def __exit__(self, exc_type=None, exc_val=None, exc_tb=None):
        self.t2 = time()
        print(self.t2-self.t1)

with Perf():
    sleep(5)