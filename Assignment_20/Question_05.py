# Write a python string to create function to find the Min of three number. 

def min_number (*args):
    min_value = min(args)
    return min_value

# Driver Code 

value = (50, 70, 30)

minimum_value = min(value)

print(f"{minimum_value} is minimum value.")