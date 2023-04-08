class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка!!!'

    def average_score(self):
        middle_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            middle_of_course = course_sum / len(course_grades)
            middle_sum += middle_of_course
        if middle_sum == 0:
            return f'Студент еще не получал оценки!'
        else:
            return f'{middle_sum / len(self.grades.values()):.2f}'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        res += f'Средняя оценка за домашние задания: {self.average_score()} \n'
        res += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
        res += f'Завершенные курсы: {", ".join(self.finished_courses)} \n'
        return res

    def __lt__(self, student):
        if not isinstance(student, Student):
            print(f'Такого студента нет!')
            return
        return self.average_score() < student.average_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}


class Lecturer(Mentor):
    def middle_rate(self):
        middle_sum = 0
        for course_grades in self.rates.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            middle_of_course = course_sum / len(course_grades)
            middle_sum += middle_of_course
        if middle_sum == 0:
            return f'Оценки еще не выставлялись!'
        else:
            return f'{middle_sum / len(self.rates.values()):.2f}'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        res += f'Средняя оценка: {self.middle_rate()}\n'
        return res

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print(f' Такого лектора нет! ')
            return
        return self.middle_rate() < lecturer.middle_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка!!!'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return res


def grades_students(students_list, course):
    overall_student_rating = 0
    lectors = 0
    for listener in students_list:
        if course in listener.grades.keys():
            average_student_score = 0
            for grades in listener.grades[course]:
                average_student_score += grades
            overall_student_rating = average_student_score / len(listener.grades[course])
            average_student_score += overall_student_rating
            lectors += 1
    if overall_student_rating == 0:
        return f'Оценок по этому предмету нет!'
    else:
        return f'{overall_student_rating / lectors:.2f}'


def grades_lecturers(lecturer_list, course):
    average_rating = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.rates.keys():
            lecturer_average_rates = 0
            for rate in lecturer.rates[course]:
                lecturer_average_rates += rate
            overall_lecturer_average_rates = lecturer_average_rates / len(lecturer.rates[course])
            average_rating += overall_lecturer_average_rates
            b += 1
    if average_rating == 0:
        return f'Оценок по этому предмету нет!'
    else:
        return f'{average_rating / b:.2f}'

# Студенты
student_1 = Student('Ольга', 'Иванова', 'Жен.')
student_1.finished_courses = ['Python', 'C++']
student_1.courses_in_progress = ['Git', 'Java']

student_2 = Student('Николай', 'Наумов', 'Муж.')
student_2.finished_courses = ['Java', 'Git']
student_2.courses_in_progress = ['Python', 'С++']
students_list = [student_1, student_2]

# Лекторы
lecturer_1 = Lecturer('Евгений', 'Шмаргунов')
lecturer_1.courses_attached = ['Git', 'Java']

lecturer_2 = Lecturer('Алёна', 'Батицкая')
lecturer_2.courses_attached = ['Python', 'C++']
lecturer_list = [lecturer_1, lecturer_2]


# Проверяющие
reviewer_1 = Reviewer('Олег', 'Булыгин')
reviewer_1.courses_attached = ['Python', 'С++', 'Java', 'Git']

reviewer_2 = Reviewer('Максим', 'Федотов')
reviewer_2.courses_attached = ['Git', 'Python', 'С++']


# Оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_1, 'С++', 9)
reviewer_1.rate_hw(student_1, 'С++', 1)
reviewer_1.rate_hw(student_1, 'С++', 3)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_1, 'Java', 1)
reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'Java', 9)

reviewer_2.rate_hw(student_2, 'Java', 10)
reviewer_2.rate_hw(student_2, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 4)
reviewer_2.rate_hw(student_2, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 10)
reviewer_2.rate_hw(student_2, 'С++', 10)
reviewer_2.rate_hw(student_2, 'С++', 10)
reviewer_2.rate_hw(student_2, 'С++', 10)

#Оценки лекторам
student_1.rate_lecturer(lecturer_1, 'Git', 1)
student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_1.rate_lecturer(lecturer_1, 'Java', 3)
student_1.rate_lecturer(lecturer_1, 'Java', 5)
student_1.rate_lecturer(lecturer_1, 'Java', 10)


student_2.rate_lecturer(lecturer_1, 'Java', 10)
student_2.rate_lecturer(lecturer_1, 'Java', 10)
student_2.rate_lecturer(lecturer_1, 'Java', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Python', 7)
student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'C++', 0)


print('Проверяющие:')
print(reviewer_1)
print(reviewer_2, end='\n\n')

print('Лекторы:')
print(lecturer_1)
print(lecturer_2, end='\n\n')

if lecturer_1 > lecturer_2:
    print(f'{lecturer_1.name} {lecturer_1.surname}  преподает лучше чем {lecturer_2.name} {lecturer_2.surname}.\n\n')
else:
    print(f'{lecturer_2.name} {lecturer_2.surname}  преподает лучше чем {lecturer_1.name} {lecturer_1.surname}.\n\n')

print('Студенты:')
print(student_1, end='\n')
print(student_2, end='\n\n')

if student_1 > student_2:
    print(f'{student_1.name} учится лучше чем {student_2.name}.\n\n')
else:
    print(f'{student_2.name} учится лучше чем {student_1.name}.\n\n')





print(f'Средняя оценка студентов по курсу "Git": {grades_students(students_list, "Git")}')
print(f'Средняя оценка студентов по курсу "Java": {grades_students(students_list, "Java")}')
print(f'Средняя оценка студентов по курсу "Python": {grades_students(students_list, "Python")}')
print(f'Средняя оценка студентов по курсу "С++": {grades_students(students_list, "С++")}\n')

print(f'Средняя оценка лекторов по курсу "Git": {grades_lecturers(lecturer_list, "Git")}')
print(f'Средняя оценка лекторов по курсу "Java": {grades_lecturers(lecturer_list, "Java")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(lecturer_list, "Python")}')
print(f'Средняя оценка студентов по курсу "С++": {grades_lecturers(lecturer_list, "С++")}')