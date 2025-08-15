# A tuple is an immutable data type in python

# Tuple creation
a = (1, 45, 342, 3456, False, 45, "Madhuvan", "Shivam", "Singh")

# Print the tuple
print("Tuple:", a)

# TUPLE Methods
print("\nTuple Methods")

# count() method: Counts the occurrences of a specific value in the tuple
no = a.count(45)
print("Count of 45 in tuple:", no)

# index() method: Finds the index of the first occurrence of a specific value
index = a.index(45)  # Returns the index of the first '45'
print("Index of first occurrence of 45:", index)

# len() function: Returns the total number of elements in the tuple
length = len(a)
print("Length of tuple:", length)

# max() function: Finds the maximum value in a tuple (only works for numeric tuples)
numeric_tuple = (1, 342, 3456, 45)  # Example numeric tuple
maximum_value = max(numeric_tuple)
print("Maximum value in numeric tuple:", maximum_value)

# min() function: Finds the minimum value in a tuple (only works for numeric tuples)
minimum_value = min(numeric_tuple)
print("Minimum value in numeric tuple:", minimum_value)

# Tuple slicing: Demonstrates how to access a slice of the tuple
slice_a = a[1:5]  # Slices from index 1 to index 4
print("Slice of tuple from index 1 to 4:", slice_a)

# tuple() function: Converts a list into a tuple
sample_list = [10, 20, 30]
converted_tuple = tuple(sample_list)
print("Converted tuple from list:", converted_tuple)

# Example of membership test: Checks if an element exists in the tuple
is_present = "Madhuvan" in a
print("'Madhuvan' in tuple:", is_present)

# Example of concatenation: Joining two tuples
b = ("Python", "Programming")
concatenated_tuple = a + b
print("Concatenated tuple:", concatenated_tuple)

# Example of repetition: Repeating a tuple
repeated_tuple = b * 3
print("Repeated tuple:", repeated_tuple)
