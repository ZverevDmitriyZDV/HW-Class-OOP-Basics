class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def list_process(self, list_needed):
        if len(list_needed):
            result_str = list_needed[0]
            for i in range(1, len(list_needed)):
                result_str += f', {list_needed[i]}'
        else:
            result_str = 'Не обнаруженно'
        return result_str

    def __str__(self):
        result = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}\n'
                  f'Средняя оценка за домашние задания: {mid_score(self.grades)}\n'
                  f'Курсы в процессе изучения: {self.list_process(self.courses_in_progress)}\n'
                  f'Завершенные курсы: {self.list_process(self.finished_courses)}')
        return result

    def __lt__(self, other_student):
        return compare(self, other_student, Student)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        result = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}\n'
                  f'Средняя оценка за лекции {mid_score(self.grades)}')
        return result

    def __lt__(self, other_lecturer):
        return compare(self, other_lecturer, Lecturer)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}')
        return result


def mid_score(grades_dict):
    total_score = 0
    total_number = 0
    for key in grades_dict.keys():
        for elem in grades_dict[key]:
            total_score += int(elem)
            total_number += 1
    if total_number:
        return total_score / total_number
    else:
        return "Оценок не обнаружено"


def compare(class1, class2, root_class):
    if isinstance(class2, root_class):
        candidate1 = f'{class1.name} {class1.surname}'
        candidate2 = f'{class2.name} {class2.surname}'
        if mid_score(class1.grades) > mid_score(class2.grades):
            line = f'{candidate1} имеет средний балл больше чем {candidate2}'
        elif mid_score(class1.grades) == mid_score(class2.grades):
            line = f'{candidate1} и {candidate2} имеют одинаковый балл'
        else:
            line = f'{candidate2} имеет средний балл больше чем {candidate1}'
        return line
    else:
        err_line = f'Некорректный ввод все данный должны быть: {root_class.__name__}'
        return err_line


def mid_score_by_course(person_list, course_name, check_class):
    grades = []
    for i in range(len(person_list)):
        if not isinstance(person_list[i], check_class):
            return f'Некорректный ввод все данные должны быть {check_class.__name__}'
        if course_name in person_list[i].grades.keys():
            grades += person_list[i].grades[course_name]
    result = f'средний балл за курс {course_name} среди {check_class.__name__} составляет: {mid_score({course_name: grades})}'
    return result


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['BIM']

mid_student = Student('Emmely', 'Riot', 'your_gender')
mid_student.courses_in_progress += ['Python']
mid_student.courses_in_progress += ['BIM']
mid_student.courses_in_progress += ['XOR']

mentor_reviewer = Reviewer('Some', 'Buddy Revier')
mentor_reviewer.courses_attached += ['Python']

mentor2_reviewer = Reviewer('Dummy', 'Buer')
mentor2_reviewer.courses_attached += ['BIM']

mentor_lecturer = Lecturer('Boddy', 'Some Lector')
mentor_lecturer.courses_attached += ['Python']

mentor2_lecturer = Lecturer('BoomBuddy', 'Furious')
mentor2_lecturer.courses_attached += ['Python']
mentor2_lecturer.courses_attached += ['BIM']

mentor_reviewer.rate_hw(best_student, 'Python', 10)
mentor_reviewer.rate_hw(best_student, 'Python', 9)
mentor2_reviewer.rate_hw(best_student, 'BIM', 8)
mentor2_reviewer.rate_hw(best_student, 'BIM', 6)
mentor_reviewer.rate_hw(mid_student, 'Python', 7)
mentor_reviewer.rate_hw(mid_student, 'Python', 3)
mentor2_reviewer.rate_hw(mid_student, 'BIM', 2)
mentor2_reviewer.rate_hw(mid_student, 'BIM', 10)

best_student.rate_lector(mentor_lecturer, 'Python', 8)
best_student.rate_lector(mentor2_lecturer, 'Python', 8)
best_student.rate_lector(mentor2_lecturer, 'BIM', 9)

mid_student.rate_lector(mentor_lecturer, 'Python', 2)
mid_student.rate_lector(mentor2_lecturer, 'Python', 3)
mid_student.rate_lector(mentor2_lecturer, 'BIM', 5)

print(best_student.grades)
print(mid_student.grades)
print('________________')
print(mentor_lecturer.grades)
print(mentor2_lecturer.grades)
print('________________')
print(best_student)
print(mid_student)
print('________________')
print(mentor_lecturer)
print(mentor2_lecturer)
print('________________')
print(mentor_reviewer)
print('________________')
print(mentor2_lecturer < mentor_lecturer)
print(mentor2_lecturer < best_student)
print('________________')
print(best_student < mentor2_lecturer)
print(best_student < mid_student)
print('________________')
need_course = 'BIM'
print(mid_score_by_course([best_student, mid_student], need_course, Student))
need_course2 = 'Python'
print(mid_score_by_course([best_student, mid_student], need_course2, Student))
print('________________')
print(mid_score_by_course([mentor2_lecturer, mentor_lecturer], need_course, Lecturer))
print(mid_score_by_course([mentor2_lecturer, mentor_lecturer], need_course2, Lecturer))
print(mid_score_by_course([mentor2_lecturer, mentor_lecturer,mentor2_reviewer], need_course2, Lecturer))
