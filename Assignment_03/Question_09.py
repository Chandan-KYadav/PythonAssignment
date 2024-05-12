# Write a python script to store an octal number 125 in variable and print it in a binary format. 

octalNumber = '0o125'

octalToDecimal = int(octalNumber, 0)

print(octalToDecimal)
print(type(octalToDecimal))


decimalToBinary = bin(octalToDecimal)
print(decimalToBinary)
print(type(decimalToBinary)) 