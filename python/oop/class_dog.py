class Dog:
    species = "Canis lupus familiaris"  # Class attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age > 0:
            self.age = age
        else:
            raise ValueError("Age cannot be negative.")

    # creating an object from class Dog
dog1 = Dog("Buddy", "Three ")
print(dog1)
print(dog1.bark())
print(f"{dog1.name} is {dog1.age} years old.")
print(dog1.species)

print(f"{dog1.name} is {dog1.get_age()} years old.")

dog2 = Dog("Max", "five")
print(dog2.bark())
print(f"{dog2.name} is {dog2.get_age()} years old.")
# print(f"set age of {dog2.name} to 6")
dog2.set_age(0)
print(f"{dog2.name} is now {dog2.get_age()} years old.")