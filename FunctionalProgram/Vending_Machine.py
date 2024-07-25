'''

@Author: Girish
@Date: 2024-07-23 
@Last Modified by: Girish
@Last Modified time: 2024-07-23 
@Title : Find the Fewest Notes to be returned for Vending Machine

'''
def min_notes_vending_machine(change,notes):
    
    """
    
    Description:
        finds minimum number of notes for a chage in a given list of numbers  
    Parameter:
        change: input for the vending machine 
        notes: posiible list of notes that a vending mavchine can give  
    Return:
        returns list if notes and minimum number of notes for a given change 

    """
    
    count = 0
    if change <= 0:
        return [],0
    for note in notes :
        if note <= change:
            result_notes,count =min_notes_vending_machine(change - note,notes)
            return[note] + result_notes,count+1
    return [],count     
           


change = int(input("Enter the change that is needed "))
notes = [1000,500,100,50,10,5,2,1]
print(min_notes_vending_machine(change,notes))

