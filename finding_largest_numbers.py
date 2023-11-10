# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
### Data ###

# x = [10,20,90,50,80]
# x = [-1,2,-3,7,-4]
x = [-1,-2,-3,-4,-5]

### Variables ###

largestnumbers = [] # Contains your answers (largest values).
number = 2 # Controls the the number of the largest numbers (Number of times you run the loop).

### ### 

def finding_largest_number (x, largestnumbers):   
    """
    This function finds the largest value in a list.
    
    Parameters:
        x : The list that we will use to find the largest value.
        largestnumbers : The list in which we store the largest value.
        
    Returns:
        largestnumbers : The list with the largest numbers.
    """
    largestvalue = -1e20 # A small number that is used to compare values in the beginning.
    
    # This loop finds the largest number from the list x.
    for i in range(len(x)):
        # print(x[i])
        if x[i] >= largestvalue:
            largestvalue = x[i]
            index = i
            
    largestnumbers.append(x[index]) # Adds the largest value to the list.
    del(x[index]) # Removes the largest value from x.
    # print(largestvalue)
    return largestnumbers

# Repeats the function to find a certain number of the largest values.
for a in range(number):
    answer = finding_largest_number(x, largestnumbers)
print(answer)
