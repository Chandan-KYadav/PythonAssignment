# Write a program to take user's age and display the category of person. Age below 10 years -Kid, age below 20 - Teen, age below 40 - young, age below 60 - experienced and age above or equal to 60 - senior citizen.

text = "Enter your age "

age = int(input(text))
value = 0 

if(age < 10):
    value = 10
elif(age > 10 and age < 20):
    value = 20
elif(age > 20 and age < 40):
    value = 40
elif(age > 40 and age < 60):
    value = 60
else:
    value = 1    

match(value):
    case 10:
        print("Kid")
    case 20:
        print("Teen")
    case 40:
        print("Young")
    case 60:
        print("Experienced")
    case 1:
        print("Senier citizen")
        
        