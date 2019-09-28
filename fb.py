"""

http://rosettacode.org/wiki/Factorial_base_numbers_indexing_permutations_of_a_collection

https://en.wikipedia.org/wiki/Factorial_number_system

"""

import math

def apply_perm(omega,fbn):
    """
    
    omega contains a list which will be permuted (scrambled)
    based on fbm.
    
    fbm is a list which represents a factorial base number.
    
    This function just translates the pseudo code in the 
    Rosetta Code task.
    
    """
    for m in range(len(fbn)):
        g = fbn[m]
        if g > 0:
            # do rotation
            # save last number
            new_first = omega[m+g]
            # move numbers right
            omega[m+1:m+g+1] = omega[m:m+g]
            # put last number first
            omega[m] = new_first
            
    return omega
    
def int_to_fbn(i):
    """
    
    convert integer i to factorial based number
    
    """
    current = i
    divisor = 2
    new_fbn = []
    while current > 0:
        remainder = current % divisor
        current = current // divisor
        new_fbn.append(remainder)
        divisor += 1
    
    return list(reversed(new_fbn))
    
def leading_zeros(l,n):
   """
   
   If list l has less than n elements returns l with enough 0 elements
   in front of the list to make it length n.
   
   """
   if len(l) < n:
       return(([0] * (n - len(l))) + l)
   else:
       return l

def get_fbn(n):
    """
    
    Return the n! + 1 first Factorial Based Numbers starting with zero.
            
    """
    max = math.factorial(n)
    
    fbn_list = []
    
    for i in range(max):
        # from Wikipedia article
        current = i
        divisor = 1
        new_fbn = int_to_fbn(i)
        fbn_list.append(leading_zeros(new_fbn,n-1))
        
    return fbn_list
    
omega=[0,1,2,3]

four_list = get_fbn(4)

for l in four_list:
    print(str(l)+'->'+str(apply_perm(omega,l)))


