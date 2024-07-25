'''

@Author: Girish
@Date: 2024-07-23 
@Last Modified by: Girish
@Last Modified time: 2024-07-23 
@Title : Temperature Conversion

'''

def celcius_to_fahrenheit(Celcius):
    """
    
    Description:
        Converts Celcius to Fahrenheit and Vice versa
    Parameter:
        Celcius : Temperature in Celcius Value
           
    Return:
        returns value of Celcius on Farhenite 

    """ 
    F = (Celcius * 9/5) + 32
    return F
    

def fahrenheit_to_celcius(fahrenheit):
    """
    
    Description:
        Converts Celcius to Fahrenheit and Vice versa
    Parameter:
        fahrenheit : Temperature in Celcius Value
           
    Return:
        returns value of Farhenite  to Celcius

 
    """     
    C = (fahrenheit - 32) * 5/9
    return C





Choose_type_of_conversion = int(input("Enter 1 if F to C or 2 for C to F"))
if Choose_type_of_conversion == 0:
    Celcius = int(input("Enter Temp in Celcius "))
    print(celcius_to_fahrenheit(Celcius))
else:
  fahrenheit = int(input("Enter the temperature in Farenheit"))
  print(fahrenheit_to_celcius(fahrenheit))  
    