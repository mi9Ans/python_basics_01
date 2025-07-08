# Student Grades Analyzer 📊

grades = {
    "Amit": 85,
    "Neha": 92,
    "Ravi": 78,
    "Simran": 90,
    "Arjun": 88
}

total = 0
highest = 0
lowest = 100
topper = ""
lowest_student = ""

for name, mark in grades.items():
    total += mark
    if mark > highest:
        highest = mark
        topper = name
    if mark < lowest:
        lowest = mark
        lowest_student = name

average = total / len(grades)

print("Average Marks:", average)
print("Topper:", topper, "with", highest)
print("Lowest Scorer:", lowest_student, "with", lowest)
