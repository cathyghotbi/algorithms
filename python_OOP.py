# Import ABC (Abstract Base Class) and abstractmethod
# ABC allows us to create abstract classes
from abc import ABC, abstractmethod


# Create an abstract base class named Shape
class Shape(ABC):

    # Constructor to initialize shape name
    def __init__(self, name):
        # Store the name of the shape
        self.name = name

    # Abstract method (must be implemented in child classes) - We force child classes to implement area() using abstractmethod
    @abstractmethod
    def area(self):
        # This method does not have implementation here
        # Child classes MUST override this method
        pass

    # Normal method shared by all shapes
    def describe(self):
        # Print the name of the shape
        print(f"This is a {self.name}.")


# Create a Rectangle class that inherits from Shape
class Rectangle(Shape):

    # Constructor for Rectangle
    def __init__(self, width, height):
        # Call parent constructor using super()
        super().__init__("Rectangle")

        # Store width
        self.width = width

        # Store height
        self.height = height

    # Override the abstract method area()
    def area(self):
        # Calculate and return area of rectangle
        return self.width * self.height


# Create a Circle class that inherits from Shape
class Circle(Shape):

    # Constructor for Circle
    def __init__(self, radius):
        # Call parent constructor
        super().__init__("Circle")

        # Store radius
        self.radius = radius

    # Override the abstract method area()
    def area(self):
        # Import math module for pi
        import math

        # Calculate and return area of circle
        return math.pi * self.radius ** 2


# Create a Triangle class that inherits from Shape
class Triangle(Shape):

    # Constructor for Triangle
    def __init__(self, base, height):
        # Call parent constructor
        super().__init__("Triangle")

        # Store base
        self.base = base

        # Store height
        self.height = height

    # Override the abstract method area()
    def area(self):
        # Calculate and return area of triangle
        return 0.5 * self.base * self.height


# --------- POLYMORPHISM DEMONSTRATION ---------

# Create objects of different shape types
shapes = [
    Rectangle(10, 5),
    Circle(7),
    Triangle(6, 4)
]

# Loop through each shape object
for shape in shapes:
    # Call describe() method (same method for all)
    shape.describe()

    # Call area() method (different behavior for each class) - Same method name → Different behavior (Polymorphism)
    print(f"Area: {shape.area()}")

    # Print separator line
    print("-" * 30)


# Output in PyCharm Terminal:
# This is a Rectangle.
# Area: 50
# ------------------------------
# This is a Circle.
# Area: 153.93804002589985
# ------------------------------
# This is a Triangle.
# Area: 12.0
# ------------------------------

# Process finished with exit code 0
