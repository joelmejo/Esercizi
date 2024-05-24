# Sistema di gestione dello zoo virtuale
  
# Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi:
#         name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).

class Animal:
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str, fence = None) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)
        self.fence = fence

    def get_name(self) -> str:
        return self.name

    def get_species(self) -> str:
        return self.species
    
    def get_age(self) -> int:
        return self.age

    def get_height(self) -> float:
        return self.height

    def set_height(self, height: float) -> None:
        self.height = height

    def get_width(self) -> float:
        return self.width

    def set_width(self, width: float) -> None:
        self.width = width

    def get_preferred_habitat(self) -> str:
        return self.preferred_habitat

    def get_health(self) -> float:
        return self.health
    
    def set_health(self, health: float) -> None:
        self.health = health

    def get_fence(self) -> 'Fence':
        return self.fence
    
    def set_fence(self, fence: 'Fence') -> None:
        self.fence = fence

    def __str__(self) -> str:
        return f"Animal(name={self.name}, species={self.species}, age={self.age})"
    
# Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali.
#        I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.

class Fence:
    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        self.area = area
        self.unavailable_area: float = 0
        self.temperature = temperature
        self.habitat = habitat
        self.animals: list[Animal] = []
    
    def get_area(self) -> float:
        return self.area
    
    def get_unavailable_area(self) -> float:
        return self.unavailable_area

    def get_temperature(self) -> float:
        return self.temperature

    def get_habitat(self) -> str:
        return self.habitat
    
    def get_animals(self) -> list:
        return self.animals
    
    def append_animal(self, animal: Animal) -> None:
        self.animals.append(animal)
        self.unavailable_area += (animal.get_height() * animal.get_width())

    def remov_animal(self, animal: Animal) -> None:
        self.animals.remove(animal)
        self.unavailable_area -= (animal.get_height() * animal.get_width())

    def __str__(self) -> str:
        animal_strings = '\n\n'.join([str(animal) for animal in self.animals])
        return f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat}" + "\n\nwith animals:\n\n" + animal_strings

# ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo.
#            I guardiani dello zoo hanno un name, un surname, e un id.

class ZooKeeper:
    def __init__(self, name: str, surname: str, id: int) -> None:
        self.name = name
        self.surname = surname
        self.id = id

# Funzionalità

# 1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo
#   di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato in base
#   alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora
#   sufficiente per ospitare questo animale.

    def add_animal(self, animal: Animal, fence: Fence) -> None:
        if animal.get_preferred_habitat() == fence.get_habitat():
            if animal.get_height() * animal.get_width() < (fence.get_area() - fence.get_unavailable_area()):
                fence.append_animal(animal)
                animal.set_fence(fence)
            else:
                print(f"There isn't enough space to add {animal.get_name()} to this fence.")
        else:
            print(f"The habitat of {animal.get_name()} does not match the habitat of this fence.")


# 2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo
#   di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto.
#   Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

    def remove_animal(self, animal: Animal, fence: Fence) -> None:
        if animal in fence.get_animals():
            fence.remov_animal(animal)
            animal.set_fence(None)
        else:
            print(f"{animal.get_name().capitalize()} couldn't be removed from the fence because it isn't in it.")


# 3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo
#   di nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa
#   di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width)
#   vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio
#   a sufficienza per ospitare l'animale ingrandito dal cibo.

    def feed(self, animal: Animal) -> None:
            fence = animal.get_fence()
            if fence is not None:
                if animal.get_height() * animal.get_width() <= (fence.get_area() - fence.get_unavailable_area()):
                    animal.set_health(animal.get_health() * 1.01)
                    animal.set_height(animal.get_height() * 1.02)
                    animal.set_width(animal.get_width() * 1.02)        
            else:
                print(f"There isn't enough space to feed {animal.get_name()} in this fence.")


# 4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo
#   di pulire tutti i recinti dello zoo. Questo metodo restituisce un valore di tipo float che indica il tempo
#   che il guardiano impiega per pulire il recinto. Il tempo di pulizia è il rapporto dell'area occupata
#   dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

    def clean(self, fence: Fence) -> float:
        if fence.get_area() == fence.get_unavailable_area():
            return fence.get_unavailable_area()
        else:
            return fence.get_unavailable_area() / (fence.get_area() - fence.get_unavailable_area())
        
    def __str__(self) -> str:
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"
    

    
# Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.
class Zoo:
    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper] ) -> None:
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def get_fences(self) -> list[Fence]:
        return self.fences

    def get_zoo_keepers(self) -> list[ZooKeeper]:
        return self.zoo_keepers
    
    def __str__(self) -> str:
        return f"Zoo(fences={self.fences}, zoo_keepers={self.zoo_keepers})"
    
    def describe_zoo(self) -> str:
        for guardian in self.zoo_keepers:
            print(f"Guardians:\n\n{guardian}")
        print("\nFences:\n")
        for fence in self.fences:
            print(fence)
            print("#" * 30)

# Funzionalità:
# 5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo,
#    sui recinti dello zoo che contengono animali. 


# keeper: ZooKeeper = ZooKeeper("Lorenzo", "Maggi", 1234)

# squirrel: Animal = Animal("Scoiattolo", "Blabla", 25, 0.2, 0.3, "Foresta")
# wolf: Animal = Animal("Lupo", "Lupus", 14, 0.6, 1.2, "Foresta")

# fence: Fence = Fence(100, 25, "Foresta")

# fences_list: list[Fence] = [fence]

# zoo1: Zoo = Zoo(fences_list, [keeper])




# # E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto 
# # Fence(area=100, temperature=25, habitat=Continentale) con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...),
# # Animal(name=Lupo, species=Lupus, age=14,...) ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

