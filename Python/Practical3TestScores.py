finalExamPercentage = 50
test1 = int(input("Enter score for Test 1: "))
test2 = int(input("Enter score for Test 2: "))
test3 = int(input("Enter score for Test 3: "))
finalExam= int(input("Enter score for Final Exam: "))
percentageTest1 = int(input("Enter percentage for Test 1: "))
percentageTest2 = int(input("Enter percentage for Test 2: "))
percentageTest3 = int(input("Enter percentage for Test 3: "))

totalPercentage = percentageTest1 + percentageTest2 + percentageTest3 + finalExamPercentage
if totalPercentage != 100:
    print("Error: Total percentage must equal 100.") 
    exit()

finalMarks= (test1 * percentageTest1 / 100) + (test2 * percentageTest2 / 100) + (test3 * percentageTest3 / 100) + (finalExam * finalExamPercentage / 100)
match finalMarks:
    case _ if finalMarks >= 90:
        grade = "A"
    case _ if finalMarks >= 80:
        grade = "B"
    case _ if finalMarks >= 70:
        grade = "C"
    case _ if finalMarks >= 60:
        grade = "D"
    case _:
        grade = "F"

print("Your final marks are:", round(finalMarks, 2), "and your grade is:", grade)