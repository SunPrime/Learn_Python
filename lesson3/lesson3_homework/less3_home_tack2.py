#Ведомость
class Register():
    total_2 = 0
    total_3 = 0
    total_4 = 0
    total_5 = 0

    def __init__(self, subj, lect):
        self.register = []
        self.subj = subj
        self.lect = lect

    def add_grade(self, student, grade):
        self.register.append(grade)
        if grade == 5:
            self.total_5 += 1
        elif grade == 4:
            self.total_4 += 1
        elif grade == 3:
            self.total_3 += 1
        else:
            self.total_2 += 1

    def __str__(self):
        return "Предмет: %s\nПреподаватель: %s\n" \
              "%d студ. - получили оценку 5\n" \
              "%d студ. - получили оценку 4\n" \
              "%d студ. - получили оценку 3\n" \
              "%d студ. - получили оценку 2\n" % (self.subj.subject, self.lect.lecturer, self.total_5, self.total_4, self.total_3, self.total_2)

#Преподаватель
class Lecturer():
    def __init__(self, lecturer):
        self.lecturer = lecturer

#Студент
class Student():
    def __init__(self, student):
        self.student = student

#Предмет
class Subject():
    def __init__(self, subject):
        self.subject = subject


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
print(register1)