# # Guardians:

# # ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

# # Fences:

# # Fence(area=100, temperature=25, habitat=Continent)

# # with animals:

# # Animal(name=Scoiattolo, species=Blabla, age=25)

# # Animal(name=Lupo, species=Lupus, age=14)
# # #########################

# # Fra un recinto e l'altro mettete 30 volte il carattere #.

# # Aggiunta di un animale in un recinto con habitat non corrispondente
# zoo1_keeper = zoo1.get_zoo_keepers()[0]  # Otteniamo il guardiano dallo zoo1
# zoo1_keeper.add_animal(wolf, fence)

# # Pulizia di un recinto completamente occupato
# zoo1_keeper.clean(fence)  # Ci aspettiamo che restituisca l'area occupata poiché il recinto è completamente occupato

# # Descrizione dello zoo1
# zoo1.describe_zoo()

# # Creazione di istanze di recinti
# fence1 = Fence(10, 20, "Foresta")
# fence2 = Fence(5, 30, "Deserto")
# fence3 = Fence(20, 25, "Prateria")
# fence4 = Fence(15, 22, "Savana")
# fence5 = Fence(8, 18, "Giungla")

# # Creazione di istanze di animali per ogni recinto
# animals_fence1 = [
#     Animal("Scoiattolo", "Blabla", 25, 0.2, 0.3, "Foresta"),
#     Animal("Orso", "Ursidae", 15, 1.2, 1, "Foresta"),
#     Animal("Tigre", "Panthera tigris", 10, 1.8, 1.5, "Foresta"),
#     Animal("Lupo", "Canis lupus", 8, 0.8, 1.2, "Foresta"),
#     Animal("Volpe", "Vulpes vulpes", 5, 0.5, 0.6, "Foresta")
# ]

# animals_fence2 = [
#     Animal("Scorpione", "Scorpione", 3, 0.05, 0.1, "Deserto"),
#     Animal("Camaleonte", "Chamaeleonidae", 2, 0.1, 0.15, "Deserto"),
#     Animal("Struzzo", "Struthio camelus", 7, 2.2, 1.5, "Deserto"),
#     Animal("Ghepardo", "Acinonyx jubatus", 6, 1.1, 0.8, "Deserto"),
#     Animal("Iena", "Hyaenidae", 9, 0.9, 1.3, "Deserto")
# ]

# animals_fence3 = [
#     Animal("Cavallo", "Equus ferus caballus", 12, 1.6, 1.7, "Prateria"),
#     Animal("Bisonte", "Bison bison", 18, 2, 2.2, "Prateria"),
#     Animal("Coyote", "Canis latrans", 11, 0.7, 1, "Prateria"),
#     Animal("Canguro", "Macropus", 14, 1.2, 1.4, "Prateria"),
#     Animal("Puma", "Puma concolor", 10, 0.9, 1.5, "Prateria")
# ]

# animals_fence4 = [
#     Animal("Giraffa", "Giraffa camelopardalis", 20, 5, 2, "Savana"),
#     Animal("Ippopotamo", "Hippopotamus amphibius", 15, 1.8, 3, "Savana"),
#     Animal("Leone", "Panthera leo", 8, 1.5, 2, "Savana"),
#     Animal("Zebra", "Equus zebra", 13, 1.3, 1.5, "Savana"),
#     Animal("Gnu", "Connochaetes", 11, 1.2, 1.6, "Savana")
# ]

# animals_fence5 = [
#     Animal("Gorilla", "Gorilla", 18, 1.7, 1.5, "Giungla"),
#     Animal("Leopardo", "Panthera pardus", 10, 1, 1.3, "Giungla"),
#     Animal("Scimmia", "Scimmia", 6, 0.5, 0.4, "Giungla"),
#     Animal("Tucano", "Tucanidae", 3, 0.2, 0.3, "Giungla"),
#     Animal("Tigre", "Panthera tigris", 9, 1.6, 1.2, "Giungla")
# ]

# # Creazione dello zoo con i recinti e il guardiano
# zoo = Zoo([fence1, fence2, fence3, fence4, fence5], [ZooKeeper("Lorenzo", "Maggi", 1234)])

# # Aggiunta di animali ai recinti
# for fence, animals in zip([fence1, fence2, fence3, fence4, fence5], [animals_fence1, animals_fence2, animals_fence3, animals_fence4, animals_fence5]):
#     for animal in animals:
#         zoo.get_zoo_keepers()[0].add_animal(animal, fence)

# # Descrizione dello zoo
# zoo.describe_zoo()


# # Creazione di animali
# squirrel = Animal("Scoiattolo", "Blabla", 25, 0.2, 0.3, "Foresta")
# lion = Animal("Leone", "Panthera leo", 8, 1.5, 2, "Savana")

# # Creazione di un recinto
# small_fence = Fence(10, 30, "Foresta")  # Recinto troppo piccolo
# full_fence = Fence(1, 25, "Foresta")  # Recinto completamente occupato

# # Creazione di un guardiano dello zoo
# keeper = ZooKeeper("Lorenzo", "Maggi", 1234)

# # Creazione dello zoo con diversi recinti e un guardiano
# zoo = Zoo([small_fence, full_fence], [keeper])

# # Aggiunta di un animale in un recinto pieno
# keeper.add_animal(squirrel, full_fence)
# keeper.add_animal(lion, small_fence)

# # Rimozione di un animale non presente nel recinto
# keeper.remove_animal(squirrel, small_fence)

# # Alimentazione degli animali in un recinto senza spazio sufficiente
# keeper.add_animal(squirrel, small_fence)
# keeper.feed(squirrel)

# # Descrizione dello zoo
# zoo.describe_zoo()
