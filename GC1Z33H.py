#task
# You need to come up with three 3 digit numbers using the above digits, each exactly once, and provided that;
# The second number (DEF) is two times the first (ABC)...
# The third number (GHI) is three times the first (ABC)?
# There are four solutions, but only one set will give the correct co-ordinates for the cache.
import itertools
for A,B,C,D,E,F,G,H,I in itertools.product(range(1, 10), repeat=9):
    if   int(str(A)+str(B)+str(C))*2==int(str(D)+str(E)+str(F))  and int(str(A)+str(B)+str(C))*3==int(str(G)+str(H)+str(I)) and  (D+I-F)<=9 and (D+I-F)>=0 and (G-D-A)>=0 and len(str(''.join(set(str(A)+str(B)+str(C)+str(D)+str(E)+str(F)+str(G)+str(H)+str(I)))))==9 :
        print('S27 2{}.{}{}{} E153 0{}.{}{}{}'.format(H,(D+I-F),A,E,B,(G-D-A),E,C) )
        #correct is 4th solution


