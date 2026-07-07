# ==================================================
# Program 1 - Vector class with operator overloading
# ==================================================

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
print(v1 == v2)


# ==========================================================
# Program 2 - ComplexNumber class with operator overloading
# ==========================================================

class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __repr__(self):
        return f"{self.real} + {self.imag}i"


# Objects of the ComplexNumber class
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)

# Use overloaded operators
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1 == c2)