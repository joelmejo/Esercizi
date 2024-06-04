# 2
# Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
# - se x è pari, deve essere diviso per 2;
# - se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.

def transform(x: int) -> int:
    # cancella pass e scrivi il tuo codice
    if x%2 == 0:
        x //= 2
    else:
        x *= 3
        x -= 1
    return x

print(transform(4)) # 2

print(transform(3)) # 8

print(transform(0)) # 0

print(transform(-10)) # -5

print(transform(-5)) # -16


# 3
# Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. L'azienda paga 10 dollari
#    all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
# Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
# La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.

def calcola_stipendio(ore_lavorate: int) -> float:
    # cancella pass e scrivi il tuo codice
    paga_oraria = 10
    if ore_lavorate <= 40:
        stipendio = ore_lavorate * paga_oraria
    else:
        ore_straordinario = ore_lavorate - 40
        stipendio = (ore_lavorate - ore_straordinario) * paga_oraria
        paga_straordinari = ore_straordinario * (paga_oraria * 1.50)
        stipendio += paga_straordinari
    return stipendio

print(calcola_stipendio(40)) # 400.0

print(calcola_stipendio(30)) # 300.0

print(calcola_stipendio(45)) # 475.0

print(calcola_stipendio(60)) # 700.0

print(calcola_stipendio(0)) # 0.0


# 4
# Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
# a) 1, 2, 3, 4, 5, 6, 7
# b) 3, 8, 13, 18, 23
# c) 20, 14, 8, 2, -4, -10
# d) 19, 27, 35, 43, 51

def print_seq(): 
    
    print("Sequenza a):")
    # SCRIVI QUI IL TUO CICLO
    for i in range(1,8):
        print(i)
    print()

    print("Sequenza b):")
    # SCRIVI QUI IL TUO CICLO
    for i in range(3,24,5):
        print(i)
    print()

    print("Sequenza c):")
    # SCRIVI QUI IL TUO CICLO
    for i in reversed(range(-10,21,6)):
        print(i)
    print()
    print("Sequenza d):")
    # SCRIVI QUI IL TUO CICLO
    for i in range(19,52,8):
        print(i)
    print()
    return

print_seq()
#  EXPECTED
# Sequenza a):
# 1
# 2
# 3
# 4
# 5
# 6
# 7

# Sequenza b):
# 3
# 8
# 13
# 18
# 23

# Sequenza c):
# 20
# 14
# 8
# 2
# -4
# -10

# Sequenza d):
# 19
# 27
# 35
# 43
# 51


# 5
# Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, restituisca il risultato della potenza base^exponent.
#    Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.
 
# La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
# Non utilizzare nessuna funzione della libreria math!

def integerPower(base, esponente):
    result = base
    for i in range(esponente + 1):
        if i <= 1:
            continue
        result *= base
    return result

print(integerPower(3, 4)) # 81

print(integerPower(5, 3)) # 125

print(integerPower(2, 5)) # 32

print(integerPower(10, 2)) # 100

# 6
# Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. La funzione
#    deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.


# Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.

def hypotenuse(lato1, lato2):
    return ((lato1**2)+(lato2**2))** 0.5

print(hypotenuse(3.0, 4.0)) # 5.0

print(hypotenuse(5.0, 12.0)) # 13.0

print(hypotenuse(8.0, 15.0)) # 17.0

print(hypotenuse(7.0, 24.0)) # 25.0

# 7
# Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    # cancella pass e scrivi il tuo codice
    dict3: dict = {}
    for key in dict1.keys():
        if key in dict3:
            dict3[key] +=dict1[key]
        else:
            dict3[key] = dict1[key]
    for key in dict2.keys():
        if key in dict3:
            dict3[key] += dict2[key]
        else:
            dict3[key] = dict2[key]
    return dict3

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})) # {'a': 1, 'b': 5, 'c': 4}

print(merge_dictionaries({}, {'a': 10, 'b': 20})) # {'a': 10, 'b': 20}

print(merge_dictionaries({'x': 5}, {'x': -5})) # {'x': 0}

print(merge_dictionaries({}, {})) # {}

