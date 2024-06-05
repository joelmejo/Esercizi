# In questo progetto, dovrai scrivere il codice per un sistema di gestione e creazione dei corsi ITS.
# Il sistema gestisce aule ed edifici (Parte 1), persone -studenti e docenti- in gruppi di studio (parte 2),
# e corsi (parte 3).
 
# ### Classe Room:
# La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), un numero di posti (seats)
#    e un'area (area). L'area è calcolata come il doppio dei posti.
# - Metodi:
#     - get_id(): Restituisce l'ID dell'aula.
#     - get_floor(): Restituisce il piano dell'aula.
#     - get_seats(): Restituisce il numero di posti dell'aula.
#     - get_area(): Restituisce l'area dell'aula.

# ### Classe Building:
# La classe Building rappresenta un edificio. Ogni edificio ha un nome (name), un indirizzo (address),
#    un intervallo di piani (floors), e una lista di aule (rooms).
# - Metodi:
#     - get_floors(): Restituisce l'intervallo di piani dell'edificio.
#     - get_rooms(): Restituisce la lista delle aule nell'edificio.
#     - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso nell'intervallo
#            di piani dell'edificio.
#     - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule.

class Room:
    def __init__(self, id: str, floor: int, seats: int) -> None:
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats * 2

    def get_id(self) -> str:
        return self.id
    
    def get_floor(self) -> int:
        return self.floor
    
    def get_seats(self) -> int:
        return self.seats
    
    def get_area(self) -> float:
        return self.area
    

class Building:
    def __init__(self, name: str, address: str, floors: tuple) -> None:
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms: list[Room] = []

    def get_floors(self) -> list[int]:
        return self.floors
    
    def get_rooms(self) -> list[Room]:
        return self.rooms
    
    def add_room(self, room: Room) -> None:
        if room not in self.rooms:
            if self.floors[0] <= room.get_floor() <= self.floors[1]:
                self.rooms.append(room)

    def area(self) -> float:
        total_area: float = 0
        for room in self.rooms:
            total_area += room.get_area()
        return total_area