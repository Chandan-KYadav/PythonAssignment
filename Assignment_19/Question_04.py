# Write a python program to create a function which expects kwargs arguments. 

def display (**kwargs):
    for key, value in kwargs.items():
        print("{} is {}".format(key,value))
    
display(firstName = "Chandan", middleName = "kumar", lastName = "yadav")