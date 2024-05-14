# Simulazione: la tartaruga e la lepre
# In questo problema ricreerete la classica gara tra la tartaruga e la lepre.
# Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento.
# I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati.
# Ogni quadrato rappresenta una posizione lungo il percorso della corsa. Il traguardo è al quadrato 70
# e il contendente che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa,
# i contendenti possono occasionalmente perdere terreno. C'è un orologio che conta i secondi.
# Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:
import random


# Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i,
# nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5,
# una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10.
# Usate una tecnica simile per muovere la lepre seguendo le sue regole.

# - Lepre:
#     - Riposo (20% di probabilità): non si muove.
#     - Grande balzo (20% di probabilità): avanza di 9 quadrati.
#     - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
#     -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
#     - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

def hare_move() -> int:
    move = random.randint(1, 10)
    if move <= 2:
        return 0
    elif move <= 4:
        return 9
    elif move <= 5:
        return -12
    elif move <= 8:
        return 1
    else:
        return -2
    
# - Tartaruga:
#     - Passo veloce (50% di probabilità): avanza di 3 quadrati.
#     - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
#     - Passo lento (30% di probabilità): avanza di 1 quadrato.

def tortoise_move() -> int:
    move = random.randint(1, 10)
    if move <= 5:
        return 3
    elif move <= 7:
        return -6
    else:
        return 1

# Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni
# degli animali (i numeri delle posizioni sono da 1 a 70). Fate partire ogni animale dalla
# posizione 1 (cioè ai "cancelli di partenza"). Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.



# Iniziate la gara stampando:
# 'BANG !!!!! AND THEY'RE OFF !!!!!'

def race() -> None:
    hare: int = 0
    tortoise: int = 0
    counter: int = 0
    path: list = ['-'] * 70
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while tortoise < 69 and hare < 69:
        race_path: list = path.copy()
        move: int = hare_move()
        
        if (hare + move) < 1:
            hare = 1
        else:
            hare += move
        move = tortoise_move()

        if (tortoise + move) < 1:
            tortoise = 1
        else:
            tortoise += move
        
        if hare > 69:
            hare = 69
        
        if tortoise > 69:
            tortoise = 69

        
        race_path[hare] = 'H'
        
        if race_path[tortoise] == 'H':
            race_path[tortoise] = 'OUCH!!!'
        else:
            race_path[tortoise] = 'T'
        print(''.join(race_path))
        counter += 1
    
    print(counter)

    if tortoise == hare:
        print("IT'S A TIE.")
    elif tortoise == 69:
        print("TORTOISE WINS! || VAY!!!")
    else:
        print("HARE WINS || YUCH!!!")

race()   


# Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo),
# stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga,
# la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere.
# Occasionalmente, i contendenti si troveranno sullo stesso quadrato.
# In questo caso la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!'
# iniziando da quella posizione. Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!'
# (in caso della stessa posizione) devono essere il carattere '_'.

# Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70.
# Se è così, stampate il nome del vincitore e terminate la simulazione.
# Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". Se vince la lepre, stampate "HARE WINS || YUCH!!!".
# Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga 
# (la "sfavorita"), oppure stampare "IT'S A TIE.". Se non vince nessun animale,
# eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

# Requisiti del Codice:
# - Utilizzare il modulo random per la generazione dei numeri casuali.
# - Definire e utilizzare:
#     - una funzione per visualizzare le posizioni sulla corsia di gara,
#     - una funzione per calcolare la mossa della tartaruga,
#     - una funzione per calcolare la mossa della lepre.
# - Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse,
# mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.
