# Exercise 1: Creating an Abstract Class with Abstract Methods

# Create an abstract class Shape with an abstract method area and another abstract method perimeter.
# Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape): 
    def __init__(self, radius: int) -> None:
        self.radius = radius

    # ovveriding abstract method
    def perimeter(self) -> float:
        return 2 * pi * self.radius
    
    # overriding abstract method
    def area(self) -> float:
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, short: float, long: float) -> None:
        self.short = short
        self.long = long

    # overriding abstract method
    def perimeter(self) -> float:
        return (self.short * 2) + (self.long * 2)
    
    # overriding abstract method
    def area(self) -> float:
        return self.short * self.long
        

# Exercise 2: Implementing Static Methods

# Create a class MathOperations with a static method add that takes two numbers and returns their sum,
#    and another static method multiply that takes two numbers and returns their product.

class MathOperations:

    @staticmethod
    def sum(num1: float, num2: float) -> float:
        return num1 + num2
    
    @staticmethod
    def multiply(num1: float, num2: float) -> float:
        return num1 * num2


# Exercise 3: Library Management System 

# Create a Book class containing the following attributes: title, author, isbn
# The book class must contains the following methods:

#     __str__ method to return a string representation of the book.

#     @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title,
#        author, isbn". It means that you must use the class reference cls to create a new object of the Book class
#        using a string.

# Example: 

# book = “La Divina Commedia, D. Alighieri, 999000666”
# divina_commedia: Book = Book.from_string(book)
# Here divina_commedia must contain an instance of the class Book with 

# title = La Divina Commedia, author = D. Alighieri, isbn = 999000666

class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"Title: {self.title}\nAuthor: {self.author}\nIsbn: {self.isbn}"
    
    @classmethod
    def from_string(cls, book_str: str):
        string_list: list= book_str.split(', ')
        return Book(string_list[0], string_list[1], string_list[2])

# Create a Member class with the following attributes: name, member_id, borrowed_books
# The member class must contain the following methods:

#     borrow_book(book) to add a book to the borrowed_books list.

#     return_book(book) to remove a book from the borrowed_books list.

#     __str__ method to return a string representation of the member.

#     @classmethod from_string(cls, member_str) to create a Member instance from a string in the format
#            "name, member_id".

class Member:
    def __init__(self, name: str, member_id: str) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books: list[Book] = []
    
    def borrow_book(self, book: Book) -> None:
        self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        self.borrowed_books.remove(book)

    def __str__(self) -> str:
        return f"Name: {self.name}\nMember ID: {self.member_id}\nBorrowed books: {self.borrowed_books}"
    
    @classmethod
    def from_string(cls, member_str: str):
        string_list: list= member_str.split(', ')
        return Member(string_list[0], string_list[1])

# Create a Library class with the following attributes: books, members, total_books (class attribute to keep
#    track of the total number of books)
# The library class must contain the following methods:

#     add_book(book) to add a book to the library and increment total_books.

#     remove_book(book) to remove a book from the library and decrement total_books.

#     register_member(member) to add a member to the library.

#     lend_book(book, member) to lend a book to a member. It should check if the book is available and if
#            the member is registered.

#     __str__ method to return a string representation of the library with the list of books and members.

#     @classmethod library_statistics(cls) to print the total number of books.

class Library:
    total_books: int= 0
    def __init__(self) -> None:
        self.books: list[Book]= []
        self.members: list[Member]= []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        Library.total_books += 1

    def remove_book(self, book: Book) -> None:
        self.books.remove(book)
        Library.total_books -= 1

    def register_member(self, member: Member) -> None:
        self.members.append(member)

    def lend_book(self, book: Book, member: Member) -> None:
        if book in self.books:
            if member in self.members:
                member.borrow_book(book)

# Create a script and play a bit with the classes:
# Create instances of books and members using class methods. Register members and add books to the library.
#    Lend books to members and display the state of the library before and after lending.

# Creazione di istanze di libri utilizzando il metodo di classe
book1_str = "La Divina Commedia, D. Alighieri, 999000666"
book1 = Book.from_string(book1_str)

book2_str = "Il Principe, N. Machiavelli, 888777555"
book2 = Book.from_string(book2_str)

# Creazione di istanze di membri utilizzando il metodo di classe
member1_str = "Mario Rossi, 123"
member1 = Member.from_string(member1_str)

member2_str = "Luigi Bianchi, 456"
member2 = Member.from_string(member2_str)

# Creazione di un'istanza di biblioteca
library = Library()

# Registrazione dei membri
library.register_member(member1)
library.register_member(member2)

# Verifica che i membri siano stati registrati correttamente
assert member1 in library.members
assert member2 in library.members

# Aggiunta di libri alla biblioteca
library.add_book(book1)
library.add_book(book2)

# Verifica che i libri siano stati aggiunti correttamente
assert book1 in library.books
assert book2 in library.books

# Prestito di libri ai membri
library.lend_book(book1, member1)
library.lend_book(book2, member2)

# Verifica che i libri siano stati prestati correttamente
assert book1 in member1.borrowed_books
assert book2 in member2.borrowed_books



# Exercise 4: University Management System


# Create a system to manage a university with departments, courses, professors, and students. 

# Create an abstract class Person:
# Attributes:

