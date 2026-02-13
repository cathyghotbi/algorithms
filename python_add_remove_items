from collections.abc import Iterable

class Garden:
    def __init__(self, area):
        self.area = area
        self.fruits = []
        self.flowers = []


    def add_fruits(self, fruits):
        if isinstance(fruits, str):
            self.fruits.append(fruits) 
        elif isinstance(fruits, Iterable):
            self.fruits.extend(fruits)

    def add_flowers(self, *flowers):
        self.flowers.extend(flowers)

    def remove_fruits(self, fruit):
        if fruit in self.fruits: # Nested lists cause membership issues (in won't search inside inner lists)
            self.fruits.remove(fruit)

    def remove_flowers(self, flower):
        self.flowers.remove(flower)

    def __str__(self):   # overriding print for this class >  controls what is returned when the object is printed
        return f"Garden has: {self.fruits} and {self.flowers}"



g1 = Garden(58)
g1.add_fruits(['apple', 'banana', 'kiwi'])
g1.add_fruits('orange')
g1.add_fruits('strawberry')
g1.add_fruits('mango')

g1.add_flowers('rose', 'lilly', 'sunflower')
g1.add_flowers('tulip')
new_flowers = ['calendula', 'daisy']
g1.add_flowers(*new_flowers)
print(g1)

g1.remove_fruits('kiwi')
g1.remove_fruits('mango')
g1.remove_flowers('lilly')
g1.remove_flowers('daisy')
print(g1)


# Garden has: ['apple', 'banana', 'kiwi', 'orange', 'strawberry', 'mango'] and ['rose', 'lilly', 'sunflower', 'tulip', 'calendula', 'daisy']
# Garden has: ['apple', 'banana', 'orange', 'strawberry'] and ['rose', 'sunflower', 'tulip', 'calendula']

# Key Concepts in this example:
# - append() → adds one item
# - extend() → adds multiple items from iterable
# - __str__() must return, not print
# - Nested lists cause membership issues (in won't search inside inner lists)
# - *args (Variable Positional Arguments),
#  - Collects multiple arguments into a tuple
#  - Allows flexible calls
# - use * to unpacks list into separate arguments
# - list does not prevent duplicates (for improvement)
