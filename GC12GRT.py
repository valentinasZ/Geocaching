#task
# First place the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 into the grid below, according to the following rules:
#
#     Each digit appears only once.
#     The 4 digit number B is a multiple of the 4 digit number A.
#     Of the five 2 digit vertical numbers, four of them are prime.
#     No 2 digit or 4 digit number starts with a 0.
#     x = A , y = B
#     xxxx_
#     _yyyy
import gmpy2

def is_valid(a, b):
  """Checks if a and b are valid numbers."""
  return (b > a and b % a == 0 and
          len(set(str(a))) == 4 and len(set(str(b))) == 4 and
          '0' not in str(a) and len([i for i in str(b) if i not in '02468']) >= 3)

def main():
  """Finds all valid numbers and prints them."""
  val = []
  for a in range(1000, 10000):
    for b in range(1000, 10000):
      if is_valid(a, b):
        val.append((a, b))

  for x, y in val:
    a = int(str(x)[1] + str(y)[0])
    b = int(str(x)[2] + str(y)[1])
    c = int(str(x)[3] + str(y)[2])
    d = str(x) + str(y)
    e = [i for i in '0123456789' if i not in d]
    che = [gmpy2.is_prime(a), gmpy2.is_prime(b), gmpy2.is_prime(c)]
    if che.count(True) >= 2 and len(e) == 2:
      print(x, y, e, d)

if __name__ == '__main__':
  main() #4 is correct