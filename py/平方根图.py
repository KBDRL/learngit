import math
import matplotlib.pyplot as plot

fig,ax = plot.subplots()
#barh为横向 bar为竖向条形图
L = []
s = 0
for i in range(1000):
    s += 0.001
    L.append(s)
print(L)
ax.scatter([i for i in L], [math.sqrt(i) for i in L], 1)

#plot.show()



plot.show()