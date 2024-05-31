# Simulazione: la tartaruga e la lepre
# In questo problema ricreerete la classica gara tra la tartaruga e la lepre.
# Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento.
# I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati.
# Ogni quadrato rappresenta una posizione lungo il percorso della corsa. Il traguardo è al quadrato 70
# e il contendente che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa,
# i contendenti possono occasionalmente perdere terreno. C'è un orologio che conta i secondi.
# Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:
from random import randint


# 1. Variabilità Ambientale:
# Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
# Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti. Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.
 
# Modificatori mossa:
# - La Tartaruga in caso di pioggia subisce penalità mossa -1. In caso di sole non subisce variazioni.
# - La Lepre in caso di pioggia subisca una penalità mossa di -2. In caso di sole non subisce variazioni.

def weather_conditions() -> str:
    variable: int = randint(0, 1)
    if variable == 0:
        return "Sunny"
    else:
        return "Rainy"

# Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i,
# nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5,
# una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10.
# Usate una tecnica simile per muovere la lepre seguendo le sue regole.

# Nuove regole di movimento:
#  Lepre:
#     - Riposo (20% di probabilità): non si muove e recupera 10 di energia.
#            Non può superare l'energiza iniziale.
#     - Grande balzo (20% di probabilità): avanza di 9 quadrati  e richiede 15 di energia.
#     - Grande scivolata (10% di probabilità): arretra di 12 quadrati e richiede 20 di energia.
#            Non può andare sotto il quadrato 1.
#     - Piccolo balzo (30% di probabilità): avanza di 1 quadrato e richiede 5 di energia.
#     - Piccola scivolata (20% di probabilità): arretra di 2 quadrati e richiede 8 di energia.
#            Non può andare sotto il quadrato 1.

def hare_move(weather: str, stamina: int) -> int:
    move = randint(1, 10)
    MAX_STAMINA: int = 100
    if weather == "Rainy":
        # Riposo
        if move <= 2:
            stamina += 10
            stamina = min(MAX_STAMINA, stamina)
            return 0, stamina
        # Grande balzo
        elif move <= 4:
            if stamina >= 15:
                stamina -= 15
                return 7, stamina
            else:
                return 0, stamina
        # Grande scivolata
        elif move <= 5:
            if stamina >= 20:
                stamina -= 20
                return -14, stamina
            else:
                return 0, stamina
        # Piccolo balzo
        elif move <= 8:
            if stamina >= 5:
                stamina -= 5
                return -1, stamina
            else:
                return 0, stamina
        # Piccola scivolata
        else:
            if stamina >= 8:
                stamina -= 8
                return -4, stamina
            else:
                return 0, stamina
    else:
        # Riposo
        if move <= 2:
            stamina += 10
            stamina = min(MAX_STAMINA, stamina)
            return 0, stamina
        # Grande balzo
        elif move <= 4:
            if stamina >= 15:
                stamina -= 15
                return 9, stamina
            else:
                return 0, stamina
        # Grande scivolata
        elif move <= 5:
            if stamina >= 20:
                stamina -= 20
                return -12, stamina
            else:
                return 0, stamina
        # Piccolo balzo
        elif move <= 8:
            if stamina >= 5:
                stamina -= 5
                return 1, stamina
            else:
                return 0, stamina
        # Piccola scivolata
        else:
            if stamina >= 8:
                stamina -= 8
                return -2, stamina
            else:
                return 0, stamina
        
# Tartaruga:
#     - Per la tartaruga, ogni volta che il numero generato indica una mossa ma non è possibile eseguirla per mancanza di energia, essa guadagna 10 di energia.
#     - Passo veloce (50% di probabilità): avanza di 3 quadrati e richiede 5 di energia.
#     - Scivolata (20% di probabilità): arretra di 6 quadrati e richiede 10 di energia. Non può andare sotto il quadrato 1.
#     - Passo lento (30% di probabilità): avanza di 1 quadrato e richiede 3 di energia.

