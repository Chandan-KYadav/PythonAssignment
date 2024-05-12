# Write a python script to check wheather two given strings are identical, first string comes before the second string in dictionary order or the string comes after the second string in dictionary order using match case statement. 

string1 = input(" Enter string 1 ")
string2 = input(" Enter string 2 ")
output = 0

if(string1 == string2):
    output = 1
elif(string1 > string2):
    output = 2
elif(string1 < string2):
    output = 3
else: 
    output = 0
    
match(output):
    case 0:
        print("Invalid")
    case 1:
        print("Identical")
    case 2:
        print("String first is greater")
    case 3:
        print("String 2 is greater")
        