class Apple:
    #constructor
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    # dunder methods
    def __str__(self):
        return "An apple which is {} and {}".format(self.color, self.flavor)

    def __repr__(self):
        return "Apple(color={!r}, flavor={!r})".format(self.color, self.flavor)

    def __eq__(self, other):
        if not isinstance(other, Apple):
            return NotImplemented
        return self.color == other.color and self.flavor == other.flavor

honeycrisp = Apple("red", "sweet")
print(honeycrisp.color)

print(honeycrisp)
print(repr(honeycrisp))

apple2 = Apple("red", "sweet")
print(honeycrisp == apple2) #True because __eq__ method is defined

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def __add__(self, other):
        return self.area() + other.area()

triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("The area of triangle 1 is", triangle1.area())
print("The area of triangle 2 is", triangle2.area())
print("The area of both triangles is", triangle1 + triangle2)