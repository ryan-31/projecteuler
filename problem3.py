# https://projecteuler.net/problem=3

maxNum = 600851475143
primeFactor = 1

for i in range(maxNum):
    if i > 0:
        if maxNum % i == 0:
            if i > primeFactor:
                primeFactor = i
                
print(primeFactor)