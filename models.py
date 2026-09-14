class Student:
    """Represents a single student and their score."""

    school_name = "Melsoft Academy"   # class variable — shared by all instances
    total_students = 0                # class variable — counts every Student ever made

    def __init__(self, name, student_id, score):
        self.name = name
        self.student_id = student_id
        self.score = score
        Student.total_students += 1   # increment the shared counter

    def get_grade(self):
        if self.score >= 80:
            return "Distinction"
        elif self.score >= 50:
            return "Pass"
        else:
            return "Fail"

    def has_passed(self):
        return self.score >= 50

    def __str__(self):
        return f"{self.student_id}: {self.name} | Score: {self.score} | Grade: {self.get_grade()}"


class HonoursStudent(Student):
    """A Student who is also doing an honours research project."""

    def __init__(self, name, student_id, score, research_topic):
        super().__init__(name, student_id, score)   # reuse the parent's init
        self.research_topic = research_topic

    def get_grade(self):
        if self.score >= 75:
            return "Distinction (Honours)"
        else:
            return super().get_grade()   # fall back to the normal grading