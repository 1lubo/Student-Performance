# Student-Performance

For this project you will be asked to create a tool that can be used by the staff of a school to analyze the performance of students. Specifically, this tool will need to read the report cards of hundreds of students and display data like the average grade, hardest subject, best performing grade level and more.

This school has exactly *1000* students that are distributed across *8* grade levels. Each student is assigned a unique id from *0 - 999* inclusively. Each students report card is stored in a *.json* file that is titled *student-id.json* These *.json* files contain the students grade level and their marks in each of the five subjects offered by the school. This is an example of student #*0's* report card:

```
{
  "id": 0,
  "grade": 5,
  "math": 34,
  "science": 58,
  "history": 34,
  "english": 26,
  "geography": 99
}
```

From the above report card, we can see that student #*0* is in grade number *5*, earned a mark of *34* in math, a mark of *58* in geography etc. 

Your project will need to load all of the *.json* files and output the following information:

- **Average Student Mark**: The average student mark is calculated by first calculating each individual students average then determining the average of all students averages. For example, if student #1 has marks of ```{"math": 77, "science": 61, "history": 40, "english": 9, "geography": 48}``` then their average is *47*. If student #*2* has marks of ```{"math": 43, "science": 52, "history": 80, "english": 58, "geography": 63}``` then their average is *59.2*. If these were the only two students the Average Student Mark would be *53.1*.
    
- **Hardest Subject**: The hardest subject is the subject that has the lowest average grade across all students.
- **Easiest Subject**: The easiest subject is the subject that has the highest average grade across all students.
- **Best Performing Grade**: The best performing grade is the grade whose students have the highest average compared to all other grade levels.
- **Worst Performing Grade**: The worst performing grade is the grade whose students have the lowest average compared to all other grade levels.
- **Best Student ID**: The best student is the student with the highest average.
- **Worst Student ID**: The worst student is the student with the lowest average.

Please download the template folder to start this project. Inside the folder you will find a folder named students that contains 1000 .json files. Write your code inside of the main.py file and when finished confirm that your programs output matches the expected output. There is only one correct answer.

## **Expected Output**


- **Average Student Grade: 50.44**
- **Hardest Subject: geography**
- **Easiest Subject: english**
- **Best Performing Grade: 6**
- **Worst Performing Grade: 5**
- **Best Student ID: 549**
- **Worst Student ID: 637**

