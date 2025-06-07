# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Subclass Student
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

# Subclass Lecturer
class Lecturer(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")

# Subclass Staff
class Staff(Person):
    def __init__(self, name, age, role, shift):
        super().__init__(name, age)
        self.role = role
        self.shift = shift

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")
        print(f"Shift: {self.shift}")

# Example

if __name__ == "__main__":
    print("=== Student ===")
    student = Student("Derrick", 20, "S123", "Computer Science")
    student.display_info()

    print("\n=== Lecturer ===")
    lecturer = Lecturer("Dr. Hallie", 45, "L456", "Engineering")
    lecturer.display_info()

    print("\n=== Staff ===")
    staff = Staff("Suzan", 38, "Technician", "Morning")
    staff.display_info()
