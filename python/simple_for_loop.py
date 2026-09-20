
# for variable in iterable:
#     code block

# for i in range(2,5):
#     # print("i value inside the loop:", i)
#     print(i)
# for letter in "Python":
#     print(letter)

# for number in [10, 20, 30]:
#     print(number)

# print("\n1. printing numbers even or odd")
# for number in range(1,10):
#     if number % 2 == 0:
#         print(number, "is even")
#     else:
#         print(number, "is odd")

print("\n2.printing prime numbers")

for number in range(5, 8):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number, "is a prime number")
#     else:
#         print(number, "is not a prime number")

# print("\3. printing number is satisfy condition")
# for number in range(1, 5):
#     if number > 1:
#         print(number, "is greater than 1")

#     else:
#         print(number, "is not greater than 1")