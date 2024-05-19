# Write a python script to create a function to check wheather a string is a panagram or not. 

# Panagram means all alphabhet are present in the string.

def is_panagram (string) :
    alphabhet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    string = str(string)
    string = string.replace(" ", "")
    string = string.lower()
    
    
    for e in alphabhet:
        if e in string:
            count += 1
    
    if count == len(alphabhet):
        return True
    else:
        return False
    
    
# Drive Code 

# text = "The quick brown fox jumps over the lazy dog."
text = "Hello"

if is_panagram(text):
    print('Yes, Is Panagarm')
else:    
    print('No, Not a Panagarm')