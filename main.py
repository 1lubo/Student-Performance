import json
from pathlib import Path
from statistics import mean

files = Path('./students').glob('*')

subjects = ['math', 'science', 'history', 'english', 'geography']
grades = {}
subject_grades = {}

for subject in subjects:  # initialize subject grades dictionary
    subject_grades[subject] = []


worst_student_id = 0  # start with the id of first student
worst_average = 100  # start with the highest possible average
best_student_id = 0  # start with the id of first student
best_average = 0  # start with the lowest possible average
num_students = 0  # counter for number of students
total_grades = 0  # overall grades

for file in files:  # iterate through all files
    with open(file, 'r') as f:  # open file
        data = json.load(f)  # load data
        current_id = data.get('id')
        current_grade = data.get('grade')

        current_average = []

        for subject in subjects:
            current_average.append(data.get(subject))
            subject_grades[subject].append(data.get(subject))

        if sum(current_average) / len(current_average) < worst_average:
            worst_student_id = current_id
            worst_average = sum(current_average) / len(current_average)
        if sum(current_average) / len(current_average) > best_average:
            best_student_id = current_id
            best_average = sum(current_average) / len(current_average)

        if current_grade in grades:
            grades[current_grade].append(
                sum(current_average) / len(current_average))
        else:
            grades[current_grade] = [
                sum(current_average) / len(current_average)]

        total_grades += sum(current_average) / len(current_average)
        num_students += 1

for grade in grades:
    average = mean(grades.get(grade))
    grades[grade] = average  # get average mark for each grade

for subject in subject_grades:
    average = mean(subject_grades.get(subject))
    subject_grades[subject] = average  # get average mark for each subject

print(
    f"Average Student Grade: {(total_grades / num_students):.2f} \n"
    f"Hardest Subject: {min(subject_grades, key=subject_grades.get)} \n"
    f"Easiest Subject: {max(subject_grades, key=subject_grades.get)} \n"
    f"Best Performing Grade: {min(grades, key=grades.get)} \n"
    f"Worst Performing Grade: {max(grades, key=grades.get)} \n"
    f"Best Student ID: {best_student_id} \n"
    f"Worst Student ID: {worst_student_id} "
)
