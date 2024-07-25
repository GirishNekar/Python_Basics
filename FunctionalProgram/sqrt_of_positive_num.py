
'''

@Author: Girish
@Date: 2024-07-23 
@Last Modified by: Girish
@Last Modified time: 2024-07-23 
@Title : Finding Square root of a number 

'''

def calculate_square_root(number,t):
    
    
    """
    
    Description:
        finds the square root of a number  
    Parameter:
        number: for which square root needed to to be found
        t : threshold value
    Return:
        returns Square root of a positive number 

    """
    
    
    if number < 0:
        return "Invalid input"
    
    
    guess = number / 2.0
    
    
    while abs(guess * guess - number) > t:
         
        guess = (guess + number / guess) / 2.0
    
    return guess

number = int(input("enter the number to find the square root")) 
square_root = calculate_square_root(number,t = 1e-15)
print(square_root)
