import random, math
vse = 50000000
#for j in range(5):
inCircle = 0
for i in range(vse):
    yCoord = random.random()
    xCoord = random.random()
    if ((xCoord-0.5)**2 +(yCoord -0.5)**2)**0.5 <= 0.5:
        inCircle = inCircle + 1
print((inCircle*4)/(vse))