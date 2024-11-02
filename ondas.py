import matplotlib.pyplot as plt
import numpy as np

init = (0,5,0.1)

x = np.arange(-5,5,0.1)
y = np.copy(x)

X, Y = np.meshgrid(x, y)

w = 1
c = 1
t = np.arange(0,.2,0.000000001)
print(t.shape)

plt.ion()
r = np.sqrt(np.power(X,2)+np.power(Y,2))
z = 1/r*np.sin((w/c)*(r)-w*1)
fig, ax = plt.subplots()
ax.pcolormesh(X,Y,z, cmap='jet')

for i in t:
    print(i)
    z = 1/r*np.sin((w/c)*(r)-w*i)
    ax.pcolormesh(X,Y,z, cmap='jet')
    plt.pause(1)
plt.show()