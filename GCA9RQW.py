#task
#Next week's winning lottery numbers are 8 different numbers all in the range 11 to 99 inclusive
#Three, and only three of them are prime numbers and the sum of these three is 265
#Of the other 5, just two of them are even, and when these 2 are multiplied together they make 1332
#The mean of the remaining 3 is 23
#What are the eight winning lottery numbers?

import sympy
import itertools
import statistics
#----------------------
even = []
odd =[]
#finding all prime numbers in range 11 - 99
prime_numbers = list(sympy.primerange(11,99))
#finding primes which 3 numbers sum is 256
prime = [i for i in itertools.combinations(prime_numbers,3) if sum(i)==265]
# finding even numbers
for i in range(12,99,2):
    for j in range(14,99,2):
        if (i*j)==1332:
            even.append([i,j])
            break
# finding odd numbers
odd = [i for i in range(11,99) if i%2!=0 and i not in prime_numbers]
odd_1 = [i for i in itertools.combinations(odd,3) if statistics.mean(i)==23 ]


print(sorted(list(prime[0])+(even[0])+list(odd_1[0])))
