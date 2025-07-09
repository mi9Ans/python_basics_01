### even_odd_counter.py
A simple while loop project that takes a number range and counts how many numbers are even and how many are odd. Great for learning loops and conditional logic.

### number_guess_game.py
A fun beginner project where the user tries to guess a secret number using a `while` loop. The program gives feedback ("Too Big" / "Too Small") after each guess and counts how many attempts it took to get it right..

### length_converter.py
A simple program that converts height from centimeters into feet and inches using float division, modulo, and rounding. It demonstrates type conversion and real-world unit conversion.

### emoji_mood_generator.py
A creative and interactive program that asks the user how they're feeling and responds with emojis and short messages based on their mood. It uses conditional logic, string input, and emoji support.

### password_checker.py
A simple password loop that keeps prompting the user until the correct password ("open123") is entered. Demonstrates sentinel-controlled loops and string comparison.

### prime_number_checker.py
Takes a number as input and checks whether it's a prime number. Uses a for loop to test divisibility from 2 to n-1. Demonstrates conditionals, user input, and basic logic.

## Project #22 - Mini Contact Book 📖

A terminal-based contact manager using Python dictionaries.

**Features:**
- Add or update contacts
- View all saved contacts
- Search contacts by name
- Uses `.get()`, `.items()`, and dictionary updates

## Project #23 - Student Grades Analyzer 📊

This project takes a dictionary of students and their marks, then performs key analysis tasks:

### ✅ Features:
- Calculates average marks
- Finds the topper (highest scorer)
- Identifies the lowest scorer
- Demonstrates use of `.items()`, loops, and conditionals
- Helps reinforce Python dictionary fundamentals

### 🧠 Concepts Used:
- Dictionary iteration
- If-else logic
- Variables for tracking top/bottom
- Arithmetic operations

This project sets a strong foundation for moving into Data Analysis.

## 📊 Project #24: Student Performance Summary Tool

This Python project reads student marks from a CSV file and performs a complete analysis — including totals, averages, toppers, lowest scorers, and subject-wise performance.

---

### ✅ Features

- 📥 Reads input from `students.csv`
- ➕ Calculates **total** and **average** marks for each student
- 🏆 Identifies the **topper** and **lowest scorer**
- 📚 Calculates **subject-wise averages** (Math, Science, English)
- 💾 Saves a new summary file (`student_summary.csv`)

---

### 📁 Files in This Project

| File Name                   | Description                          |
|----------------------------|--------------------------------------|
| `student_analysis.py`| Python script for analysis logic     |
| `students.csv`             | Input data file with student scores  |

---

### 🧠 Sample Input (`students.csv`)

```csv
Name,Math,Science,English
Amit,78,85,88
Neha,92,89,95
Ravi,65,70,72
Simran,88,90,84
Arjun,74,80,79


📊 Student Totals and Averages:
     Name  Total  Average
0   Amit    251    83.67
1   Neha    276    92.00
2   Ravi    207    69.00
3 Simran    262    87.33
4  Arjun    233    77.67

🏆 Topper:
    Name  Total  Average
1  Neha    276    92.0

📉 Lowest Scorer:
   Name  Total  Average
2  Ravi    207    69.0

📚 Subject-wise Averages:
Math: 79.4
Science: 82.8
English: 83.6

How to run
1)pip install pandas
2)python StudentSidebarAnalysis.py

Anshumaan Mishra
> Beginner Python Projects | July 2025
> Project #24 of 60

