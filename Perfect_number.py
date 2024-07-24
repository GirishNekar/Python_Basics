
'''
@Author: Girish
@Date: 2024-07-22 
@Last Modified by: Girish
@Last Modified time: 2021-02-11 
@Title : finding no of randoms to traverse the list of numbers only once
'''
def check_perfect(num):
    """
    
    Description:
        chechs if a number is a perfet number
    Parameter:
        num: number we are using to check 
    Return:
        returns The number is perfet or not

    """
    sum = 0
    for number_to_iterate in range(1,(num/2)+1):
        if num % number_to_iterate == 0:
            sum = sum + number_to_iterate
    if sum == num:
        return "The number is a Perfect number"
    else:
        return "Not a perfect Number"

num = int(input("enter the number of to chech if ita a perfect number"))
print(check_perfect(num))