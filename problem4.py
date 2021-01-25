maxPal = 0

for i in range(100, 999):
    for x in range(100,999):
        tempPal = str(i*x)
        if tempPal[0] == tempPal[-1] and tempPal[1] == tempPal[-2] and tempPal[2] == tempPal[-3]:
            tempPal = int(tempPal)
            if tempPal > maxPal:
                maxPal = tempPal
print(maxPal)
