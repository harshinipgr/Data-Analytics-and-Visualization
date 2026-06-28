# Student Marks Analysis

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the folder where this Python file is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# Create output folder
output_folder = os.path.join(current_folder, "output")
os.makedirs(output_folder, exist_ok=True)
df = pd.read_csv("c:\\Users\\harvi\\Desktop\\Extras\\Data-Analytics-and-Visualization\\01_Student_Marks_Analysis\\student_marks.csv")

# Display dataset
print("\nStudent Marks Dataset")
print(df)

# Calculate Total Marks
df["Total"] = df["Math"] + df["Science"] + df["English"]

# Calculate Average Marks
df["Average"] = df["Total"] / 3

# Assign Grade
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(grade)

# Pass/Fail Status
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Display updated dataset
print("\nStudent Performance")
print(df)

# Class Statistics
print("\nClass Statistics")
print("------------------------")
print("Highest Average :", df["Average"].max())
print("Lowest Average  :", df["Average"].min())
print("Class Average   :", round(df["Average"].mean(),2))

# Topper
topper = df.loc[df["Average"].idxmax()]
print("\nTopper")
print("------------------------")
print("Name :", topper["Name"])
print("Average :", round(topper["Average"],2))

# Grade Count
print("\nGrade Distribution")
print(df["Grade"].value_counts())

# Save updated report
df.to_csv(os.path.join(output_folder, "student_report.csv"), index=False)

# ------------------------------
# Visualization
# ------------------------------

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Average"])
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.savefig(os.path.join(output_folder, "bar_chart.png"))
plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
df["Grade"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Grade Distribution")
plt.ylabel("")
plt.savefig(os.path.join(output_folder, "pie_chart.png"))
plt.show()

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Average"], bins=5)
plt.title("Distribution of Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.savefig(os.path.join(output_folder, "histogram.png"))
plt.show()