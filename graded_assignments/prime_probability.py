import os
import random
l=[]
for i in range(1000000):
    l.append(random.randint(1,6))
print(l.__sizeof__())
# primes=[2,3,5]
aha:int=0
for haha in l:
    if haha %2 :
        aha+=1
some_var = aha / len(l)
print(some_var*100)