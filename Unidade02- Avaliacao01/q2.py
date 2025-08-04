quant = 0
for num in range(10,100000):
    n = num
    pal = 0
    while num > 0:
        pal = pal*10 +(num%10)
        num //= 10
    
    if pal == n:
        quant += 1
print(quant)
