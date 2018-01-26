'''根据利息计算每个与信用卡固定还款12个月还清'''
'''Monthly interest rate = (Annual interest rate) / 12.0
   Monthly payment lower bound = Balance / 12
   Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0'''
balance = 320000
annualInterestRate = 0.2
# 29157.09
f = annualInterestRate / 12 #月利息
z = balance / 12 #每月最低还款
h = ( balance * ((1 + f)**12)) / 12.0 #每月最高还款
b = balance
while 1:
    m = round((h+z)/2,3)
    b = balance
    for i in range(12):
        b = (b - m) *(1 + f)
    if b > 0:
        z = m
    elif b < 0:
        h = m
    if round(abs(h-z),3) <= 0.002:
        print('Lowest Payment: ',round(m,2))
        break
