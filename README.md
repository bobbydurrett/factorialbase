# factorialbase
Rosetta Code Python Implementation of "Factorial base numbers indexing permutations of a collection"

http://rosettacode.org/wiki/Factorial_base_numbers_indexing_permutations_of_a_collection

Notes:

https://en.wikipedia.org/wiki/Factorial_number_system

fb.py does the example where 

omega = 0123 and 2.0.1 leads to 2031.

get_fbn working 

but apply_perm not working for several cases:

output:

[0, 0, 0]->[0, 1, 2, 3]
[0, 0, 1]->[0, 1, 3, 2]
[0, 1, 0]->[0, 3, 1, 2]
[0, 1, 1]->[0, 1, 2, 3]
[0, 2, 0]->[0, 3, 1, 2]
[0, 2, 1]->[0, 2, 1, 3]
[1, 0, 0]->[2, 0, 1, 3]
[1, 0, 1]->[0, 2, 3, 1]
[1, 1, 0]->[2, 3, 0, 1]
[1, 1, 1]->[3, 0, 1, 2]
[1, 2, 0]->[0, 2, 3, 1]
[1, 2, 1]->[2, 1, 3, 0]
[2, 0, 0]->[3, 2, 1, 0]
[2, 0, 1]->[1, 3, 0, 2]
[2, 1, 0]->[0, 3, 1, 2]
[2, 1, 1]->[1, 3, 2, 0]
[2, 2, 0]->[2, 0, 1, 3]
[2, 2, 1]->[1, 3, 0, 2]
[3, 0, 0]->[2, 1, 3, 0]
[3, 0, 1]->[0, 2, 3, 1]
[3, 1, 0]->[1, 2, 0, 3]
[3, 1, 1]->[3, 2, 0, 1]
[3, 2, 0]->[1, 0, 3, 2]
[3, 2, 1]->[2, 3, 0, 1]

should be:

0.0.0 -> 0123
0.0.1 -> 0132
0.1.0 -> 0213
0.1.1 -> 0231
0.2.0 -> 0312
0.2.1 -> 0321
1.0.0 -> 1023
1.0.1 -> 1032
1.1.0 -> 1203
1.1.1 -> 1230
1.2.0 -> 1302
1.2.1 -> 1320
2.0.0 -> 2013
2.0.1 -> 2031
2.1.0 -> 2103
2.1.1 -> 2130
2.2.0 -> 2301
2.2.1 -> 2310
3.0.0 -> 3012
3.0.1 -> 3021
3.1.0 -> 3102
3.1.1 -> 3120
3.2.0 -> 3201
3.2.1 -> 3210
       
   