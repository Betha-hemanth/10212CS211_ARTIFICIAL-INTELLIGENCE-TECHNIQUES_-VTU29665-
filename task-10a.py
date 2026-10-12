# Student Information System

students = {
    "Ravi": "CSE",
    "Priya": "ECE",
    "Hemanth": "IT",
    "Uday": "EEE"
}

name = input("Enter student name: ")

if name in students:
    print("Department:", students[name])
else:
    print("Student not found")
