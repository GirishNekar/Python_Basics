'''

@Author: Girish
@Date: 2024-07-22 
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 
@Title : finding harmonic of given number

'''


def harmonic(num):
    """
    
    Description:
        Used to calulate the harmonic of the number 
    Parameter:
        num: parameter used to limit the calculation of the harmonic 
    Return:
        returns harmonic value

"""
    
    harm = 0
    for number_to_iterate in range(1,num+1):
        harm = harm + (1/number_to_iterate)
    return harm

num = int(input("enter the number to find the harmonic(should be grater than 0) \n"))
print(harmonic(num))