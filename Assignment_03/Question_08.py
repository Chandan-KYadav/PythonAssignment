# Write a python script to storea hexdecimal number 2F in a variable and print it in octal format. 

hexValue = '0x2F'

# Firstly Convert into decimal or int

hexToDecimal = int(hexValue,0)

print(hexToDecimal)

print(type(hexToDecimal))


#

decimalToOctal = oct(hexToDecimal)

print(f'Octal value {decimalToOctal}  and its type {type(decimalToOctal)}')