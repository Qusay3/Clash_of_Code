
# We want to determine the number of divisors of n in a range from 1 to n.

# The numbers 1 and n are excluded as divisors. 

def number_of_divisors(n):
  
    '''Calculate the number of divisors that can,
    divide n.
    Args:
        n(int): the number to find its divisors
    Returns:
        number of divisors.
    '''
    count = 0
    for i in range(2, n):

        if n % i == 0 :
            
            count +=1
    
    return count

print(number_of_divisors(3))
            
        
        
        
        