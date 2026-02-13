student_name = input("Enter student name: ")
maths_marks = int(input("Enter Maths marks: "))
science_marks = int(input("Enter Science marks: "))
english_marks = int(input("Enter English marks: "))
if maths_marks<0 or maths_marks>100 or science_marks<0 or science_marks>100 or english_marks<0 or english_marks>100:
    print("Invalid marks entered")
    exit()

total_marks = maths_marks + science_marks + english_marks
percentage = (total_marks/300)*100

if maths_marks<40 or science_marks<40 or english_marks<40 :
    print(f"Student Name: {student_name}\n Total Marks: {total_marks}\n Percentage: {percentage:.2f}\n Status: Fail")
else:
    if percentage>= 75:
        grade = "A"
    elif percentage>= 60 and percentage <70:
        grade = "B"
    else:
        grade= "C"
    print(f" Student Name: {student_name}\n Total Marks: {total_marks}\n Percentage: {percentage:.2f}\n Status: pass\n Grade: {grade}")