print(merge_dictionaries({'a': 3}, {'b': 4})) # {'a': 3, 'b': 4}

# 8
# Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi (ore, minuti e secondi)
#   e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta (le ore 12, dunque,
#        vengono considerate come orario di partenza, dunque, come uno zero).

# Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono passati 11750 secondi da quando
#   l'orologio ha "battuto le 12" per l'ultima volta.

# Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, entrambi espressi mediante ore, minuti e secondi.
#    La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari,
#    entrambi contenuti entro un ciclo dell'orologio di 12 ore.

# Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.

def seconds_since_noon(ore: int, minuti: int, secondi: int):
    minuti += (ore * 60)
    secondi += (minuti * 60)
    return secondi
    
def time_difference(ore1, minuti1, secondi1, ore2, minuti2, secondi2):
    distanza1: int = seconds_since_noon(ore1, minuti1, secondi1)
    distanza2: int = seconds_since_noon(ore2, minuti2, secondi2)
    if distanza1 >= distanza2:
        differenza = distanza1 - distanza2
    else:
        differenza = distanza2 - distanza1
    return differenza

print(time_difference(1, 0, 0, 3, 15, 30)) # 8130

print(time_difference(11, 59, 59, 2, 0, 0)) # 35999

print(time_difference(0, 0, 0, 12, 0, 0)) # 43200

print(time_difference(9, 0, 0, 11, 0, 0)) # 7200


# 9

# Si scriva una funzione in Python che simuli una palla che rimbalza calcolando la sua altezza da terra
#    in centimetri per ogni secondo, a mano a mano che il tempo passa su un orologio simulato.

# Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.

# Dopo ogni secondo, il valore dell'altezza cambia, aggiungendo al valore corrente dell'altezza il valore
#    della velocità corrente; poi, il valore della velocità viene modificato, sottraendo 96 al valore della velocità corrente.
# Dunque, dopo ogni secondo, si ha che
# altezza = altezza + velocità
# velocità = velocità - 96.
 
# Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, si deve moltiplicare altezza e velocità per -0.5
#    per simulare il rimbalzo. Dunque, per il rimbalzo, si avrà che
# altezza= altezza*-0,5 
# velocità=velocità*-0,5.

# Ci si fermi al quinto rimbalzo.
 
# Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a cui si trova la palla in quel determinato secondo.
# Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
 
# "Tempo: 0 Altezza: 0"
 
# Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
# Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
 
# "Tempo: 4 Rimbalzo!"

def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0

    
    # cancella pass e scrivi il tuo codice
  
    while rimbalzi < 5:
        print(f"Tempo: {tempo} Altezza: {altezza}")
        altezza += velocita
        velocita = velocita - 96
        if altezza < 0:
            altezza *= -0.5 
            velocita *= -0.5
            rimbalzi += 1
            tempo += 1
            print(f"Tempo: {tempo} Rimbalzo!")
        tempo += 1

rimbalzo()
# EXPECTED
# Tempo: 0 Altezza: 0.0
# Tempo: 1 Altezza: 100.0
# Tempo: 2 Altezza: 104.0
# Tempo: 3 Altezza: 12.0
# Tempo: 4 Rimbalzo!
# Tempo: 5 Altezza: 88.0
# Tempo: 6 Altezza: 230.0
# Tempo: 7 Altezza: 276.0
# Tempo: 8 Altezza: 226.0
# Tempo: 9 Altezza: 80.0
# Tempo: 10 Rimbalzo!
# Tempo: 11 Altezza: 81.0
# Tempo: 12 Altezza: 250.0
# Tempo: 13 Altezza: 323.0
# Tempo: 14 Altezza: 300.0
# Tempo: 15 Altezza: 181.0
# Tempo: 16 Rimbalzo!
# Tempo: 17 Altezza: 17.0
# Tempo: 18 Altezza: 172.5
# Tempo: 19 Altezza: 232.0
# Tempo: 20 Altezza: 195.5
# Tempo: 21 Altezza: 63.0
# Tempo: 22 Rimbalzo!
# Tempo: 23 Altezza: 82.75
# Tempo: 24 Altezza: 245.0
# Tempo: 25 Altezza: 311.25
# Tempo: 26 Altezza: 281.5
# Tempo: 27 Altezza: 155.75
# Tempo: 28 Rimbalzo!


