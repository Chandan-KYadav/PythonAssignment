# Create four variables in a python script and assign values of different data types to them. Write a Python script to print values, data type and if of each variable. 

# Variable decleration
var1 = 35
var2 = True
var3 = "MySirG"
var4 = 5.46

# Data Type
datatype_of_var1 = type(var1)
datatype_of_var2 = type(var2)
datatype_of_var3 = type(var3)
datatype_of_var4 = type(var4)

# Id
id_of_var1 = id(var1)
id_of_var2 = id(var2)
id_of_var3 = id(var3)
id_of_var4 = id(var4)

# Print Values, Data Type and Id

print(f'Variable1 = {var1}, Data Type = {datatype_of_var1} and Id = {id_of_var1}')
print(f'Variable2 = {var2}, Data Type = {datatype_of_var2} and Id = {id_of_var2}')
print(f'Variable3 = {var3}, Data Type = {datatype_of_var3} and Id = {id_of_var3}')
print(f'Variable4 = {var4}, Data Type = {datatype_of_var4} and Id = {id_of_var4}')