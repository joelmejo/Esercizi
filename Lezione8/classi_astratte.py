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

# Create subclasses Student and Professor that inherit from Person and implement the abstract methods:

# Student:
# Additional attributes: student_id (string), courses (list of Course instances)
# Method enroll(course) to enroll the student in a course.
# Professor:
# Additional attributes: professor_id (string), department (string), courses (list of Course instances)
# Method assign_to_course(course) to assign the professor to a course.


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


# Create a script:

# Create instances of departments, courses, professors, and students.
# Add them to the university.
# Enroll students in courses and assign professors to courses.
# Display the state of the university.