'''

@Author: Girish
@Date: 2024-07-23 
@Last Modified by: Girish
@Last Modified time: 2021-02-11 
@Title : reversing a number

'''


def swap_nibbles_8bit(num):
    
    
    """
    
    Description:
        swaps the nibble   
    Parameter:
        num : number that needed to be swapped
    Return:
        returns swapped binary string 


    """
   
   
    binary_bits = format(num, '08b')
    mylist = [char for char in binary_bits]

    
    for i in range(4):
        temp = mylist[i]
        mylist[i] = mylist[i+4]
        mylist[i+4] = temp

    swapped_binary_str = "".join(mylist)
    return swapped_binary_str

def is_power_of_2_after_swapping(binary_str):
    
    
    """
    
    Description:
        Chacks if the swapped number is power of 2   
    Parameter:
        binary_str : string that needed to checked for the power of 2 
    Return:
        returns True if it is power of 2 and returns false if it si not power of 2 


    """   
    
    
    first_one_index = binary_str.find('1')
    

    if first_one_index == -1:
        return False
    

    for char in binary_str[first_one_index + 1:]:
        if char == '1':
            return False
    
    return True


num = int(input("Enter an 8-bit integer (in decimal): "))
    
    
swapped_binary_str = swap_nibbles_8bit(num)
print("Swapped binary string:", swapped_binary_str)
    
   
if is_power_of_2_after_swapping(swapped_binary_str):
    print("The number is a power of 2 after swapping nibbles.")
else:
    print("The number is NOT a power of 2 after swapping nibbles.")


