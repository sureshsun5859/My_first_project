"""A guided tour of Python for loops.

Run this file from the project root:
    python python/for_loop_deep_dive.py

Read and run one section at a time while learning.
"""


# 1. The basic idea: visit every item in an iterable.
print("\n1. Basic iteration")
for item in ["Python", "SQL", "Spark"]:
    print("Learning:", item)

for character in "loop":
    print("Character:", character)


# 2. range(): start is included, stop is excluded, and step is optional.
print("\n2. range()")
for number in range(5):
    print(number, end=" ")
print()

for number in range(2, 11, 2):
    print(number, end=" ")
print()

for number in range(10, 0, -1):
    print(number, end=" ")
print()


# 3. Conditions inside a loop.
print("\n3. Conditions")
for number in range(1, 11):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


# 4. Accumulation: build a result while visiting items.
print("\n4. Accumulation")
numbers = [12, 7, 18, 3, 20, 5]
total = 0
largest = numbers[0]

for number in numbers:
    total += number
    if number > largest:
        largest = number

print("Total:", total)
print("Largest:", largest)


# 5. break stops the loop; continue skips the current iteration.
print("\n5. break and continue")
for number in range(1, 11):
    if number == 4:
        continue
    if number == 8:
        break
    print(number)


# 6. enumerate() gives both the position and the item.
print("\n6. enumerate()")
fruits = ["apple", "banana", "orange"]
for position, fruit in enumerate(fruits, start=1):
    print(position, fruit)


# 7. zip() combines related sequences. It stops at the shortest sequence.
print("\n7. zip()")
names = ["Alice", "Bob", "Charlie"]
scores = [91, 84, 96]

for name, score in zip(names, scores):
    result = "pass" if score >= 60 else "fail"
    print(name, score, result)


# 8. Dictionaries: keys, values, and key-value pairs.
print("\n8. Dictionaries")
student = {"name": "Alice", "age": 25, "grade": "A"}

for key in student:
    print("Key:", key)

for value in student.values():
    print("Value:", value)

for key, value in student.items():
    print(key, "=", value)


# 9. Unpacking structured data while looping.
print("\n9. Unpacking")
coordinates = [(10, 20), (30, 40), (50, 60)]
for x_coordinate, y_coordinate in coordinates:
    print("x:", x_coordinate, "y:", y_coordinate)


# 10. for...else: else runs only when break was not used.
print("\n10. for...else")
search_value = 13
search_numbers = [2, 4, 6, 8, 10]

for number in search_numbers:
    if number == search_value:
        print("Found", search_value)
        break
else:
    print(search_value, "was not found")


# 11. Nested loops: useful for grids and combinations.
print("\n11. Nested loops")
for row in range(1, 4):
    for column in range(1, 4):
        print(f"({row}, {column})", end=" ")
    print()

print("Multiplication table")
for first_number in range(1, 4):
    for second_number in range(1, 4):
        print(first_number * second_number, end=" ")
    print()


# 12. List comprehensions: a loop that creates a list.
print("\n12. List comprehensions")
squares = [number ** 2 for number in range(1, 6)]
even_squares = [number ** 2 for number in range(1, 11) if number % 2 == 0]
print("Squares:", squares)
print("Even squares:", even_squares)


# 13. Dictionary and set comprehensions.
print("\n13. Dictionary and set comprehensions")
square_lookup = {number: number ** 2 for number in range(1, 6)}
word_lengths = {word: len(word) for word in ["cat", "python", "database"]}
unique_lengths = {len(word) for word in ["cat", "dog", "horse", "bird"]}
print(square_lookup)
print(word_lengths)
print(unique_lengths)


# 14. Generator expressions: produce one value at a time.
print("\n14. Generator expressions")
squares_generator = (number ** 2 for number in range(1, 6))
for square in squares_generator:
    print(square)


# 15. Files are iterable: one line is visited per iteration.
print("\n15. File iteration")
file_lines = ["name,score", "Alice,91", "Bob,84"]
for line in file_lines:
    name, score = line.split(",")
    print(name, score)

# To loop through a real file, use:
# with open("python/sample_data.csv", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())


# 16. Manual iteration explains how for works internally.
print("\n16. iter() and next()")
iterator = iter(["first", "second", "third"])
print(next(iterator))
print(next(iterator))
print(next(iterator))


# 17. A generator function uses yield and can be consumed by for.
print("\n17. Generator function")
def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1

for number in count_up_to(5):
    print(number)


# 18. Custom iterable: define the iteration protocol yourself.
print("\n18. Custom iterable")
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for number in Countdown(3):
    print(number)


# 19. Sorting during iteration.
print("\n19. sorted() and reversed()")
unsorted_numbers = [5, 2, 9, 1]
for number in sorted(unsorted_numbers):
    print(number, end=" ")
print()

for number in reversed(unsorted_numbers):
    print(number, end=" ")
print()


# 20. Exception handling inside a loop keeps bad input from stopping all work.
print("\n20. try and except")
raw_values = ["10", "20", "not a number", "30"]
for raw_value in raw_values:
    try:
        number = int(raw_value)
    except ValueError:
        print("Skipping invalid value:", raw_value)
    else:
        print("Accepted:", number)


# 21. Practical project example: summarize student records.
print("\n21. Practical summary")
students = [
    {"name": "Alice", "scores": [90, 92, 88]},
    {"name": "Bob", "scores": [70, 75, 72]},
    {"name": "Charlie", "scores": [98, 96, 99]},
]

for student_record in students:
    scores = student_record["scores"]
    average = sum(scores) / len(scores)
    status = "pass" if average >= 60 else "fail"
    print(student_record["name"], "average:", round(average, 2), status)


# 22. Common mistake: do not remove items from the list being visited.
print("\n22. Safe filtering")
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print("Original:", numbers)
print("Filtered:", odd_numbers)


# 23. Quick rules to remember.
print("\n23. Rules")
print("1. for visits items; it does not require numeric data.")
print("2. range(stop) excludes stop.")
print("3. Use enumerate() for position plus value.")
print("4. Use zip() for related sequences.")
print("5. break stops; continue skips; else means no break occurred.")
print("6. Prefer readable loops over clever one-line code.")
