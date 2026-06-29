# Student Information System
name=input("Enter Student Name:")
roll_no=input("Enter Roll Number:")
branch=input("Enter Branch:")
age=int(input("Enter Age:"))
marks=float(input("Enter Marks:"))

print("\n======STUDENT DETAILS======")
print("Name     :",name)
print("Roll no  :",roll_no)
print("Branch   :",branch )
print("Age      :",age)
print("Marks    :",marks)

if marks>=40:
    print("Result  :Pass")
else:
    print("Result   :Fail")    