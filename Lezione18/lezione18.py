# 1 Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using
#    math.sqrt(). Handle ValueError if the input is negative by returning an informative message.

def safe_sqrt(n: int) -> int:
    from math import sqrt
    try:
        square = sqrt(n)
    except:
        print("Impossibile eseguire la radice quadrata di un numero negativo")
# safe_sqrt(-2)


# 2 Password Validation: Write a function validate_password(password) that checks if a password meets certain
#    criteria (i.e., minimum length of 20 characters, at least three uppercase characters, and at least four
#    special characters).  Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.

def validate_password(psw: str):
    class InvalidPasswordError(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)

        def __str__(self):
            return f'{self.__class__.__name__}: {self.message}'
        
    try:
        if len(psw) < 20:
            raise InvalidPasswordError("The password must be at least 20 characters long")
        
        count: int= 0
        uppercase_letters: list= list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        for i in list(psw):
            if i in uppercase_letters:
                count += 1
        if count < 3:
            raise InvalidPasswordError("the password must contain at least 3 uppercase characters")
        
        special_characters = list('!@#$%^&*()-_=+[]{}|;:,.<>/?`~')
        for i in list(psw):
            if i in special_characters:
                count += 1
        if count < 4:
            raise InvalidPasswordError("the password must contain at least 4 special characters")
        
    except InvalidPasswordError as e:
        print(e)
# validate_password('avgahngnannfsthwnsswmwtaAAA%%%%ngnwr')


# 3 Context Managers for File Handling: Use the with statement and context managers to open and close a file.
#    Handle potential IOError within the with block for clean resource management.

def context_manager():
    try:
        with open('file_non_esistente.txt', 'r') as file:
            print(file.read())
    except IOError:
        print("An IOError occurred")
# context_manager()


# 4 Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing
#    methods to add a new date, delete a given date, modify a date, and perform a query on a given date is required.
#    A query on a given date allows for retrieving a given new date. Note that a date is an object for your
#    database; it must be instantiated from a string.
from datetime import date
class Dates:
    def __init__(self) -> None:
        self.dates: list[date] = []

    def add_new_date(self, data: str) -> None:
        day, month, year = map(int, data.split('-'))
        date1 = date(year, month, day)
        self.dates.append(date1)
    
    def remove_date(self, data: str) -> None:
        data: list[int]= map(int, data.split('-'))
        for d in self.dates:
            if d.year == data[2]:
                if d.month == data[1]:
                    if d.day == data[0]:
                        self.dates.remove(d)
    
    def modify_date(self, old_date: str, new_date: str) -> None:
        old_date: list[int]= map(int, old_date.split('-'))
        for d in self.dates:
            if d.year == old_date[2]:
                if d.month == old_date[1]:
                    if d.day == old_date[0]:
                        day, month, year = map(int, new_date.split('-'))
                        d = date(year, month, day)

    # def getDate(self) -> date:
        



# 5 An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases
#    using UnitTest trying to (possibly) cover all execution paths! User input is assumed to be a formula that
#    consists of a number, an operator (at least + and -), and another number, separated by white space
#    (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:

#      If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
#     Try to convert the first and third inputs to a float (like so: float_value = float(str_value)).
#        Catch any ValueError that occurs, and instead raise a FormulaError.
#     If the second input is not '+' or '-', again raise a FormulaError.
#     If the input is valid, perform the calculation and print out the result. The user is then prompted to
#        provide new input, and so on, until the user enters quit.

def interactive_calculator() -> float:
    class FormulaError(Exception):
        def __init__(self, message: str) -> None:
            self.message = message
            super().__init__(self.message)
        
        def __str__(self):
            return f"{self.__class__.__name__}: {self.message}"
    print("Enter your operation: ")

    raises: int= 0
    while raises < 5:
        formula: str = input()
        listed_formula: list= formula.split()
        try:
            if len(listed_formula) != 3:
                raise FormulaError("Please input two numbers and an operand(+ or -)")
            else:    
                n1: float = float(listed_formula[0])
                n2: float = float(listed_formula[2])
                operand: str = listed_formula[1]
                if operand == '+':
                    return n1 + n2
                elif operand == '-':
                    return n1 - n2
                else:
                    raise FormulaError("Please input a valid operand")
        except ValueError as e:
            raises += 1
            print(FormulaError("Please input two valid numbers"))
        
        except FormulaError as e:
            raises += 1
            print(e)

print(interactive_calculator())

# 6 Personalized math library: Create a Python library that provides functions for handling fractions,
#        with built-in error handling. The library must include functions for the following operations:
#     Create a fraction from the numerator and denominator.
#     Collect the numerator and denominator of a fraction.
#     Simplify a fraction.
#     Add, subtract, multiply and divide fractions.
#     Check whether one fraction is equivalent to another. 

#     All library functions must use the try-except block to handle potential errors, such as null denominators,
#        unsupported operations, or division by zero. The library must raise custom exceptions to indicate specific
#        errors to the user.

# 7 Custom Exception for Data Structure Integrity: Define a custom exception class DataStructureIntegrityError.
#     Define the custom data structure linked list use classes with methods to append, remove and access a given
#     element, and write functions that operate on that (i.e., print the list,  reverse the list, and check whether
#     the list is ordered). Raise this exception if the data structure's integrity is compromised (e.g., empty list
#     access, index error).