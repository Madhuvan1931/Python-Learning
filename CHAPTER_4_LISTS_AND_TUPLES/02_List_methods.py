list = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
l1 = [1,8,7,2,21,15] 
l2 = [1,8,7,2,21,15]
l3 = [1,8,7,2,21,15]

print(list)
print(l1)

# List Methods 
# Lists are Mutable 
print("List Methods")

list.append("Neeraj") # inserts the element into list
print(list)

# .sort() - works with only same data type
l1.sort() # updates the list to [1,2,7,8,15,21] 
print(l1)

l2.reverse() # updates the list to [15,21,2,7,8,1] 
print(l2)

l1.append(8) # adds 8 at the end of the list
print(l1)

l3.insert(3,8) # This will add 8 at 3 index 
print(l3)

print(l3.pop(2)) # Will delete element at index 2 and return its value.
print(l3)

l3.remove(21) # Will remove 21 from the list.
print(l3)