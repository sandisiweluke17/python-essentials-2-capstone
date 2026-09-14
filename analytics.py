def filter_students(students, predicate):
    """
    Generator: yields students one at a time that match a condition.
    'predicate' is a function like has_passed, so this stays reusable.
    """
    for student in students:
        if predicate(student):
            yield student


def make_grader(pass_mark):
    """
    Closure: returns a function that remembers 'pass_mark' even after
    make_grader has finished running.
    """
    def grade(student):
        return "Pass" if student.score >= pass_mark else "Fail"
    return grade


def calculate_average(students):
    """Returns the average score, or 0 if there are no students."""
    if not students:
        return 0
    return sum(s.score for s in students) / len(students)


def count_pass_fail(students):
    """Returns a tuple: (number who passed, number who failed)."""
    passed = sum(1 for s in students if s.has_passed())
    failed = len(students) - passed
    return passed, failed


def find_top_student(students):
    """Returns the student with the highest score, or None if empty."""
    if not students:
        return None
    return max(students, key=lambda s: s.score)