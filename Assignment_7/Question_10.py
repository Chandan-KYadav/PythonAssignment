# Write a program to display day name on the basis of user's liking of a colour. ask user for his favorite colour. User can answer in a sentence like " I like red colour". Assuring all colour name entered by user in lowercase. Use match case to display day name associated with the colour. 
text1 = """user's liking of a colour. ask user for his favorite colour. User can answer in a sentence like "I like red colour". Assuring all colour name entered by user in lowercase."""

text2 = """ 
a. Yellow : Monday
b. Blue : Tuesday
c. Orange : Wednesday
d. White : Thursday
e. Black : Friday
f. Red : Saturday
g. All other colours : Sunday
"""
string = input(text1) 
colour = ""

if("yellow" in string):
    colour = "yellow"
elif("blue" in string):
    colour = "blue"
elif("orange" in string):
    colour = "orange"
elif("white" in string):
    colour = "white"
elif("black" in string):
    colour = "black"
elif("red" in string):
    colour = "red"
else:
    colour = "other"
    

match(colour):
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thursday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case "other":
        print("Sunday")
