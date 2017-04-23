import numpy as np

def main():
    infile = open("euler13.txt", "r")
    
    lines = infile.read().split()
    arr = []
    for line in lines:
        arr.append(eval(line))

    sum = 0
    for num in arr:
        num /= 1e40
        sum += num
    print(sum)
        
        

main()
