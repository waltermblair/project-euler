def main(a, b, sum):
    if(b > 4000000):
        print(sum)
    else:
        if(b%2==0):
            return main(b, a+b, sum+b)
        else:
            return main(b, a+b, sum)
