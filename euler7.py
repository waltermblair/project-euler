counter = 1
a = 3
while(counter < 10001):
    i = 2
    while(a%i != 0 and i < a):
        i += 1
        if(i == a):
            counter += 1
    a += 1
print(a-1)
