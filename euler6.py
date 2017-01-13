sums = 0
squares = 0
for i in range(1, 101, 1):
    sums += i*i
    squares += i
squares *= squares
print(squares-sums)
