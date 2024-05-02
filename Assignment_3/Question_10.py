# Write a python script to add twwo numbers 25(in octal) and 30 (in hexdecimal) and display the result in binary format. 

hexvalue = '0x39'
octalValue = '0o25'

hexvalueToDecimal = int(hexvalue, 0)

octalValueToDecimal = int(octalValue, 0)

actualValue = hexvalueToDecimal + octalValueToDecimal 

decimalToBinary = bin(actualValue)

print(decimalToBinary)
