# Write a python program to create a function that finds a maximum of four numbers. 

def maximum_num (*args):
    return max(args)

max_value = maximum_num(10, 15, 90, 45, 68)
print(max_value)