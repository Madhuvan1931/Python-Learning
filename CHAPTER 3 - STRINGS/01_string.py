
a ='Madhuvan Singh'   # Single quoted string 
b = "Madhuvan Singh"  # Double quoted string 
c = '''Madhuvan Singh'''  # Triple quoted string 

#  String Slicing
print("String Slicing")

name = a[5]

print(name)

print(b[0:8])
print(b[9:14])


# Negative Slicing
print("Negative Slicing")

name = "Madhuvan Singh"
print(name[-5:-1]) # Sing
print(name[1:5]) # adhu

# We can provide a skip value as a part of our slice like this:
print("Slicing by Values")

word = "amazing" 
print(word[1: 6: 2]) # "mzn" 

# Other advanced slicing techniques:
print(word[:7])  # word [0:7] – 'amazing' 
print(word[0:])  # word [0:7] – 'amazing' 

print("String Functions")

print(len(a)) # prints Length of srting

str = "Madhuvan" 
print(str.endswith("van"))  # Output: True 
print(str.startswith("Mad")) #Output: True

count = str.count("a") 
print(count)  # Output: 2 

str1 = "madhuvan"
capitalized_string = str1.capitalize() 
print(capitalized_string)  # Output: "Madhuvan"


#  returns the index of first occurrence of that word in the string
index = str.find("h")
print(index)


#  This function replace the old word with new word in the entire string.
replace_string = str.replace('a', 'U')
print("Replaced Srting: " ,replace_string)

