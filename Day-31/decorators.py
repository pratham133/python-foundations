# ==========================================
# Program 1 (Functions are Objects)
# ==========================================

def greet():

    print("Hello Buddy!")

say_hello = greet

say_hello()


# ==========================================
# Program 2 (Passing Function as Argument)
# ==========================================

def greet():

    print("Hello new function!")

def execute(function):

    function()

execute(greet)


# ==========================================
# Program 3 (Returning a Function)
# ==========================================

def greet():

    print("Hello Buddy!")

def outer():

    return greet

returned_function = outer()

returned_function()


# ==========================================
# Program 4 (Our First Decorator)
# ==========================================

def decorator(function):

    def wrapper():

        print("Before Function")

        function()

        print("After Function")

    return wrapper

def greet():

    print("Hello Buddy!")

greet = decorator(greet)

greet()


# ==========================================
# Program 5 (Using @decorator)
# ==========================================

def decorator(function):

    def wrapper():

        print("Before Function")

        function()

        print("After Function")

    return wrapper

@decorator
def greet():

    print("Hello Buddy! This is advance Python.")

greet()


# ==========================================
# Program 6 (Decorator Problem)
# ==========================================

# def decorator(function):

#     def wrapper():

#         print("Before Function")

#         function()

#         print("After Function")

#     return wrapper


# @decorator
# def greet(name):

#     print(f"Hello {name}")


# greet("Pratham")


# ==========================================
# Program 7 (Decorator with *args)
# ==========================================

def decorator(function):

    def wrapper(*args):

        print("Before Function")

        function(*args)

        print("After Function")

    return wrapper

@decorator
def greet(name):
    
    print(f"Hello {name}")

greet("Pratham")


# ==========================================
# Program 8 (Decorator with **kwargs)
# ==========================================

def decorator(function):

    def wrapper(**kwargs):

        print("Before Function")

        function(**kwargs)

        print("After function")

    return wrapper

@decorator
def student(name, age):

    print(f"Name : {name}")

    print(f"Age : {age}")

student(name="Pratham", age=22)