# 10
# Si immagini una funzione che comprime i file all'80% e li salva su un supporto di memorizzazione.
# Prima che il file compresso venga memorizzato, deve essere diviso in blocchi da 512 byte ciascuno.
 
# Si sviluppi in Python un algoritmo per questa funzione che prende in input una lista di valori interi,
# dove ogni valore intero della lista rappresenta la dimensione non compressa di un singolo file espressa in byte.
 
# Tale funzione deve utilizzare un ciclo per iterare la lista e, per ogni dimensione non compressa,
# deve calcolare la dimensione compressa di tale file espressa come float (ovvero deve calcolare l' 80% della dimensione non compressa),
# calcolare il numero di blocchi (arrotondato al numero intero più vicino) da 512 byte necessari per la memorizzazione,
# al fine di determinare se il file compresso può essere salvato nello spazio rimanente nel supporto di memorizzazione o meno.
 
# In caso affermativo, il programma memorizza il file. In tal caso, la funzione deve stampare la dimensione originale del file,
# la dimensione compressa, i blocchi utilizzati per memorizzare il file in questione e i blocchi disponibili rimasti sul supporto di memorizzazione. 
# Ad esempio, se è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1100 byte, la funzione stamperà:
 
# "File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998."
 
# Il ciclo continua finché non viene riscontrato un file della lista la cui dimensione compressa occupa
# un numero di blocchi più grande di quelli rimasti disponibili sul supporto di memorizzazione. In tal caso,
# la funzione deve avvisare l'utente che lo spazio disponibile sul supporto di memorizzazione non è sufficiente per salvare il file. 
# Ad esempio, se non è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1048576 byte, la funzione stamperà:
 
# "Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente."

# Inizialmente, il numero totale di blocchi disponibili sul supporto di memorizzazione per il salvataggio dei file è un numero intero pari a 1000 blocchi. 

def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000  # Spazio totale disponibile in blocchi
    
    # Inserisci qui il tuo codice
    for file in files:
        file_compresso= file * 0.8
        blocchi = file_compresso / 512
        blocchi = round(blocchi)
        if spazio_totale_blocchi > blocchi:
            spazio_totale_blocchi -= blocchi
            print(f"File di {file} byte compresso in {file_compresso} byte e memorizzato. Blocchi usati: {blocchi}. Blocchi rimanenti: {spazio_totale_blocchi}.")
        else:
            print(f"Non è possibile memorizzare il file di {file} byte. Spazio insufficiente.")
            break

memorizza_file([1100, 20000, 1048576, 512, 5000])
# EXPECTED
# File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998.
# File di 20000 byte compresso in 16000.0 byte e memorizzato. Blocchi usati: 31. Blocchi rimanenti: 967.
# Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente.

memorizza_file([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
# EXPECTED
# File di 100 byte compresso in 80.0 byte e memorizzato. Blocchi usati: 0. Blocchi rimanenti: 1000.
# File di 200 byte compresso in 160.0 byte e memorizzato. Blocchi usati: 0. Blocchi rimanenti: 1000.
# File di 300 byte compresso in 240.0 byte e memorizzato. Blocchi usati: 0. Blocchi rimanenti: 1000.
# File di 400 byte compresso in 320.0 byte e memorizzato. Blocchi usati: 1. Blocchi rimanenti: 999.
# File di 500 byte compresso in 400.0 byte e memorizzato. Blocchi usati: 1. Blocchi rimanenti: 998.
# File di 600 byte compresso in 480.0 byte e memorizzato. Blocchi usati: 1. Blocchi rimanenti: 997.
# File di 700 byte compresso in 560.0 byte e memorizzato. Blocchi usati: 1. Blocchi rimanenti: 996.
# File di 800 byte compresso in 640.0 byte e memorizzato. Blocchi usati: 1. Blocchi rimanenti: 995.
# File di 900 byte compresso in 720.0 byte e memorizzato. Blocchi usati: 1. Blocchi rimanenti: 994.
# File di 1000 byte compresso in 800.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 992.