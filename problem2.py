# https://projecteuler.net/problem=2
finNum = 0
n1 = 0 
n2 = 1
tot = 0

while (finNum < 4000000):
    finNum = n1 + n2
    n1 = n2
    n2 = finNum
    if finNum % 2 == 0:
        tot+= finNum 
    else:
        tot+=0

print(tot)
