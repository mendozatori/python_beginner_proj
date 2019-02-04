# GRADE CALCULATION APPLICATION

# constant variables
ASSIGN_WEIGHT = .25
ASSIGN_MAX = 100
QUIZ_WEIGHT = .30
QUIZ_MAX = 25
MIDTERM_WEIGHT = .45
MIDTERM_MAX = 50

# set up input variables
first_assign = float(input("Please enter your assignment 1 score: "))
second_assign = float(input("Please enter your assignment 2 score: "))
third_assign = float(input("Please enter your assignment 3 score: "))

quiz_1 = float(input("Please enter quiz 1 score: "))
quiz_2 = float(input("Please enter quiz 1 score: "))

midterm = float(input("Please enter mid-term score: "))

# calculations
midterm_weight = (midterm * MIDTERM_WEIGHT) / MIDTERM_MAX

average_assign = (first_assign + second_assign + third_assign) / 3
avg_assign_weight = (average_assign * ASSIGN_WEIGHT) / ASSIGN_MAX

average_quiz = (quiz_1 + quiz_2) / 2
avg_quiz_weight = (average_quiz * QUIZ_WEIGHT) / QUIZ_MAX

# overall grade calculation
overall_grade = (avg_assign_weight + avg_quiz_weight + midterm_weight) * 100

# print statements
print("The average of the assignments is: ", average_assign)
print("The average of the quizzes is: ", average_quiz)
print("The overall grade is: ", overall_grade)
