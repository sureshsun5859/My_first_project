# print(print("hello"))

# x = print("hello")

# print(x)
#my understand by default print will will retrun NONE after print the value. if we want change thiw we cando

def my_print(*arg):
    print(arg)
    return 0

result = my_print("Hello")

print(result)