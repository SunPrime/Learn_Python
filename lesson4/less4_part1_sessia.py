class Statistics:
    def __init__(self):
        self.five = 0
        self.four = 0
        self.three = 0
        self.two = 0

    def __add__(self, other):
        result = Statistics()
        result.five = self.five + other.five
        result.four = self.four + other.four
        result.three = self.three + other.three
        result.two = self.two + other.two
        return result

    def __str__(self):
        return "Five: %s, four: %s, three: %s, two: %s" % (self.five, self.four, self.three, self.two)

# statistics1 = Statistics()
# statistics2 = Statistics()
# statistics3 = statistics1 + statistics2
# statistics3 = statistics1.__add__(statistics2)
class Session:
    def __init__(self, name):
        self.name = name
        self.exam_list = []

    def add_exam(self, exam):
        self.exam_list.append(exam)

    def statistics(self):
        result_statistics = Statistics()
        for exam in self.exam_list:
            result_statistics += exam.statistics()
        return result_statistics

class Exam:
    def __init__(self, subject, date, teacher):
        self.subject = subject
        self.date = date
        self.teacher = teacher
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def statistics(self):
        result_statistics = Statistics()
        for mark in self.marks:
            if mark.mark == 2:
                result_statistics.two += 1
            if mark.mark == 3:
                result_statistics.three += 1
            if mark.mark == 4:
                result_statistics.four +=1
            if mark.mark == 5:
                result_statistics.five += 1
        return result_statistics

class Mark:
    def __init__(self, student, mark):
        self.student = student
        self.mark = mark

class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name):
        self.name = name

class Subject:
    def __init__(self, name):
        self.name = name

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
print(statistics)