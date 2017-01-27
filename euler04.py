import math

start = 999*999
solution = 1
for i in range(start, start-100000, -1):
    pow = len(str(i))-1
    if(int(i/math.pow(10,pow)) == int(i%10)):
        value = str(i)
        k = 1
        while(value[k:k+1] == value[-k-1:-k] and k <= len(value)-1):
            k+=1
            if(k == len(value)-1):
                for j in range(999,100,-1):
                    if(i%j == 0 and len(str(int(i/j))) == 3):
                        solution = i
print("Solution: ",solution)
