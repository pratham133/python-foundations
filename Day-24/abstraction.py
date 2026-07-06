# ==========================================
# Program 1 (Creating an Abstract Class)
# ==========================================

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        print("Woof!")

dog = Dog()

dog.speak()


# # ==========================================
# # Program 2 (Missing Abstract Method)
# # ==========================================

# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def speak(self):
#         pass

# class Dog(Animal):
#     pass

# dog = Dog()


# ==========================================
# Program 3 (Multiple Child Classes)
# ==========================================

from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        print("Woof!")

class Cat(Animal):

    def speak(self):
        print("Meoww!")

class Cow(Animal):

    def speak(self):
        print("Moooo!")

class Lion(Animal):

    def speak(self):
        print("Rooar!")

dog = Dog()
cat = Cat()
cow = Cow()
lion = Lion()

dog.speak()
cat.speak()
cow.speak()
lion.speak()


# =========================================================
# Program 4 (Real-Life Example of Multiple Child Classes)
# =========================================================

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")

class UPI(Payment):

    def pay(self):
        print("Paid using UPI")

class PayPal(Payment):
    
    def pay(self):
        print("Paid using PayPal")

creditcard = CreditCard()
upi = UPI()
paypal = PayPal()

creditcard.pay()
upi.pay()
paypal.pay()


# ==========================================
# Program 5 (Abstraction + Polymorphism)
# =========================================

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        print("Woof!")

class Cat(Animal):

    def speak(self):
        print("Meoww!")

def animal_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)