
"""
import random
n=random.randbytes(3)
print(n)
x=random.sample
print(x)
print(random.randrange(0,99))
print(random.randint(100,211))

mylist=("black","white","mono")
mylist1={"lol","haha"}
mylist2=["pv sindhu", "kevin", "sania", "saina"]
print(random.choice(mylist))
print(random.choice(mylist1))
print(random.choice(mylist2)

print(random.shuffle(mylist))
print(random.shuffle(mylist1))
print(random.shuffle(mylist2))

"""


import string
import random
s=10
ran= ''.join(random.sample(string.ascii_uppercase+string.digits, k=10))
print(ran)
s1=4
ran1= ''.join(random.sample(string.digits, k=6))
print(ran1)

