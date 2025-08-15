# Write a program to accept marks of 6 students and display them in a sorted manner. 

Marks = []

f1 = int(input("Enter Marks 1:  "))
Marks.append(f1)
f2 = int(input("Enter Marks 2:  "))
Marks.append(f2)
f3 = int(input("Enter Marks 3:  "))
Marks.append(f3)
f4 = int(input("Enter Marks 4:  "))
Marks.append(f4)
f5 = int(input("Enter Marks 5:  "))
Marks.append(f5)
f6 = int(input("Enter Marks 6:  "))
Marks.append(f6)


print("List of Marks: ", Marks)
Marks.sort()
print("Sorted Marks: ", Marks)