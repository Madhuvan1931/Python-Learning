# Type Function 
print("Type Function")
a = 31  
print(type(a)) # class <int> 

b = "31" 
print(type (b)) # class <str> 

c = "Madhuvan"
print(type (c)) # <class 'str'>

d = True
print(type (d)) # <class 'bool'>

e = None
print(type (e)) # <class 'NoneType'>

f = 3.45
print(type(f)) # <class 'float'>

# Type casting
print("Type Casting")
a = "31" 
b = int(a) # a but  the type should be int
print(type(b))

a = 31.5 
b = str(a) # a but  the type should be string
print(type(b))


# This is invalid
# a = "Madhuvan Singh"
# b = int(a)
# print(type(b))