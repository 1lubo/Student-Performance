import json
from pathlib import Path


def get_average_mark_student(student):
    overall_mark = 0
    for mark in student:
        if mark in subjects:
            overall_mark += student[mark]
    student['average'] = overall_mark / len(subjects)
    return student  # return student report card with added average mark


# add mark for subject to dictionary of individual subject marks
def get_average_mark_subject(student):
    for mark in student:
        if mark in subjects:
            if mark in subject_marks:
                subject_marks[mark] = subject_marks.get(mark) + student[mark]
            else:
                subject_marks[mark] = student[mark]


# add average mark for subject to dictionary of individual grade marks
def get_average_mark_grade(student):
    student_grade = student.get('grade')
    if student_grade in grade_marks:
        grade_marks[student_grade] = grade_marks.get(
            student_grade) + student.get('average')
    else:
        grade_marks[student_grade] = student.get('average')


files = Path('./students').glob('*')
subjects = ['math', 'science', 'history', 'english', 'geography']
report_cards = []
subject_marks = {}
grade_marks = {}
average_grade = 0

for file in files:  # iterate through all files
    with open(file, 'r') as f:  # open file
        data = json.load(f)  # load data
        report_cards.append(get_average_mark_student(data))


for card in report_cards:
    get_average_mark_subject(card)
    get_average_mark_grade(card)
    average_grade += card.get('average')

worst_student = min(report_cards, key=lambda card: card['average'])
best_student = max(report_cards, key=lambda card: card['average'])

print(f''' 
Average Student Grade: {(average_grade / len(report_cards)):.2f}
Hardest Subject: {min(subject_marks, key=subject_marks.get)}
Easiest Subject: {max(subject_marks, key=subject_marks.get)}
Best Performing Grade: {max(grade_marks, key=grade_marks.get)}
Worst Performing Grade: {min(grade_marks, key=grade_marks.get)}
Best Student ID: {best_student['id']}
Worst Student ID: {worst_student['id']}
''')
