# Exercise 1
# 1. Copy the code and print the age of
# bob (using the dot notation)
# 2. Create an if-statement that prints
# the name of the oldest of the two
# Persons
# 3. Create three other Persons. Make
# a list called people with all 5
# Persons.
# 4. Make a loop that finds and prints
# the youngest person’s name

class Person1:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
alice = Person1("Alice W.", 45)
bob = Person1("Bob M.", 36)

print(bob.age)

if alice.age > bob.age:
    print(alice.name)
else:
    print(bob.name)

john: Person1 = Person1("John B.", 30)
mary: Person1 = Person1("Mary C.", 20)
michael: Person1 = Person1("Michael D.", 25)

people: list = [alice, bob, john, mary, michael]
youngest: str = ""
youngest_age: int = 200
for person in people:
    if person.age < youngest_age:
        youngest_age = person.age
        youngest = person.name

print(youngest)