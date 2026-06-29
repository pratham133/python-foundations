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

    def update_age(self, new_age):
        if new_age > 0:
            self.age = new_age
            print("\nAge updated successfully!")
        else:
            print("\nInvalid age! Age must be greater than 0.")


student1 = Student("Pratham", 22, "Python")
student2 = Student("Swati", 19, "Data Analyst")

student1.display_details()

print("-" * 30)

student2.display_details()


# ==========================================
# Program 6 (Updating Object Attributes)
# ==========================================

student1.update_age(23)

print("\nAfter updating age of student1:\n")

student1.display_details()


# ==========================================
# Program 7 (Age validation)
# ==========================================

student1.update_age(-10)

print("\nTrying to update with invalid age:\n")

student1.display_details()