# ============================================================
#  Student Result Analyzer - Moderate Level Python Code
# ============================================================

import csv

# ---- Functions ----

def get_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 40:
        return 'D'
    else:
        return 'F'

def input_students():
    names      = []
    marks_list = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        print("\nStudent", i + 1)
        name  = input("  Enter student name          : ")
        marks = int(input("  Enter marks obtained (0-100): "))
        while marks < 0 or marks > 100:
            print("  Invalid! Marks must be between 0 and 100.")
            marks = int(input("  Enter marks obtained (0-100): "))
        names.append(name)
        marks_list.append(marks)
    return names, marks_list

def save_to_csv(names, marks_list, mode):
    # mode = 'w' for new report, 'a' for adding entries
    file   = open("student_results.csv", mode, newline="")
    writer = csv.writer(file)

    if mode == 'w':
        writer.writerow(["Name", "Marks", "Grade", "Pass/Fail"])  # header only for new file

    for i in range(len(names)):
        grade = get_grade(marks_list[i])
        if marks_list[i] >= 40:
            status = "Pass"
        else:
            status = "Fail"
        writer.writerow([names[i], marks_list[i], grade, status])

    file.close()

def read_from_csv():
    names      = []
    marks_list = []
    try:
        file   = open("student_results.csv", "r")
        reader = csv.reader(file)
        next(reader)   # skip header row
        for row in reader:
            if len(row) == 4:       # valid student row has 4 columns
                names.append(row[0])
                marks_list.append(int(row[1]))
        file.close()
    except:
        print("  No report found. Please create a new report first.")
    return names, marks_list

def display_entries(names, marks_list):
    if len(names) == 0:
        print("  No entries to display.")
        return
    print("\n" + "=" * 45)
    print("   STUDENT ENTRIES / GRADE FOR EACH STUDENT")
    print("=" * 45)
    print(f"{'Name':<15} {'Marks':<10} {'Grade':<8} {'Status'}")
    print("-" * 45)
    for i in range(len(names)):
        grade = get_grade(marks_list[i])
        if marks_list[i] >= 40:
            status = "Pass"
        else:
            status = "Fail"
        print(f"{names[i]:<15} {marks_list[i]:<10} {grade:<8} {status}")
    print("=" * 45)

def display_summary(names, marks_list):
    if len(names) == 0:
        print("  No data found. Please create a new report first.")
        return

    # Average
    total = 0
    for m in marks_list:
        total = total + m
    average = total / len(marks_list)

    # Highest
    highest_marks = marks_list[0]
    for m in marks_list:
        if m > highest_marks:
            highest_marks = m
    highest_name = names[marks_list.index(highest_marks)]

    # Lowest
    lowest_marks = marks_list[0]
    for m in marks_list:
        if m < lowest_marks:
            lowest_marks = m
    lowest_name = names[marks_list.index(lowest_marks)]

    # Pass / Fail count
    passed = 0
    failed = 0
    for m in marks_list:
        if m >= 40:
            passed = passed + 1
        else:
            failed = failed + 1

    pass_percent = (passed / len(marks_list)) * 100

    # Grade for each student
    grades = []
    for m in marks_list:
        grades.append(get_grade(m))

    # Grade-wise distribution (count of each grade)
    grade_counts = {"A+": 0, "A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades:
        grade_counts[g] = grade_counts[g] + 1

    print("\n" + "=" * 45)
    print("           REPORT SUMMARY / ANALYSIS")
    print("=" * 45)
    print(f"  Total Students  : {len(names)}")
    print(f"  Class Average   : {average:.2f}")
    print(f"  Highest Scorer  : {highest_name} ({highest_marks})")
    print(f"  Lowest Scorer   : {lowest_name} ({lowest_marks})")
    print(f"  Students Passed : {passed}")
    print(f"  Students Failed : {failed}")
    print(f"  Pass Percentage : {pass_percent:.2f}%")
    print("=" * 45)

    # ---- Grade-wise distribution ----
    print("\n" + "-" * 45)
    print("           GRADE-WISE DISTRIBUTION")
    print("-" * 45)
    for g in ["A+", "A", "B", "C", "D", "F"]:
        print(f"  {g:<4}: {grade_counts[g]}")
    print("=" * 45)


# ---- Main Program ----

print("\n" + "=" * 45)
print("       STUDENT RESULT ANALYZER")
print("=" * 45)

while True:
    print("\n  1 - Create New Report")
    print("  2 - Add Entries to Existing Report")
    print("  3 - View Report Summary / Analysis")
    print("  4 - Display Entries / Grade For Each Student")
    print("  5 - Exit")
    print("-" * 45)

    choice = input("  Enter your choice: ")

    # ---------- Option 1 ----------
    if choice == '1':
        print("\n-- Create New Report --")
        names, marks_list = input_students()
        save_to_csv(names, marks_list, 'w')
        print("  New report created and saved to student_results.csv")

    # ---------- Option 2 ----------
    elif choice == '2':
        print("\n-- Add Entries to Existing Report --")
        names, marks_list = input_students()
        save_to_csv(names, marks_list, 'a')
        print("  Entries added to student_results.csv")

    # ---------- Option 3 ----------
    elif choice == '3':
        print("\n-- Report Summary / Analysis --")
        names, marks_list = read_from_csv()
        display_summary(names, marks_list)

    # ---------- Option 4 ----------
    elif choice == '4':
        print("\n-- Display Entries / Grade For Each Student --")
        names, marks_list = read_from_csv()
        display_entries(names, marks_list)

    # ---------- Option 5 ----------
    elif choice == '5':
        print("\n  Thank you for using this ANALYZER!")
        print("=" * 45)
        break

    else:
        print("  Invalid choice. Please enter 1 to 5.")
