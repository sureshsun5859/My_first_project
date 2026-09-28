# list = list(range(1, 11))

# print(list)

# list = list(range))

# print(list)

# help(range)

a = 10

print(f"printing the type of object a: {type(a)}")

print(f"printing the memory location of object a: {id(a)}")

print(f"printing the hexadecimal memory location of object a: {hex(id(a))}")

print(isinstance(a, object)) #proof of is that "a" is object of class int 

# let me create some array 

my_list =[10, "suresh", "chennai", "data Engineer", 100000]

# print the list values
print(f"printing the values of my_list: {my_list}")

print(f"printing the type of object my_list: {type(my_list)}")

print(f"printing the memory location of object my_list: {id(my_list)}")

print(f"printing the hexadecimal memory location of object my_list: {hex(id(my_list))}")

print(isinstance(my_list, object)) #proof of is that "my_list" is object of class list

# print the merory location of each element in the list
for i, element in enumerate(my_list):
    print(f"Element {i}: {element}, Type: {type(element)}, Memory Location: {id(element)}, Hexadecimal Memory Location: {hex(id(element))}")

# print how many bytes of memory is used by the list object
import sys
print(f"Memory size of my_list object: {sys.getsizeof(my_list)} bytes")

#print the memory size of each element in the list
for i, element in enumerate(my_list):
    print(f"Element {i}: {element}, Memory Size: {sys.getsizeof(element)} bytes")

# Element 0: 10, Memory Size: 28 bytes
# Element 1: suresh, Memory Size: 47 bytes  
# # here suresh we can store in 6 bytes(6 characters * 1 byte) but python is using 47 bytes because python is using unicode to store the string
#  and also it is storing some additional information like length of the string, hash value, etc.
# object/type information
# string length
# Unicode representation details
# null terminator
# alignment/padding
# Element 2: chennai, Memory Size: 48 bytes
# Element 3: data Engineer, Memory Size: 54 bytes
# Element 4: 100000, Memory Size: 28 bytes

text = "suresh"

print(f"printing the values of text: {text}")

print(f"printing the type of object text: {type(text)}")

print(f"printing the memory location of object text: {id(text)}")

print(f"printing the hexadecimal memory location of object text: {hex(id(text))}")

print(f"memory size of text object: {sys.getsizeof(text)} bytes")

print(my_list[1] == text)  # True: same value
print(my_list[1] is text)  # May be True: same object

print(id(my_list[1])) # Memory location of the string in the list
print(id(text))  # Memory location of the string variable

# estimate the list's allocated and reserved reference slots
import struct

empty_list_size = sys.getsizeof([])
pointer_size = struct.calcsize("P")

print(f"\n Empty list size: {empty_list_size} bytes")
print(f"\n Pointer size: {pointer_size} bytes")

allocated_slots = (
    sys.getsizeof(my_list) - empty_list_size
) // pointer_size

reserved_slots = allocated_slots - len(my_list)

print(f"Used slots: {len(my_list)}")
print(f"Allocated slots: {allocated_slots}")
print(f"Reserved slots: {reserved_slots}")
print(f"Reserved bytes: {reserved_slots * pointer_size}")

# observe how list capacity grows as elements are appended
items = []
previous_size = sys.getsizeof(items)

print(f"Initial size: {previous_size} bytes")

for number in range(20):
    items.append(number)
    current_size = sys.getsizeof(items)
    print(f"\n Appended {number}: size={current_size} bytes")
    if current_size != previous_size:
        print(
            f"length={len(items)}, "
            f"memory={current_size} bytes"
        )
        previous_size = current_size