import numpy as np

def main():
    file = open("euler11.txt", "r")
    nums = file.read().split()
    m = np.asmatrix(nums, dtype = int).reshape((20,20))

    solution = 0
    ldiag = 0
    for i in range(20):
        for j in range(20):
            if(m[i,j] > 20):
                if(i+4<20):
                    down = m[i,j]*m[i+1,j]*m[i+2,j]*m[i+3,j]
                if(j+4<20):
                    right = m[i,j]*m[i,j+1]*m[i,j+2]*m[i,j+3]
                if(i+4<20 and j+4<20):
                    rdiag = m[i,j]*m[i+1,j+1]*m[i+2,j+2]*m[i+3,j+3]
                if(i+4<20 and j-4>0):
                    ldiag = m[i,j]*m[i+1,j-1]*m[i+2,j-2]*m[i+3,j-3]
                solution = max(solution, down, right, rdiag, ldiag)
    print(solution)

main()
