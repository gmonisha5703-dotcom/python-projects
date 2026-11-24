# Student Marks Calculator

print("===== STUDENT MARKS CALCULATOR =====")

name = input("Enter Student Name: ")

subjects = ["Tamil", "English", "Maths", "Science", "Computer Science"]

total = 0

for subject in subjects:
    while True:
        try:
            mark = int(input(f"Enter {subject} Marks (0-100): "))

            if 0 <= mark <= 100:
                total += mark
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

average = total / len(subjects)

print("\n===== STUDENT RESULT =====")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)
print("==========================")
