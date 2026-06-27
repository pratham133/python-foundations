# ==========================================
# Program 1 (Creating First Class)
# ==========================================

class Student:
    pass


# ==========================================
# Program 2 (Creating First Object)
# ==========================================

student1 = Student()


# ==========================================
# Program 3 (Constructor __init__)
# ==========================================

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age 
        self.course = course

student1 = Student("Pratham", 21, "Python")


# ==========================================
# Program 4 (Accessing Object Attributes)
# ==========================================

print(f"Name: {student1.name}")
print(f"Age: {student1.age}")
print(f"Course: {student1.course}")


# ==========================================
# Program 5 (Methods)
# ==========================================

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

student1 = Student("pratham", 22, "Python")
student2 = Student("Swati", 19, "Data Analsyt")

student1.display_details()

student2.display_details()