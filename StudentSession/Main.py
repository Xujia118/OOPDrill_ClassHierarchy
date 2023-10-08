from Student import FullTimeStudent, PartTimeStudent
from Session import Session
from student_list import student_list
import random

def populate_students(students_list):
    students = []

    # Set some students as full time, arbitrarily the first 13 students
    for i in range(0, 13):
        name = students_list[i]
        student = FullTimeStudent(name)
        student.quiz_score = [random.randint(60, 100) for _ in range(15)]
        student.exam_score = [random.randint(60, 100) for _ in range(2)]
        students.append(student)

    # Set some students as part time, arbitrarily the last 7 students
    for i in range(13, 20):
        name = students_list[i]
        student = PartTimeStudent(name)
        student.quiz_score = [random.randint(60, 100) for _ in range(15)]
        students.append(student)

    # Every item in the list is a student object
    return students

if __name__ == '__main__':
    students = populate_students(student_list)

    session = Session()
    
    # Calculate average quiz score per student
    average_score_per_student = session.get_average_score_per_student(students)
    for name, average_score in average_score_per_student:
        print(name, average_score)

    # Sort quiz score in ascending order
    sorted_average_score = session.sort_quiz_scores(students)
    for name, quiz_score in sorted_average_score:
        print(name, quiz_score)

    # Print part time student names
    part_time_students = session.check_status(students)
    for student in part_time_students:
        print(student)

    # Print exam scores of full time students
    full_time_students_exam_score = session.get_exam_scores(students)
    for name, exam_score in full_time_students_exam_score:
        print(name, exam_score)