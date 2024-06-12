# Exercise 2
# 1. Write a class called Student with the attributes name (str) and
# studyProgram (str)
# 2. Create three instances. One for yourself, one for your left neighbour and one
# for our right neighbour.
# 3. Add a method printInfo that prints the name and studyProgram of a
# Student. Test your method on the objects!
# 4. Modify the code and add age and gender to the attributes. Modify your
# printing methods respectively too.

class Student:
    def __init__(self, name: str, age: int, gender: str, study_program: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.study_program = study_program
    
    def __str__(self) -> str:
        return f"{self.name}, {self.age}, {self.gender}, {self.study_program}"

mario: Student = Student('Mario', 20, 'Male', 'Cyber')
luigi: Student = Student('Luigi', 21, 'Male', 'Cloud')
rose: Student = Student('Rose', 18, 'Female', 'Full Stack')

print(mario)
print(luigi)
print(rose)
