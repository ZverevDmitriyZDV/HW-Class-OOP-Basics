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

    def mid_score(self, grades_dict):
        total_score = 0
        total_number = 0
        for key in grades_dict.keys():
            for elem in grades_dict[key]:
                total_score += elem
                total_number += 1
        if total_number:
            return total_score / total_number
        else:
            return "Оценок не обнаружено"

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
                  f'Средняя оценка за домашние задания: {self.mid_score(self.grades)}\n'
                  f'Курсы в процессе изучения: {self.list_process(self.courses_in_progress)}\n'
                  f'Завершенные курсы: {self.list_process(self.finished_courses)}\n')
        return result


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
                  f'Средняя оценка за лекции {Student.mid_score(self,self.grades)}\n')
        return result


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
                  f'Фамилия: {self.surname}\n')
        return result


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['BIM']

mentor_reviewer = Reviewer('Some', 'Buddy Revier')
mentor_lecturer = Lecturer('Boddy', 'Some Lector')
mentor_reviewer.courses_attached += ['Python']
mentor_lecturer.courses_attached += ['Python']

mentor_reviewer.rate_hw(best_student, 'Python', 10)
mentor_reviewer.rate_hw(best_student, 'Python', 9)
mentor_reviewer.rate_hw(best_student, 'BIM', 8)
mentor_reviewer.rate_hw(best_student, 'BIM', 6)
best_student.rate_lector(mentor_lecturer, 'Python', 8)
best_student.rate_lector(mentor_lecturer, 'Pythonize', 6)
best_student.rate_lector(mentor_reviewer, 'Pythonize', 0)

# print(best_student.grades)
# print(mentor_lecturer.grades)
print(best_student)
print(mentor_lecturer)
print(mentor_reviewer)