# Write a python script to create the list of city names taken from the users. 

cityName = []
index = 0
listLength = int(input("Enter the length of list : "))

while(index < listLength):
    
    userInput = input(f'Enter city {index + 1}: ')
    
    cityName.append(userInput)
    
    index += 1
    
    
print(cityName)