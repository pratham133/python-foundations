# ==========================================
# Program 1 (Basic Polymorphism)
# ==========================================

class Dog:

    def speak(self):
        print("woof!")

class Cat:

    def speak(self):
        print("Meow!")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


# ==========================================
# Program 2 (One Function, Different Objects)
# ==========================================

class Dog():

    def speak(self):
        print("woof!")
    
class Cat():

    def speak(self):
        print("Meow!")

def animal_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)


# ==========================================
# Program 3 (Polymorphism with Inheritance)
# ==========================================

class Person:

    def introduce(self):
        print("I am a person.")

class Student(Person):

    def introduce(self):
        print("I am a student.")

class Teacher(Person):

    def introduce(self):
        print("I am a teacher.")

class Doctor(Person):
    print("I am a doctor.")

def introduce_person(person):
    person.introduce()

student = Student()
teacher = Teacher()
doctor = Doctor()

introduce_person(student)
introduce_person(teacher)
introduce_person(doctor)


# ==========================================
# Program 4 (Duck Typing)
# ==========================================

class Dog():

    def speak(self):
        print("Woof!")

class Robot():

    def speak(self):
        print("Beep Boop!")

class Baby():

    def speak(self):
        print("Goo Goo!")

def make_sound(obj):
    obj.speak()

dog = Dog()
robot = Robot()
baby = Baby()

make_sound(dog)
make_sound(robot)
make_sound(baby)
