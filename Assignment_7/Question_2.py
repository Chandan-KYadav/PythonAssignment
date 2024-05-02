# Write a menu driven program to perform following operation : Addition, Substraction, Multiplication and division

program = '''
Choose your option below :
         1. Addition
         2. Substraction
         3. Multiplication
         4. Division
         5. Exit
        '''
        
menuDriven = int(input(program))

match menuDriven :
    case 1 :
        print("Enter Two Numbers")
        num1 = int(input("Enter number1 "))
        num2 = int(input("Enter number2 "))
        output = num1 + num2
        print(output)
    case 2 :
        print("Enter Two Numbers")
        num1 = int(input("Enter number1 "))
        num2 = int(input("Enter number2 "))
        output = num1 - num2
        print(output)
    case 3 :
        print("Enter Two Numbers")
        num1 = int(input("Enter number1 "))
        num2 = int(input("Enter number2 "))
        output = num1 * num2
        print(output)
    case 4 :
        print("Enter Two Numbers")
        num1 = int(input("Enter number1 "))
        num2 = int(input("Enter number2 "))
        output = num1 / num2
        print(output)
    case 5 :
        exit()
        