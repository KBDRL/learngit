
'''生成器特性求素数'''

def genPrimes():
    yield 2
    n = 3
    while True:
        for num in range(3, (int(n / 2) + 1)):
            if n % num == 0:
                n += 2
                break
        else:
            yield n
            n += 2
g = genPrimes()
t = 0
for i in g:
    print(i)
