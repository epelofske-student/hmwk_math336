import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def value(x, t):
	L = 40
	alpha = 1
	sum = 0
	for n in range(1, 80):
		cn = 0
		if n%2 == 1:
			cn = 0
		if n%2 == 0:
			cn = -1*(4.0/(math.pi*((n**2)-1)))
		p1 = math.e**((-1*((n**2)*(math.pi**2)*(alpha**2)*t))/(L**2))
		p2 = math.cos((n*math.pi*x)/float(L))
		sum = sum+(cn*p1*p2)
	return (math.pi/2.0)+sum
x = []
t = []
u = []

for a in range(1, 100):
	for i in range(1, 300):
		x.append(a)
		t.append(i)
		u.append(value(a, i))
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(x, t, u, linewidth=0.2, antialiased=True)
ax.set_ylabel('t')
ax.set_xlabel('x')
ax.set_zlabel('u(x, t)')
plt.show()
