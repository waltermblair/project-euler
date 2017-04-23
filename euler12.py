import math

def main():
    n = 1
    d = 0
    sum = 0
    while d < 500:
        sum += n
        d = 0
        for i in range(1, math.ceil(sum**0.5)):
            if sum % i == 0:
                d += 2
            
        n += 1
    print(sum)
   
main()
