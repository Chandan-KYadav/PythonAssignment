# Write a python program to print all items by referring to their index numbers (thelist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"])

thelist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

index = 0

while(index < len(thelist)):
    
    print(f'index[{index}] {thelist[index]}')
    
    index += 1