import math

sum = 2
for i in range(2,2000000):
    j = 2
    while(i%j != 0 and j < math.sqrt(i)+1):
        if(j >= math.sqrt(i)):
           sum += i
        j += 1
print("Sum = ", sum)
