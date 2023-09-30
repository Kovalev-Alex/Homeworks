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
        return(
            f'Имя: {self.name} \n'
            f'Фамилия: {self.surname} \n'
            f'Средняя оценка за домашние задания: \n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )


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
                f'Средняя оценка за лекции: 9,9')

    def __compare(self,):
        pass


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


def comparison(student_list):
    pass


best_student = Students('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']


cool_lecturer = Lecturers('Any', 'Key')
cool_lecturer.courses_attached += ['Python']

cool_lecturer2 = Lecturers('john', 'Dow')
cool_lecturer2.courses_attached += ['Git']

hard_reviewer = Reviewers('Nice', ' Duck')
hard_reviewer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer2, 'Git', 8)
hard_reviewer.rate_hw(best_student, 'Python', 9)

print(best_student.grades)
print(cool_lecturer.grades)
print(cool_lecturer2.grades)
print(hard_reviewer)
print(cool_lecturer)
print(best_student)
