# Employee Data Analysis Project

import pandas as pd

# Employee Dataset
data = {
    "Name": ["Arun", "Priya", "Rahul", "Monisha", "Kavi"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [30000, 25000, 35000, 40000, 28000],
    "Experience": [2, 1, 3, 4, 2]
}

df = pd.DataFrame(data)

print("===== EMPLOYEE DATASET =====")
print(df)

print("\n===== DATA ANALYSIS =====")

print("Total Employees:", len(df))
print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())

print("\n===== DEPARTMENT ANALYSIS =====")
print(df.groupby("Department")["Salary"].mean())

print("\n===== EXPERIENCE ANALYSIS =====")
print(df.groupby("Department")["Experience"].mean())

print("\nData Analysis Completed Successfully!")
