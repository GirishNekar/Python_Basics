

'''

@Author: Girish
@Date: 2024-07-22 
@Last Modified by: Girish
@Last Modified time: 2021-02-11 
@Title : Prime facors 

'''

import time

def stop_watch():
    """
    
    Description:
        prints elapsed time from start and end point
    Parameter:
        none
    Return:
       none 

    """
    
    input("Press enter to start the timer")
    start_time = time.time()
    input("Press enter to stop the timer")
    stop_time = time.time()
    print(stop_time - start_time)


stop_watch()