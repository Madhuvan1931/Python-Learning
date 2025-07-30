# Write a program to detect double space in a string

str = input("Enter String: ")

print(str.find("  "))

if "  " in str:
    print("Double space detected in: ", str)
elif " " in str:
    print("Single space detected in: ", str)
elif "" in str:
    print("No space detected in: ", str)
else:
    print("There is more than 3 spaces in: ", str)