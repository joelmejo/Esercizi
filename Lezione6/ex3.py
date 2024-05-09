# Exercise 3 (Folder 9 ex_3.py)
# Given is the class Animal. For each task, test your changes!
# 1. Create two realistic instances of Animals
# 2. Print the name of each object
# 3. Change the amount of legs of one object using the dot notation
# 4. Add a method setLegs() to set the legs of an object and repeat task 3 but
# this time using the method.
# 5. Add a method getLegs() to return the amount of legs
# 6. Add a method named printInfo that prints all attributes of the Animal

class Animal:
    def __init__(self, name: str, legs: int) -> None:
        self._name = name
        self._legs = legs
    
    def get_name(self) -> str:
        return self._name
    
    def set_name(self) -> None:
        raise Exception("You cannot change the name!")
    
    def get_legs(self) -> str:
        return self._legs
    
    def set_legs(self, legs) -> None:
        self._legs = legs
    
    def __str__(self) -> str:
        return f"{self._name} has {self._legs} legs."


cat: Animal = Animal('Cat', 4)
bird: Animal = Animal('Bird', 2)

cat._legs = 3
print(cat.get_name())
print(cat.get_legs())

cat.set_legs(2)
print(bird.get_name())
print(bird.get_legs())

print(cat)
print(bird)


