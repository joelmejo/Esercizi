import unittest
from classi_astratte import *

class testEx1(unittest.TestCase):
    def setUp(self) -> None:
        self.circle = Circle(5)
        self.rectangle = Rectangle(4, 5)
    
    def test_perimeter(self):
        self.assertEqual(self.circle.perimeter(), 2*pi*5)
        self.assertEqual(self.rectangle.perimeter(), 18)

    def test_area(self):
        self.assertEqual(self.circle.area(), pi*25)
        self.assertEqual(self.rectangle.area(), 20)

class testEx2(unittest.TestCase):
    def setUp(self) -> None:
        self.num1 = 5
        self.num2 = 7
    
    def test_sum(self):
        self.assertEqual(MathOperations.sum(self.num1, self.num2), 12)

    def test_multiply(self):
        self.assertEqual(MathOperations.multiply(self.num1, self.num2), 35)

class testEx3(unittest.TestCase):
    def setUp(self) -> None:
        self.book = Book("B001", "Book1", "122312425")
        self.member = Member("M001", "Member1")
        self.library = Library()
        self.library.add_book(self.book)
        self.library.register_member(self.member)

    def test_isInstance(self):
        self.assertIsInstance(self.book, Book)
        self.assertIsInstance(self.member, Member)
        self.assertIsInstance(self.library, Library)
    
    def test_In(self):
        self.assertIn(self.book, self.library.books)
        self.assertIn(self.member, self.library.members)

    def test_not_borrowed(self):
        self.assertNotIn(self.book, self.member.borrowed_books)

class testEx4(unittest.TestCase):
    def setUp(self):
        self.math_dept = Department("Mathematics")
        self.cs_dept = Department("Computer Science")

        self.calculus = Course("Calculus", "MATH101")
        self.programming = Course("Programming", "CS101")

        self.prof_john = Professor("John Doe", 45, "P1", "Mathematics")
        self.prof_jane = Professor("Jane Doe", 40, "P2", "Computer Science")

        self.student_anna = Student("Anna Smith", 20, "S1")
        self.student_bob = Student("Bob Johnson", 22, "S2")

        self.uni = University("My University")

        self.uni.add_department(self.math_dept)
        self.uni.add_department(self.cs_dept)

        self.uni.add_student(self.student_anna)
        self.uni.add_student(self.student_bob)

        self.student_anna.enroll(self.calculus)
        self.student_bob.enroll(self.programming)

        self.prof_john.assign_to_course(self.calculus)
        self.prof_jane.assign_to_course(self.programming)

    def test_isInstance(self):
        self.assertIsInstance(self.math_dept, Department)
        self.assertIsInstance(self.cs_dept, Department)
        self.assertIsInstance(self.calculus, Course)
        self.assertIsInstance(self.programming, Course)
        self.assertIsInstance(self.prof_jane, Professor)
        self.assertIsInstance(self.prof_john, Professor)
        self.assertIsInstance(self.student_anna, Student)
        self.assertIsInstance(self.student_bob, Student)
        self.assertIsInstance(self.uni, University)
    
    def test_In(self):
        self.assertIn(self.math_dept, self.uni.departments)
        self.assertIn(self.cs_dept, self.uni.departments)

        self.assertIn(self.student_anna, self.uni.students)
        self.assertIn(self.student_bob, self.uni.students)

        self.assertIn(self.calculus, self.student_anna.courses)
        self.assertIn(self.programming, self.student_bob.courses)

        self.assertIn(self.calculus, self.prof_john.courses)
        self.assertIn(self.programming, self.prof_jane.courses)

if __name__ == '__main__':
    unittest.main()