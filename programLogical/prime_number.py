'''

@Author: Girish
@Date: 2024-07-23 
@Last Modified by: Girish
@Last Modified time: 2021-02-11 
@Title : finding no of randoms to traverse the list of numbers only once

'''
def prime_num(num):
    """
    
    Description:
        Checks if a given number is prime or not 
    Parameter:
        num: this id the number that is being checked
    Return:
        return prime if its a prime number , if  not retunr s nOt a Prime number 

    """  
    
    
    if num == 0:
        return " NOt a Prime NUmber"
    if num == 1:
        return "Not aprime Number"
    if num == 2 :
        return "It is a Prime Number"
    if num >2:
        for number_to_iterate in range(2,num):
            if num % number_to_iterate == 0:
                return "Not a Prime Number"
        return "Prime Number "
            
            
            




num = int(input("Enter thr number to checkfor prime\n"))
print(prime_num(num))