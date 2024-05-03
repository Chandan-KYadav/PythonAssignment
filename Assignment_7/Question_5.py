# Write a program which take input from the user. Print Saurabh sukhla if the number is even, Prateek Jain if the number is negative odd number and print aditys choudhary if number is positive odd number. 

text = " Enter even or odd number, number will be positive or negative "
num = int(input(text))

result = ""

if(num % 2 == 0):
    result = "even"
elif(num % 2 != 0 and num < 0):
    result = "negativeOdd"
elif(num % 2 !=0):
    result = "odd"
else:
    print("Invalid")
    
match(result):
    case "":
        print("Invalid Text")
    case "even":
        print("Sourabh Sukla")
    case "negativeOdd":
        print("Prateek jain")
    case "odd":
        print("Aditya Choudhary")
        