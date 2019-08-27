import random
import string
str1=string.printable
print(str1)
print(len(str1))

for i in range(6):
    print (str1[random.randint(0,100)],end="")
