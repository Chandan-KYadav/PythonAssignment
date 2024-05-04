# Write a python program to check wheather a given number is positive, negative and zero using match case statement. 

num = -6
text = ""

if num == 0 :
    text = "Zero"
elif num > 0 :
    text = "Positive"
else :
    text = "Negative"
    
match(text):
    case "Zero":
        print("Number is Zero")
    case "Positive":
        print("Number is positive")
    case "Negative":
        print("Number is Negative")