#     name (string)
#     age (int)

# Methods:

#     __init__ method to initialize the attributes.
#     Abstract method get_role to be implemented by subclasses.
#     __str__ method to return a string representation of the person.

class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self) -> None:
        pass

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"

# Create subclasses Student and Professor that inherit from Person and implement the abstract methods:

# Student:
# Additional attributes: student_id (string), courses (list of Course instances)
# Method enroll(course) to enroll the student in a course.

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.courses: list['Course']= []

    def get_role(self) -> None:
        return "Student"
    
    def enroll(self, course: 'Course') -> None:
        self.courses.append(course)

    def __str__(self) -> str:
        return super().__str__()
    
    def __repr__(self) -> str:
        return f"{self.name}"

# Professor:
# Additional attributes: professor_id (string), department (string), courses (list of Course instances)
# Method assign_to_course(course) to assign the professor to a course.

class Professor(Person):
    def __init__(self, name: str, age: int, professor_id: str, department: str) -> None:
        super().__init__(name, age)
        self.professor_id = professor_id
        self.department = department
        self.courses: list['Course'] = []

    def get_role(self) -> None:
        return "Professor"

    def assign_to_course(self, course: 'Course'):
        self.courses.append(course)

    def __str__(self) -> str:
        return super().__str__()
    
    def __repr__(self) -> str:
       return f"{self.name}"

# Create a class Course:
# Attributes:

#     course_name (string)
#     course_code (string)
#     students (list of Student instances)
#     professor (Professor instance)

# Methods:

#     __init__ method to initialize the attributes.
#     add_student(student) to add a student to the course.
#     set_professor(professor) to set the professor for the course.
#     __str__ method to return a string representation of the course.

class Course:
    def __init__(self, course_name: str, course_code: str) -> None:
        self.course_name = course_name
        self.course_code = course_code
        self.students: list[Student]
        self.professor: Professor = None

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def set_professor(self, professor: Professor) -> None:
        self.professor = professor
    
    def __str__(self) -> str:
        return f"Course name: {self.course_name}\nCourse code: {self.course_code}\nStudents enrolled: {self.students}\nProfessor: {self.professor}"

# Create a class Department:

# Attributes:

#     department_name (string)
#     courses (list of Course instances)
#     professors (list of Professor instances)


# Methods:

#     __init__ method to initialize the attributes.
#     add_course(course) to add a course to the department.
#     add_professor(professor) to add a professor to the department.
#     __str__ method to return a string representation of the department.

class Department:
    def __init__(self, department_name: str) -> None:
        self.department_name = department_name
        self.courses: list[Course] = []
        self.professors: list[Professor] = []

    def add_course(self, course: Course) -> None:
        self.courses.append(course)

    def add_professor(self, professor: Professor) -> None:
        self.professors.append(professor)

    def __str__(self) -> str:
        return f"Department name: {self.department_name}\nCourses: {self.courses}\nProfessors: {self.professors}"
    
    def __repr__(self) -> str:
        return f"{self.department_name}"


# Create a class University:

# Attributes:

#     name (string)
#     departments (list of Department instances)
#     students (list of Student instances)


# Methods:

#     __init__ method to initialize the attributes.
#     add_department(department) to add a department to the university.
#     add_student(student) to add a student to the university.
#     __str__ method to return a string representation of the university.

class University:
    def __init__(self, name: str) -> None:
        self.name = name
        self.departments: list[Department] = []
        self.students: list[Student] = []
    
    def add_department(self, department: Department) -> None:
        self.departments.append(department)

    def add_student(self, student: Student) -> None:
        self.students.append(student)
    
    def __str__(self) -> str:
        return f"University name: {self.name}\nDepartments: {self.departments}\nStudents: {self.students}"


# Create a script:

# Create instances of departments, courses, professors, and students.
# Add them to the university.
# Enroll students in courses and assign professors to courses.
# Display the state of the university.

def test_university_system():
    # Create instances of departments, courses, professors, and students.
    math_dept = Department("Mathematics")
    cs_dept = Department("Computer Science")

    calculus = Course("Calculus", "MATH101")
    programming = Course("Programming", "CS101")

    prof_john = Professor("John Doe", 45, "P1", "Mathematics")
    prof_jane = Professor("Jane Doe", 40, "P2", "Computer Science")

    student_anna = Student("Anna Smith", 20, "S1")
    student_bob = Student("Bob Johnson", 22, "S2")

    uni = University("My University")

    # Add them to the university.
    uni.add_department(math_dept)
    uni.add_department(cs_dept)

    uni.add_student(student_anna)
    uni.add_student(student_bob)

    # Enroll students in courses and assign professors to courses.
    student_anna.enroll(calculus)
    student_bob.enroll(programming)

    prof_john.assign_to_course(calculus)
    prof_jane.assign_to_course(programming)

    # Display the state of the university.
    print(uni)

    # Assertions to test the system
    assert student_anna.get_role() == "Student"
    assert prof_john.get_role() == "Professor"
    assert calculus in student_anna.courses
    assert programming in student_bob.courses
    assert calculus in prof_john.courses
    assert programming in prof_jane.courses
    assert math_dept in uni.departments
    assert cs_dept in uni.departments
    assert student_anna in uni.students
    assert student_bob in uni.students

test_university_system()