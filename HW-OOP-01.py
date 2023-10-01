from statistics import mean


class Students:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturers) and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        return (
            f'Имя: {self.name} \n'
            f'Фамилия: {self.surname} \n'
            f'Средняя оценка за домашние задания:  {self.__average_grade()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )

    def __average_grade(self):
        for grade in self.grades.values():
            return round(mean(grade), 2)

    def __lt__(self, other):
        if isinstance(other, Students):
            return self.__average_grade() < other.__average_grade()
        return False

    def __gt__(self, other):
        if isinstance(other, Students):
            return self.__average_grade() > other.__average_grade()
        return False

    def __eq__(self, other):
        if isinstance(other, Students):
            return self.__average_grade() == other.__average_grade()
        return False


class Mentors:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturers(Mentors):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия:{self.surname} \n'
                f'Средняя оценка за лекции: {self.__average_grade()}')

    def __average_grade(self):
        for grade in self.grades.values():
            return round(mean(grade), 2)

    def __lt__(self, other):
        if isinstance(other, Lecturers):
            return self.__average_grade() < other.__average_grade()
        return False

    def __gt__(self, other):
        if isinstance(other, Lecturers):
            return self.__average_grade() > other.__average_grade()
        return False

    def __eq__(self, other):
        if isinstance(other, Lecturers):
            return self.__average_grade() == other.__average_grade()
        return False


class Reviewers(Mentors):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия:{self.surname}'

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Students) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


student1 = Students('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Students('Tom', 'Cruse', 'male')
student2.courses_in_progress += ['Python', 'Java']
student2.finished_courses += ['Введение в программирование']

lecturer1 = Lecturers('Any', 'Key')
lecturer1.courses_attached += ['Python', 'Java']

lecturer2 = Lecturers('john', 'Dow')
lecturer2.courses_attached += ['Python', 'Git']

reviewer1 = Reviewers('Nice', ' Duck')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewers('Darth', 'Wader')
reviewer2.courses_attached += ['Python', 'Java']

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer1, 'Python', 9)

student1.rate_lecturer(lecturer2, 'Git', 8)
student1.rate_lecturer(lecturer2, 'Git', 10)
student1.rate_lecturer(lecturer2, 'Git', 10)

student1.rate_lecturer(lecturer2, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Python', 10)

student2.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer1, 'Java', 10)

student2.rate_lecturer(lecturer2, 'Git', 10)
student2.rate_lecturer(lecturer2, 'Git', 8)
student2.rate_lecturer(lecturer2, 'Git', 8)

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 9)

reviewer1.rate_hw(student1, 'Git', 10)
reviewer1.rate_hw(student1, 'Git', 10)
reviewer1.rate_hw(student1, 'Git', 9)

reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student1, 'Python', 9)

reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 10)

reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 8)

reviewer2.rate_hw(student2, 'Java', 9)
reviewer2.rate_hw(student2, 'Java', 8)
reviewer2.rate_hw(student2, 'Java', 8)

student_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]


def average_score_students(list_, course):
    all_grade = []
    for student in list_:
        avr_grd = student.grades.get(course)
        if avr_grd is not None:
            all_grade.append(mean(avr_grd))
    return round(mean(all_grade), 3)


def average_score_lecturers(list_, course):
    all_grade = []
    for lecturer in list_:
        avr_grd = lecturer.grades.get(course)
        if avr_grd is not None:
            all_grade.append(mean(avr_grd))
    return round(mean(all_grade), 3)
