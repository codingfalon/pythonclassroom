lloyd = {                               #create dictionary for each student's performance
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

def average(numbers):                  #function applies to each student
    total = sum(numbers)
    total = float(total)               #uses float to ensure decimal is utilized
    average = total/len(list(numbers)) #len counts how many numbers were used for average
    
    return average

def get_average(student):
    homework = average(student["homework"]) #key/value pairs provide data per student
    quizzes = average(student["quizzes"])
    tests = average(student["tests"]) 
    return .10*homework + .30*quizzes + .60*tests #preset formula for class grade
    
def get_letter_grade(score):
    if score >= 90:                    #preset formula for grading system
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "F" 

def get_class_average (students):
    results = []                            #begin with an empty list to call later
    for student in students:
        result = get_average(student)       #iterates through formula for each student
        results.append(result)
    return average(results)

students = [lloyd, alice, tyler]
print get_class_average(students)           #displays each students' (float) average     
print get_letter_grade(results)             #displays each students' letter grade