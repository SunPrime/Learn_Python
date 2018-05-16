import unittest

from lesson3.lesson3_homework.less3_home_tack2 import Subject, Lecturer, Student, Register


class MyTestCase(unittest.TestCase):
    def test_Register(self):
        math = Subject("Теория вероятности")
        lect1 = Lecturer("Клевер О.И.")
        stud1 = Student("Иванов")
        stud2 = Student("Петров")
        stud3 = Student("Сидоров")
        stud4 = Student("Васечкин")
        register1 = Register(math, lect1)
        register1.add_grade(stud1, 5)
        register1.add_grade(stud2, 4)
        register1.add_grade(stud3, 3)
        register1.add_grade(stud4, 5)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
