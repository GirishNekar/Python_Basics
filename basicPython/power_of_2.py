
'''

@Author: Girish
@Date: 2024-07-22 
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 
@Title : listing numbers which are power of 2

'''


def power_of_2(num1):
    
    mylist = [] ## created empty list
    """
    
    Description:
        Calculates the numbers which are power of 2 and append themp to a list
    Parameter:
        num: parameter to calcualte power of 2 
    Return:
        returns mylist variable which contains numbers which are power if 2

    """
    
    for number_to_iterate in range(num+1):
        mylist.append(2**number_to_iterate)
    return mylist 


num = int(input('Enter the number less than 31'))
print(power_of_2(num))