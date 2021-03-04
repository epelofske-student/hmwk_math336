import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def value(x, t):
	sum = 0
	for n in range(1, 80):
		coef1 = 60.0/((math.pi**3)*(n**3))
		inner = 2*(1-math.cos(n*math.pi))
		inner2 = (n**2)*(math.pi**2)*(1+math.cos(n*math.pi))
		out = (math.e)**(-1*((n**2)*(math.pi**2)*t)/900.0)
		out2 = math.sin((n*math.pi*x)/30.0)
		sum = sum+(coef1*(inner-inner2)*out*out2)
	return 30-x+sum
x = []
t = []
u = []

for a in range(1, 100):
	for i in range(1, 100):
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
