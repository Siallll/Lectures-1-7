# 1*2 =2
# 2*3*4=24
# 3*4*5*6=
# 4*5*6*7*8=
n = 4
sum = 0
for i in range(1, n + 1):
    prod = 1
    for j in range(i, (2 * i) + 1):
        prod *= j
    sum += prod
print(sum)
