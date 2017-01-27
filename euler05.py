i = 20
found = False
while(not found):
    i+=1
    j=1
    while(i%j==0):
        j+=1
        if(j==21):
            print(i)
            found = True
