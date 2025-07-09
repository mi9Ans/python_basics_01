import pandas as pd

#Load student data
df = pd.read_csv("student.csv")

print("📃 Full Student Data:\n")
print(df)

# Step 2: Add total and average columns
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = round(df["Total"] / 3, 2)

print("\n📊 Student Totals and Averages:\n")
print(df[["Name", "Total", "Average"]])

# Step 3: Find topper and lowest scorer
topper_row = df[df["Total"] == df["Total"].max()]
lowest_row = df[df["Total"] == df["Total"].min()]

print("\n🏆 Topper:\n", topper_row[["Name", "Total", "Average"]])
print("\n📉 Lowest Scorer:\n", lowest_row[["Name", "Total", "Average"]])

# Step 4: Subject-wise Averages
math_avg = round(df["Math"].mean(), 2)
sci_avg = round(df["Science"].mean(), 2)
eng_avg = round(df["English"].mean(), 2)

print("\n📚 Subject-wise Averages:")
print(f"Math: {math_avg}")
print(f"Science: {sci_avg}")
print(f"English: {eng_avg}")

# Step 5: Save updated data to a new file
df.to_csv("student_summary.csv", index=False)
print("\n✅ Summary saved to 'student_summary.csv'")
