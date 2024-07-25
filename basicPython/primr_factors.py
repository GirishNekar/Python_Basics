'''

@Author: Girish
@Date: 2024-07-22 
@Last Modified by: Girish
@Last Modified time: 2021-02-11 
@Title : Prime facors 

'''


def prime_factors(num):
    """
    
    Description:
        calcualtes prime factors of a given number
    Parameter:
        num: it is a number for which we are calculating the prime facoors
    Return:
        returns list of prime factors

    """
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 2

    if n > 2:
        factors.append(n)
    
    return factors


num = int(input("Enter a number "))
factors = prime_factors(num)
print(factors)
