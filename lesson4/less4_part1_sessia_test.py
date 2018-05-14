import unittest

from lesson4.less4_part1_sessia import Teacher, Subject, Student, Exam, Mark, Session


class TestCase_Session(unittest.TestCase):
    def test_statistics(self):
        teacher1 = Teacher('teacher1')
        subject1 = Subject('subject1')
        student1 = Student('student1')
        student2 = Student('student2')
        student3 = Student('student3')
        student4 = Student('student4')
        student5 = Student('student5')
        exam1 = Exam(subject1, 'today', teacher1)
        exam1.add_mark(Mark(student1, 3))
        exam1.add_mark(Mark(student2, 4))
        exam1.add_mark(Mark(student3, 5))
        exam1.add_mark(Mark(student4, 4))
        exam1.add_mark(Mark(student5, 2))
        session = Session('Spring 2018')
        session.add_exam(exam1)
        statistics = session.statistics()


if __name__ == '__main__':
    unittest.main()
