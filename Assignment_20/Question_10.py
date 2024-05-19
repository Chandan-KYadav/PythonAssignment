# Write a python script to create a function to check wheather a string is a anagram or not. 

# Anagram string
# s1 = 'Listen'
# s2 = 'Silent'

def is_anagram (string1, string2):
    if sorted(string1.lower()) == sorted(string2.lower()):
        print("Yes, Anagram string")
    else:
        print("Not, Anagram string")
        
# Driver Code

# str1 = "Listen"
# str2 = "Silent"

str1 = "Hello"
str2 = "hi"

is_anagram(str1, str2)