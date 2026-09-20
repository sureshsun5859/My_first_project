"""A practical introduction to Python's built-in data types.

Run this file directly to see each example and its type.
"""


def show_type(name, value):
	"""Print a value together with the type Python assigned to it."""
	print(f"{name:<18} value={value!r:<30} type={type(value).__name__}")


print("1. Basic data types")
integer_number = 42
decimal_number = 3.14
complex_number = 2 + 3j
is_learning = True
nothing = None

show_type("integer", integer_number)
show_type("float", decimal_number)
show_type("complex", complex_number)
show_type("boolean", is_learning)
show_type("None", nothing)

print("\n2. Text data")
message = "Python is fun"
show_type("string", message)
print("uppercase:", message.upper())
print("first character:", message[0])
print("characters 0 to 5:", message[0:6])

print("\n3. Ordered collections")
shopping_list = ["book", "pen", "notebook"]
coordinates = (10, 20)
numbers = range(1, 4)

show_type("list", shopping_list)
show_type("tuple", coordinates)
show_type("range", numbers)
shopping_list.append("bag")
print("list after append:", shopping_list)

print("\n4. Mapping data")
student = {
	"name": "Asha",
	"age": 20,
	"subjects": ["Python", "Math"],
}
show_type("dictionary", student)
print("student name:", student["name"])
print("dictionary keys:", list(student.keys()))

print("\n5. Set data")
unique_numbers = {1, 2, 2, 3, 3}
fixed_unique_numbers = frozenset({1, 2, 3})

show_type("set", unique_numbers)
show_type("frozenset", fixed_unique_numbers)
print("duplicates removed:", sorted(unique_numbers))
print("set union:", unique_numbers | {3, 4, 5})

print("\n6. Binary data")
raw_bytes = b"hello"
editable_bytes = bytearray(b"hello")
view_of_bytes = memoryview(raw_bytes)

show_type("bytes", raw_bytes)
show_type("bytearray", editable_bytes)
show_type("memoryview", view_of_bytes)
editable_bytes[0] = ord("H")
print("bytearray after editing:", editable_bytes)
print("decoded bytes:", raw_bytes.decode("utf-8"))

print("\n7. Mutability")
mutable_list = [1, 2]
mutable_list.append(3)
immutable_tuple = (1, 2)

print("lists are mutable:", mutable_list)
print("tuples are immutable: create a new tuple instead of changing it")
print("tuple with an added value:", immutable_tuple + (3,))

print("\n8. Useful type checks and conversions")
print("is integer_number an int?", isinstance(integer_number, int))
print("is message a string?", isinstance(message, str))
print("int('10'):", int("10"))
print("float('2.5'):", float("2.5"))
print("str(100):", str(100))
print("list('cat'):", list("cat"))
print("set([1, 1, 2]):", set([1, 1, 2]))

print("\nQuick reference")
print("int, float, complex, bool, NoneType")
print("str, list, tuple, range, dict")
print("set, frozenset, bytes, bytearray, memoryview")
