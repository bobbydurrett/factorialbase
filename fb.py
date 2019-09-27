omega=[0,1,2,3]
fbn=[2,0,1]

for m in range(3):
    g = fbn[m]
    if g > 0:
        print(m)
        print(g)
        print(omega)

        # do rotation
        # save last number
        new_first = omega[m+g]
        # move numbers right
        
        omega[m+1:m+g+1] = omega[m:m+g]
        # put last number first
        omega[m] = new_first
        
print(omega)


        