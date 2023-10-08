from Student import FullTimeStudent, PartTimeStudent
from statistics import mean

class Session:
    def __init__(self):
        self.students = []
    
    def get_average_score_per_student(self, students):
        result = []
        for student in students:
            name = student.name
            average_score = mean(student.quiz_score)
            average_score = round(average_score, 1)
            result.append((name, average_score))
        return result
    
    def sort_quiz_scores(self, students):
        sorted_list = sorted(self.get_average_score_per_student(students), key=lambda x:x[1])
        return sorted_list
    
    def check_status(self, students):
        result = []
        for student in students:
            if isinstance(student, PartTimeStudent):
                result.append(student.name)
        return result
    
    def get_exam_scores(self, students):
        result = []
        for student in students:
            if isinstance(student, FullTimeStudent):
                result.append((student.name, student.exam_score))
        return result