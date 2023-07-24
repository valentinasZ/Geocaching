# after you solve any MOM
# save your result to mom.txt file
import re
y,x = [],[]
with open('mom.txt') as text:
    for i in text.readlines():
        if 'X =' in i and 'Y =' in i:
            x.append(int(''.join(re.findall('X = (\d+)', i ))))
            y.append(int(''.join(re.findall('Y = (\d+)', i))))


print(sum(x))
print(sum(y))

