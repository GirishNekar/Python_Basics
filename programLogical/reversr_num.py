'''

@Author: Girish
@Date: 2024-07-23 
@Last Modified by: Girish
@Last Modified time: 2021-02-11 
@Title : reversing a number

'''

def reverse_num(num):
    """
    
    Description:
        reverses the given number 
    Parameter:
        num: number thet is being reversed
    Return:
        returns the reversed number 

    """      
    rev = 0
    while num >= 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev


num = int(input("enter the number to be reversed"))
print(reverse_num(num))