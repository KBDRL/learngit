#这是求开方的算法
def kaf():
    e = 0.000000000000000001   #精度
    y = int(input("输入一个数字："))
    guess = y / 2
    n = 0
    while abs(guess * guess - y) >= e:
        guess = guess - ((guess ** 2) - y)/(2 * guess)
        n += 1
    print("所求数字为：%s" %guess,"计算次数为：%s" %n)

if __name__ == '__main__':
    kaf()
