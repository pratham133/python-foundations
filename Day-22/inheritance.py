# ==========================================
# Program 1 (Parent Class)
# ==========================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old.")

person1 = Person("Pratham", 22)

person1.introduce()


# ==========================================
# Program 2 (Creating Child Class)
# ==========================================

class Student(Person):
    pass

Student1 = Student("Swati", 19)

Student1.introduce()


# ==========================================
# Program 3 (Adding Child Class Features)
# ==========================================

class Student(Person):

    def study(self):
        print(f"{self.name} is studying Python")

Student1 = Student("Pratham", 22)

Student1.introduce()
Student1.study()


# ==========================================
# Program 4 (Method Overriding)
# ==========================================

class Student(Person):

    def introduce(self):
        print(f"Hi! I'm {self.name}")
        print("I'm a Python stduent.")

student1 = Student("Pratham", 22)

student1.introduce()


# ==========================================
# Program 5 (Using super())
# ==========================================

class Student(Person):

    def introduce(self):
        super().introduce()
        print("I am learning Python.")

student1 = Student("Pratham", 22)

student1.introduce()

# ==========================================
# Program 6 (super() with __init__)
# ==========================================

class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def dispaly_details(self):
        self.introduce()
        print(f"Course: {self.course}")

student1 = Student("Swati", 19, "Data Analyst")

student1.dispaly_details()


# ==========================================
# Program 7 (isinstance() and issubclass())
# ==========================================

# ==========================================
# Program 7 (isinstance() and issubclass())
# ==========================================

class Person:
    pass


class Student(Person):
    pass


student1 = Student()

print(isinstance(student1, Student))
print(isinstance(student1, Person))

print(issubclass(Student, Person))
print(issubclass(Person, Student))