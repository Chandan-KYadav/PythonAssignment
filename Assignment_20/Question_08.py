# Write a python script to create a function that accepts a string and calculate the number of upper case and number of lower case. 

def calculate_upper_lower (string):
    upperCase = 0
    lowerCase = 0
    specialCharacter = 0
    
    for e in string:
        s = str(e) # S --> e converted to str
        
        if s.isupper():
            upperCase += 1
        elif s.islower():
            lowerCase += 1
        else:
            specialCharacter += 1
            
    return upperCase, lowerCase
        
        
# Drive Code         

text = "Hello, I am learning Python Full Stack Web Development."

result = calculate_upper_lower(text)

print("Number of Upper Case : ", result[0])
print("Number of Lower Case : ", result[1])

         