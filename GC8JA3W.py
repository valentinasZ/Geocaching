import itertools
# task
# Geocaching is a very important word. It invites You to find, investigate and to solve.
# Try to  find the root from GEOCACHING and You will get coordinates:

formula = '''N 54 43.N(H-G)(A+N)
E 25 1(O+A+1).O(C+E-2)(I+1)'''

for g, e, o, c, a, h, i, n in itertools.product(range(0, 10), repeat=8):
    if h - g > 0 and a + n < 10 and o + a + 1 < 10 and 2*e - 2 > 0 \
            and c + e - 2 < 10 and i + 1 < 10 and all(g != x for x in [e, o, c, a, h, i, n]) \
            and all(e != x for x in [o,c,a,h,i,n]) and all(o != x for x in [c,a,h,i,n]) \
            and all(c != x for x in [a,h,i,n]) and all(a!= x for x in [h,i,n]) and h!=i \
            and h!=n and i!=n \
       and  int((int('{}{}{}{}{}{}{}{}{}{}'.format(g,e,o,c,a,c,h,i,n,g)))**0.5) == (int('{}{}{}{}{}{}{}{}{}{}'.format(g,e,o,c,a,c,h,i,n,g)))**0.5 :
        print(f'54 43.{n}{h-g}{a+n}',f'25 1{o+a+1}.{o}{c+e-2}{i+1}')
        print( (int('{}{}{}{}{}{}{}{}{}{}'.format(g,e,o,c,a,c,h,i,n,g))))