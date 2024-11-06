
student = {
    "name": "Sneha",
    "roll_number": "54",
    "registration_number": "MES24MCA-2054",
    "department": "MCA",
    "semester": "1 st"
}


print("\nStudent list:\n\n", student)

total_marks = int(input("\n\nEnter the total marks: "))

student["total_mark"] = total_marks

print("\n\nStudent list updated with total marks:\n\n", student)
if student["total_mark"] >= 90:
    student["grade"] = "A"
elif student["total_mark"] >= 82:
    student["grade"] = "B"
elif student["total_mark"] >= 75:
    student["grade"] = "C"
elif student["total_mark"] >= 60:
    student["grade"] = "D"
elif student["total_mark"] >= 50:
    student["grade"] = "P"
else:
    student["grade"] = "F"

print("\n\nStudent list updated with grade:\n\n", student)

del student["roll_number"]
print("\n\nStudent list after deleting roll number:\n\n", student)
