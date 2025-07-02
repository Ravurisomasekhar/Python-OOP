class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        else:
            return "D"


class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, marks):
        student = Student(name, roll_number, int(marks))
        self.students.append(student)

    def display_student(self):
        for student in self.students:
            grade = student.get_grade()
            print(f"Name: {student.name}, Roll Number: {student.roll_number}, Marks: {student.marks}, Grade: {grade}")

    def calculate_average(self):
        total = 0
        for student in self.students:
            total += student.marks
        average = total / len(self.students)
        print(f"Average Marks: {average:.2f}")  

def inp_formt():
    g = GradeBook()
    while True:
        try:
            s = input()
            s = s.strip().split(":")
            if "Add" in s[0]:
                two = s[1].split(",")
                name = two[0].strip()
                roll_number = two[1].strip()
                marks = two[2].strip()
                g.add_student(name, roll_number, marks)
            elif "DisplayStudents" in s[0]:
                g.display_student()
            elif "CalculateAverageMarks" in s[0]:
                g.calculate_average()
        except Exception as e:
            break
inp_formt()