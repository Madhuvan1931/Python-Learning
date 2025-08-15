# A tuple is an immutable data type in python.

a = (1, 2, 3, 5, 7)

print(type(a))

# a[0] = 4 'tuple' object does not support item assignment

print(a[0])

print(a)

b = () # empty tuple 
c = (1,) # tuple with only one element needs a comma 
d = (1,7,2) # tuple with more than one element 

print(b)
print(c)
print(d)

# tuple with different data type
x = (1, 4.56, "Hello", 5, "Bye")
print(type(x))
print(x[2][1:4])