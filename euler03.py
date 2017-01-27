import math

def main():
    n = 600851475143
    factor = math.ceil(math.sqrt(n))
    while(factor > 2):
        if(n % factor == 0):
            i = math.ceil(math.sqrt(factor))
            while(factor % i != 0):
                i -= 1
                if(i == 1):
                    print(factor)
                    i = factor
        factor-=1
