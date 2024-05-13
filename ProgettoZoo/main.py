# Sistema di gestione dello zoo virtuale
    
# Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi:
#         name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).

class Animal:
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str, health: float) -> None:
        self._name = name
        self._species = species
        self._age = age
        self._height = height
        self._width = width
        self._preferred_habitat = preferred_habitat
        self._health = round(100 * (1 / age), 3)

    def get_name(self) -> str:
        return self._name

    def get_species(self) -> str:
        return self._species
    
    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        self._height = height

    def get_width(self) -> float:
        return self._width

    def set_width(self, width: float) -> None:
        self._width = width

    def get_preferred_habitat(self) -> str:
        return self._preferred_habitat

    def get_health(self) -> float:
        return self._health
    
# Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali.
#        I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.

class Fence:
    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        self._area = area
        self._temperature = temperature
        self._habitat = habitat
        self._animals: list[Animal] = []
    
    def get_area(self) -> float:
        return self._area
    
    def set_area(self, area: float) -> None:
        self._area = area

    def get_temperature(self) -> float:
        return self._temperature

    def get_habitat(self) -> str:
        return self._habitat
    
    def get_animals(self) -> list:
        return self._animals
    
    def add_animal(self, animal: Animal) -> None:
        self._animals.append(animal)
    
# ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo.
#            I guardiani dello zoo hanno un name, un surname, e un id.

class ZooKeeper:
    def __init__(self, name: str, surname: str, id: int) -> None:
        self._name = name
        self._name = name
        self._id = id

# Funzionalità

# 1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo
#   di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato in base
#   alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora
#   sufficiente per ospitare questo animale.

    def add_animal(animal: Animal, fence: Fence) -> None:
        if animal.get_preferred_habitat == fence.get_habitat:
            if animal.get_height * animal.get_width < fence.get_area:
                fence.add_animal(animal)
                fence.set_area = (fence.get_area - (animal.get_height * animal.get_width))
        else:
            print(f"There isn't enough space to add {animal.get_name} to this fence.")



# 2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo
#   di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto.
#   Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

# 3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo
#   di nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa
#   di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width)
#   vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio
#   a sufficienza per ospitare l'animale ingrandito dal cibo.

# 4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo
#   di pulire tutti i recinti dello zoo. Questo metodo restituisce un valore di tipo float che indica il tempo
#   che il guardiano impiega per pulire il recinto. Il tempo di pulizia è il rapporto dell'area occupata
#   dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.


    
# Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.
class Zoo:
    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper] ) -> None:
        self._fences = fences
        self._zoo_keepers = zoo_keepers

    def get_fences(self) -> list[Fence]:
        return self._fences

    def get_zoo_keepers(self) -> list[ZooKeeper]:
        return self._zoo_keepers

# Funzionalità:
# 5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo,
#    sui recinti dello zoo che contengono animali. 


keeper = ZooKeeper("Lorenzo", "Maggi", 1234)

squirrel = Animal("Scoiattolo", "Blabla", 25, 0.2, 0.3, "Foresta")
wolf = Animal("Lupo", "Lupus", 14, 0.6, 1.2, "Foresta")



fence = Fence(100, 25, "Foresta")

# E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto 
# Fence(area=100, temperature=25, habitat=Continentale) con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...),
# Animal(name=Lupo, species=Lupus, age=14,...) ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

# Guardians:

# ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

# Fences:

# Fence(area=100, temperature=25, habitat=Continent)

# with animals:

# Animal(name=Scoiattolo, species=Blabla, age=25)

# Animal(name=Lupo, species=Lupus, age=14)
# #########################

# Fra un recinto e l'altro mettete 30 volte il carattere #.