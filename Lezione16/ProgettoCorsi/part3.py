#### Classe Course:
# La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
# - Metodi:
#     - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il
#            limite di studenti.
#     - get_groups(): Restituisce la lista dei gruppi nel corso.
#     - add_group(group): Aggiunge un gruppo al corso.

# # Copia qui di seguito il codice di Realizzazione e Gestione Corsi ITS - Parte 1 

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

# Copia qui di seguito il codice di Realizzazione e Gestione Corsi ITS - Parte 2

class Person:
    def __init__(self, cf: str, name: str, surname: str, age: int) -> None:
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int) -> None:
        super().__init__(cf, name, surname, age)
        self.group: 'Group' = None

    def set_group(self, group: str) -> None:
        self.group = group
    
class Lecturer(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int) -> None:
        super().__init__(cf, name, surname, age)

class Group:
    def __init__(self, name: str, limit: int) -> None:
        self.name = name
        self.limit = limit
        self.students: list[Student] = []
        self.lecturers: list[Lecturer] = []

    def get_name(self) -> str:
        return self.name
    
    def get_limit(self) -> int:
        return self.limit
    
    def get_students(self) -> list[Student]:
        return self.students
    
    def get_limit_lecturers(self) -> int:
        return max((len(self.students) - 1) // 10, 1)
    
    def add_student(self, student: Student) -> None:
        if len(self.students) < self.limit:
            self.students.append(student)

    def add_lecturer(self, lecturer: Lecturer) -> None:
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)

# Definisci qui di seguito la classe Course

class Course:
    def __init__(self, name: str, groups: list[Group]= []) -> None:
        self.name = name
        self.groups = groups

    def register(self, student: Student) -> None:
        for group in self.groups:
            if len(group.get_students()) < group.limit:
                group.add_student(student)
                break
    
    def get_groups(self) -> list[Group]:
        return self.groups
    
    def add_group(self, group: Group) -> None:
        self.groups.append(group)