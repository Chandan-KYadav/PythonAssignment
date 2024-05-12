# Write a python program to check wheather a given string is a multiword string or single word string using match case statement.

text = "M"
count = 0 
value = 0

for e in text:
    count+=1
    
if count > 1 :
    value = 1


match(value):
    case 0: 
        print("Single word string")
    case 1:
        print("Multi word string")
    