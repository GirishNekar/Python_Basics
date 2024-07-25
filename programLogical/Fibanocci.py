'''

@Author: Girish
@Date: 2024-07-22 
@Last Modified by: Girish
@Last Modified time: 2021-02-11 
@Title : finding no of randoms to traverse the list of numbers only once

'''
def fibanocci(n):
    """
    
    Description:
        prints the fibanocci series 
    Parameter:
        num: number till where we need fiabnoci series
    Return:
        none, prints fibanocci series 

    """
    
    
    num1 = 0
    num2 = 1
    print(num1,end=" ")
    print(num2,end=" ")
    next_number = num2  
    
 
    while next_number <= n:
        print(next_number, end=" ")
        num1, num2 = num2, next_number
        next_number = num1 + num2


num = int(input("Enter the number till where you need fibanocci series\n"))
fibanocci(num)

