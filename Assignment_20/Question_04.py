# Write a python program to create a function to check wheather a passed  string is palindrome or not.

def check_palindrome_not (string):
    length = len(string) + 1 
    
    # String comprehension
    reverse_string = string[-1: -(length): -1]
    
    if(string.lower() == reverse_string.lower()):
        return True
    else:
        return False
    

# Drive Code

user_input = input("Enter a String to check Palindrome or not ")

if check_palindrome_not(user_input):
    print(f'{user_input} is Palindrone string.')
else:
    print(f'{user_input} is Not Palindrone string. ')
