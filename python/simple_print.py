print("hello world")

a = 100
b = 100.100
c = "suresh"
d = 3+4j
e = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print()

my_list = [1,2,3,4,5, "suresh", 100, 100.100, True, [20, 30, 40],(1234, 5678), {1,2,3,1}, {"name":"suresh", "age":30}]
print(my_list)
print(type(my_list))
print(  my_list[5], my_list[6], my_list[7], my_list[8])
print(  my_list[9][2])
print(  my_list[10][1])
print(  my_list[11]) # you can not access set values by index also duplicate values are not allowed in set
print(  my_list[12]["name"])

print(type((1,2,3)))


import math 
number = 16
print(int(math.sqrt(number)))