def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    6a+9b+20c=n
    """
    #设a，b，c为0；取值范围为0-n/(6 or 9 or 20）
    a, b, c = 0, 0, 0
    print('n = ', n)
    for a in range(0, int(n / 6) + 1):
        #print('a = ', a)
        if (6 * a + 9 * b + 20 * c) == n:
            print('YES')
            return True
        for b in range(0, int(n / 9) + 1):
            #print('b = ', b)
            if (6 * a + 9 * b + 20 * c) == n:
                print('YES')
                return True
            for c in range(0, int(n / 20) + 1):
                if (6 * a + 9 * b + 20 * c) == n:
                    return True
    print("NO")
    return False
    #当a达到峰值即 a == n / 6 时 a的下限增加 1 而b，c的下限不变

    #当a的下限等于上限时，a的下限重置为0 转而从b的下限开始增长

    #当b的下限等于上限时，b的下限重置为0 转而从c的下限开始增长


a = [400, 126, 27, 35, 37, 43, 7, 123]
for i in a:
    print(McNuggets(i))
