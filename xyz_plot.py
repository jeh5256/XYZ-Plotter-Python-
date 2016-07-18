from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

path = "/Users/justinhughes/downloads/nvt.xyz"

/Users/justinhughes/PycharmProjects/untitled1

with open(path) as xyzFile:
    coords = xyzFile.readlines()

x = y = z = []

for xyz in range(2, int(coords[0]) + 1):

     x.append(float(coords[xyz].rsplit()[1]))
     y.append(float(coords[xyz].rsplit()[2]))
     z.append(float(coords[xyz].rsplit()[3]))



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.show()