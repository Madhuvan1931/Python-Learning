# Write a program to fill in a letter template given below with name and date. 

letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 

letter = letter.replace("<|Name|>", "Madhuvan Singh").replace("<|Date|>", "01-12-2024")


print(letter)