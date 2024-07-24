'''

@Author: Girish
@Date: 2024-07-23 
@Last Modified by: Girish
@Last Modified time: 2024-07-23 
@Title : Finding day of a week for given date

'''

def day_of_week(month, day, year):
    
    """
    
    Description:
    finds day in a week foe a given date
    Parameter:
           month:month of year
           day: day of a month
           year:year for which day need to be found
    Return:
        returns day of a week 

    """   
    
    
    y0 = year - (14 - month) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = month + 12 * ((14 - month) // 12) - 2
    d0 = (day + x + (31 * m0) // 12) % 7
    day_dict = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    return day_dict[int(d0)]

month = int(input("Enter the month (1-12): "))
day = int(input('Enter the day (1-31): '))
year = int(input('Enter the year: '))

print(day_of_week(month, day, year))