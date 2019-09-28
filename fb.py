"""

http://rosettacode.org/wiki/Factorial_base_numbers_indexing_permutations_of_a_collection

https://en.wikipedia.org/wiki/Factorial_number_system

"""

def apply_perm(omega,fbm):
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

omega=[0,1,2,3]
fbn=[2,0,1]
      
print(apply_perm(omega,fbn))


