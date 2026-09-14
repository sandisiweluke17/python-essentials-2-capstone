from models import Student, HonoursStudent
from data_tools import generate_sample_data_file, load_and_clean_records, export_results, append_log
from analytics import filter_students, make_grader, calculate_average, count_pass_fail, find_top_student
from reporting import environment_report, date_report

students = []  # holds Student objects once loaded


def print_menu():
    print("\n===== STUDENT ANALYTICS TOOLKIT =====")
    print("1. Generate sample data file")
    print("2. Load & clean records from file")
    print("3. View all students")
    print("4. Analyse (averages, pass/fail, top student)")
    print("5. Filter students (generator)")
    print("6. Grade with a custom pass mark (closure)")
    print("7. Environment & date report")
    print("8. Export results to a file")
    print("9. Exit")


def load_students():
    global students
    records = load_and_clean_records()
    students = [Student(name, sid, score) for name, sid, score in records]
    append_log(f"Loaded {len(students)} students from file.")
    print(f"Loaded {len(students)} students.")


def view_students():
    if not students:
        print("No students loaded yet. Choose option 2 first.")
        return
    for s in students:
        print(s)


def analyse_students():
    if not students:
        print("No students loaded yet. Choose option 2 first.")
        return
    avg = calculate_average(students)
    passed, failed = count_pass_fail(students)
    top = find_top_student(students)
    print(f"Average score: {avg:.2f}")
    print(f"Passed: {passed} | Failed: {failed}")
    print(f"Top student: {top}")


def filter_students_menu():
    if not students:
        print("No students loaded yet. Choose option 2 first.")
        return
    print("Filter by: 1) Passed  2) Failed")
    try:
        choice = int(input("Choose (1-2): "))
        if choice == 1:
            result = filter_students(students, lambda s: s.has_passed())
        elif choice == 2:
            result = filter_students(students, lambda s: not s.has_passed())
        else:
            print("Invalid choice.")
            return
        for s in result:
            print(s)
    except ValueError:
        print("Please enter a number.")


def grade_with_custom_pass_mark():
    if not students:
        print("No students loaded yet. Choose option 2 first.")
        return
    try:
        pass_mark = int(input("Enter custom pass mark: "))
        grader = make_grader(pass_mark)
        for s in students:
            print(f"{s.name}: {grader(s)}")
    except ValueError:
        print("Please enter a number.")


def show_environment_and_date_report():
    print(environment_report())
    target = input("Enter a future date (YYYY-MM-DD) to count days until, or press Enter to skip: ").strip()
    if target:
        print(date_report(target))
    else:
        print(date_report())


def export_report():
    if not students:
        print("No students loaded yet. Choose option 2 first.")
        return
    lines = [str(s) for s in students]
    avg = calculate_average(students)
    passed, failed = count_pass_fail(students)
    top = find_top_student(students)
    content = "\n".join(lines) + f"\n\nAverage: {avg:.2f}\nPassed: {passed} | Failed: {failed}\nTop student: {top}\n"
    path = export_results(content)
    append_log(f"Exported report to {path}.")
    print(f"Report exported to {path}")


def main():
    while True:
        print_menu()
        try:
            choice = int(input("Choose an option (1-9): "))
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue

        if choice == 1:
            path = generate_sample_data_file()
            print(f"Sample data file created at {path}")
        elif choice == 2:
            load_students()
        elif choice == 3:
            view_students()
        elif choice == 4:
            analyse_students()
        elif choice == 5:
            filter_students_menu()
        elif choice == 6:
            grade_with_custom_pass_mark()
        elif choice == 7:
            show_environment_and_date_report()
        elif choice == 8:
            export_report()
        elif choice == 9:
            print("Goodbye!")
            break
        else:
            print("Please choose a number between 1 and 9.")


if __name__ == "__main__":
    main()