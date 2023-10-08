class Student:
    def __init__(self, name):
        self.name = name
        self.quiz_score = [0] * 15 

class FullTimeStudent(Student):
    def __init__(self, name):
        super().__init__(name)
        self.exam_score = [0] * 2

class PartTimeStudent(Student):
    def __init__(self, name):
        super().__init__(name)

