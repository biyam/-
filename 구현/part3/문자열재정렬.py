import re
a = "".join(sorted(input()))


numbers = re.findall("\d", a)
strings = re.findall("[a-zA-z]", a)

sum = 0
for i in numbers:
    sum += int(i)
    
print(''.join(strings) + str(sum))