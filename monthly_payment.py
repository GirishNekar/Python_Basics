
'''

@Author: Girish
@Date: 2024-07-23 
@Last Modified by: Girish
@Last Modified time: 2024-07-23 
@Title : Finding monthly payment of a person who took loan 

'''

def monthly_payment(P,Y,R):
    """
    
    Description:
        finds the onthly paymnet of a person 
    Parameter:
        P : Loan amount 
        Y : Number of years given to pay off the loan
        R : Interest rate
    Return:
        returns payment has to be made monthly

    """ 
    
    n = 12 * Y
    r = R / (12 * 100)
    payment = (P * r) / (1 - (1 + r) ** (-n))
    return payment



P = int(input("Enter the Loan amount to be paid"))
Y = int(input("Enter the number of years given to pay off the Loan"))
R = int(input("Entert the interst rate"))

print(monthly_payment(P,Y,R))