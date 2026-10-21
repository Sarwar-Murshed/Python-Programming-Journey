
marks = int(input("Enter student marks : "))

if (marks < 0 or marks > 100):
    print("You entered invalid marks")

else:
    if (marks >= 90):
        grade = "A"
        GPA = "4.00"

    elif (marks >= 86 and marks < 90):
        grade = "A-"
        GPA = "3.67"

    elif (marks >= 82 and marks < 86):
        grade = "B+"
        GPA = "3.33"

    elif (marks >= 78 and marks < 82):
        grade = "B"
        GPA = "3.00"

    elif (marks >= 74 and marks < 78):
        grade = "C"
        GPA = "2.67"

    elif (marks >= 68 and marks < 74):
        grade = "C"
        GPA = "2.67"

    else:
        grade = "F"
        GPA = "0.00"

    print("Grade:", grade, "\t GPA:", GPA)