# Check that a tuple type cannot be changed in python

# Create a tuple
my_tuple = (10, 20, 30, 40)

# Display the tuple
print("Original Tuple:", my_tuple)

# Try to modify the tuple (this will cause an error)

my_tuple[1] = 50 #TypeError: 'tuple' object does not support item assignment

