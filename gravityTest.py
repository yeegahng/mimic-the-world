import matplotlib.pyplot as plt
import math


a = [0, -1]
v = [10, 0]
p = [0, 1000]
anchor = [500, 500]
pvec = [list(), list()]
dvec = list()
for _ in range(100):
    v[0] += a[0]
    v[1] += a[1]
    p[0] += v[0]
    p[1] += v[1]
    pvec[0].append(p[0])
    pvec[1].append(p[1])
    dvec.append(math.sqrt((anchor[0] - p[0])**2 + (anchor[1] - p[1])**2))

plt.subplot(311)
plt.scatter(pvec[0], pvec[1])
plt.scatter(anchor[0], anchor[1])
plt.subplot(312)
plt.scatter(range(len(dvec)), dvec)
plt.subplot(313)
plt.show()
