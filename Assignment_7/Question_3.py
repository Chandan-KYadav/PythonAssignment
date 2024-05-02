# Write a menu driven program to check isosceles triangle, right angle triangle and equilateral triangle.


program = '''
        1. Check isosceles triangle or not.
        2. Check right-angled triangle or not.
        3. Check equilateral triangle or not.
        4. Exit
        '''
        
match(int(input(program))):
    case 1:
        sideOne = int(input("Enter the first side length of triangle "))
        sideTwo = int(input("Enter the second side length of triangle "))
        sideThree = int(input("Enter the third side length of triangle "))
        
        if(sideOne == sideTwo or sideTwo == sideThree or sideThree == sideOne):
            print("isoceles triangle")
        else:
            print("Not a isoceles triangle")
    case 2:
        sideOne = int(input("Enter the first side length of triangle "))
        sideTwo = int(input("Enter the second side length of triangle "))
        sideThree = int(input("Enter the third side length of triangle "))
        
        squareOfSideOne = sideOne*sideOne
        squareOfSideTwo = sideTwo*sideTwo
        squareOfSideThree = sideThree*sideThree
        
        if sideOne > sideTwo and sideOne > sideThree :
            if(squareOfSideOne == squareOfSideTwo + squareOfSideThree):
                print("Right-angled triangle")
            else:
                print("Not a right-angle triangle")
        elif sideTwo > sideOne and sideTwo > sideThree :
            if(squareOfSideTwo == squareOfSideOne + squareOfSideThree):
                print("Right-angled triangle")
            else:
                print("Not a right-angle triangle")
        else  :
            if(squareOfSideThree == squareOfSideTwo + squareOfSideOne):
                print("Right-angled triangle")
            else:
                print("Not a right-angle triangle")
            
    case 3:
        sideOne = int(input("Enter the first side length of triangle "))
        sideTwo = int(input("Enter the second side length of triangle "))
        sideThree = int(input("Enter the third side length of triangle "))
        
        if(sideOne == sideTwo and sideTwo == sideThree and sideThree == sideOne):
            print("equilateral  triangle")
        else:
            print("Not a equilateral triangle")
    case 4:
        exit()





        