def tortoise_move(weather: str, stamina: int) -> int:
    move = randint(1, 10)
    if weather == "Rainy":
        # Passo veloce
        if move <= 5:
            if stamina >= 5:
                stamina -= 5
                return 2, stamina
            else:
                stamina += 10
                return 0, stamina
        # Scivolata
        elif move <= 7:
            if stamina >= 10:
                stamina -= 10
                return -7, stamina
            else:
                stamina += 10
                return 0, stamina
        # Passo lento
        else:
            if stamina >= 3:
                stamina -= 3
                return 0, stamina
            else:
                stamina += 10
                return 0, stamina
    else:
        # Passo veloce
        if move <= 5:
            if stamina >= 5:
                stamina -= 5
                return 3, stamina
            else:
                stamina += 10
                return 0, stamina
        # Scivolata
        elif move <= 7:
            if stamina >= 10:
                stamina -= 10
                return -6, stamina
            else:
                stamina += 10
                return 0, stamina
        # Passo lento
        else:
            if stamina >= 3:
                stamina -= 3
                return 1, stamina
            else:
                stamina += 10
                return 0, stamina
      

# - Ostacoli:
# Posizionati a intervalli regolari sulla pista (es. ai quadrati 15, 30, 45), gli ostacoli riducono
# la posizione dell'animale di un numero specificato di quadrati (es: -3, -5, -7). Gli ostacoli
# sono rappresentati da un dizionario che mappa le posizioni degli ostacoli sul percorso (chiave)
# ed i relaviti effetti (valore). Assicurarsi che nessun animale retroceda al di sotto del primo
# quadrato a seguito di un ostacolo.

# - Bonus:
# Dislocati strategicamente lungo la corsa (es. ai quadrati 10, 25, 50), i bonus aumentano la posizione
# dell'animale di un numero determinato di quadrati (es: 5, 3, 10). I bonus sono rappresentati da un dizionario
# che mappa le posizioni dei bonus sul percorso (chiave) ed i relaviti effetti (valore).
# Consentire agli animali di beneficiare pienamente dei bonus, ma non oltrepassare il traguardo.

obstacles: dict = {15: -3, 30: -5, 45: -7}
bonus: dict = {10: 5, 25: 3, 50: 10}


def race() -> None:
    MAX_STAMINA: int = 100
    hare: int = 0
    hare_stamina: int = MAX_STAMINA
    tortoise: int = 0
    tortoise_stamina: int = MAX_STAMINA
    counter: int = 0
    PATH_LEN: int = 69
    print("BANG !!!!!\nAND THEY'RE OFF !!!!!")
    while tortoise < PATH_LEN and hare < PATH_LEN:
        
        race_path: list = ['_'] * (PATH_LEN + 1)

        if counter % 10 == 0:
            weather: str = weather_conditions()
            print(f"The weather is {weather}")


        move, hare_stamina = hare_move(weather, hare_stamina)
        
        if hare + move in obstacles:
            move += obstacles[hare + move]
            print("Hare hit an obstacle")

        elif hare + move in bonus:
            move += bonus[hare + move]
            print("Hare hit a bonus")
        hare = max(0, hare + move)
        hare = min(PATH_LEN, hare)

        move, tortoise_stamina = tortoise_move(weather, tortoise_stamina)

        if tortoise + move in obstacles:
            move += obstacles[tortoise + move]
            print("Tortoise hit an obstacle")
        elif tortoise + move in bonus:
            move += bonus[tortoise + move]
            print("Tortoise hit a bonus")

        tortoise = max(0, tortoise + move)
        tortoise = min(PATH_LEN, tortoise)

        if tortoise == hare:
            race_path[tortoise] = 'OUCH!!!'
        else:
            race_path[tortoise] = 'T'
            race_path[hare] = 'H'

        print(''.join(race_path))
        counter += 1
    
    print(counter)

    if tortoise == hare:
        print("IT'S A TIE.")
    elif tortoise == PATH_LEN:
        print("TORTOISE WINS! || VAY!!!")
    else:
        print("HARE WINS || YUCH!!!")

race()

# Requisiti del Codice:
# - Utilizzare il modulo random per la generazione dei numeri casuali.
# - Definire e utilizzare:
#     - una funzione per visualizzare le posizioni sulla corsia di gara,
#     - una funzione per calcolare la mossa della tartaruga,
#     - una funzione per calcolare la mossa della lepre.
# - Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse,
# mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.
