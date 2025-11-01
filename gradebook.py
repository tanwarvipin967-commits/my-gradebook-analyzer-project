# Name: Vipin Tanwar
# Date: 31 october 2025
# Title: Analyze student marks without using built-in functions
             
def calculate_average(marks_dict):
    total = 0
    count = 0
    for name in marks_dict:
        total = total + marks_dict[name]
        count = count + 1
    avg = total / count
    return avg


def calculate_median(marks_dict):
    marks = []
    for name in marks_dict:
        marks.append(marks_dict[name])

    n = len(marks)
    for i in range(n):
        for j in range(0, n - i - 1):
            if marks[j] > marks[j + 1]:
                temp = marks[j]
                marks[j] = marks[j + 1]
                marks[j + 1] = temp

    if n % 2 == 0:
        mid1 = marks[n // 2 - 1]
        mid2 = marks[n // 2]
        median = (mid1 + mid2) / 2
    else:
        median = marks[n // 2]
    return median


def find_max_score(marks_dict):
    first = True
    for name in marks_dict:
        if first:
            max_score = marks_dict[name]
            first = False
        else:
            if marks_dict[name] > max_score:
                max_score = marks_dict[name]
    return max_score


def find_min_score(marks_dict):
    first = True
    for name in marks_dict:
        if first:
            min_score = marks_dict[name]
            first = False
        else:
            if marks_dict[name] < min_score:
                min_score = marks_dict[name]
    return min_score

def assign_grades(marks_dict):
    grades = {}
    for name in marks_dict:
        score = marks_dict[name]
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades


def get_pass_fail_lists(marks_dict):
    passed = []
    failed = []
    for name in marks_dict:
        if marks_dict[name] >= 40:
            passed.append(name)
        else:
            failed.append(name)
    return passed, failed


def manual_entry():
    marks = {}
    n = int(input("Enter number of students: "))
    i = 0
    while i < n:
        name = input("Enter student name: ")
        score = int(input("Enter marks for " + name + ": "))
        marks[name] = score
        i = i + 1
    return marks


def print_results_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("-" * 30)
    for name in marks:
        print(f"{name:<15}{marks[name]:<10}{grades[name]}")
    print("-" * 30)


def main(): 
    
    print("==============================================")
    print("     WELCOME TO GRADEBOOK ANALYZER SYSTEM     ")
    print("==============================================")
    
    marks = manual_entry()

    avg = calculate_average(marks)
    median = calculate_median(marks)
    max_score = find_max_score(marks)
    min_score = find_min_score(marks)

    print("\n📊 --- Analysis Summary ---")
    print("Average Marks:", round(avg, 2))
    print("Median Marks:", median)
    print("Highest Marks:", max_score)
    print("Lowest Marks:", min_score)

    grades = assign_grades(marks)
    passed, failed = get_pass_fail_lists(marks)

    print(f"\n✅ Passed Students ({len(passed)}): {', '.join(passed)}")
    print(f"❌ Failed Students ({len(failed)}): {', '.join(failed)}")

    print_results_table(marks, grades)

    print("\n📈 --- Grade Distribution ---")
    grade_letters = ["A", "B", "C", "D", "F"]
    for letter in grade_letters:
        count = 0
        for name in grades:
            if grades[name] == letter:
                count = count + 1
        print(letter, ":", count)

while True:
    main()
    again = input("\nDo you want to analyze again? (y/n): ")
    if again.lower() != "y":
        print("\nThank you for using GradeBook Analyzer! ")
        break
