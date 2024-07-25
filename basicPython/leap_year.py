def check_if_leap(num):
    if num % 4 == 0:
        if num % 100 == 0:
            if num % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
       return False
    
    
    
num = int(input('Enter the year (only 4 digi numbers)'))
print(check_if_leap(num))