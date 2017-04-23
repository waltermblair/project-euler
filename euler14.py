def main():
    longestChain = 0
    solution = 0
    for i in range(2, int(1e6)):
        chain = 1
        tmp = i
        while i > 1:
            if i % 2 == 0:
                i/=2
                chain+=1
            else:
                i=3*i+1
                chain+=1
        if chain > longestChain:        
            longestChain = chain
            solution = tmp
    print(solution)

main()
