import numpy as np
import matplotlib.pyplot as plt

# * A Test Script to Test Whether I can do some 3D Operations #
#// TODO: 1. 3d Plot of a Cuboid                                                          
# TODO: 2. Make the Cuboid Rotate
# TODO: 3. Make an animation for Cuboid
# TODO: 4. Use Serial Data from controller to animate the cuboid

def draw3Dline(a, b):
    pass

def main():
    plt.style.use("dark_background")
    fig = plt.figure(figsize=(8, 4))
    ax = plt.axes(projection="3d")

    x_ax = (0, 1)
    y_ax = (0, 0)
    z_ax = (0, 0)
    ax.plot3D(x_ax, y_ax, z_ax, color='red')

    x_ax = (0, 1)
    y_ax = (0, 0)
    z_ax = (1, 1)
    ax.plot3D(x_ax, y_ax, z_ax, color='red')

    x_ax = (0, 1)
    y_ax = (1, 1)
    z_ax = (0, 0)
    ax.plot3D(x_ax, y_ax, z_ax, color='red')

    x_ax = (0, 1)
    y_ax = (1, 1)
    z_ax = (1, 1)
    ax.plot3D(x_ax, y_ax, z_ax, color='red')
##

    x_ax = (0, 0)
    y_ax = (0, 0)
    z_ax = (0, 1)
    ax.plot3D(x_ax, y_ax, z_ax, color='blue')

    x_ax = (0, 0)
    y_ax = (1, 1)
    z_ax = (0, 1)
    ax.plot3D(x_ax, y_ax, z_ax, color='blue')

    x_ax = (1, 1)
    y_ax = (0, 0)
    z_ax = (0, 1)
    ax.plot3D(x_ax, y_ax, z_ax, color='blue')

    x_ax = (1, 1)
    y_ax = (1, 1)
    z_ax = (0, 1)
    ax.plot3D(x_ax, y_ax, z_ax, color='blue')
##

    x_ax = (0, 0)
    y_ax = (0, 1)
    z_ax = (0, 0)
    ax.plot3D(x_ax, y_ax, z_ax, color='green')

    x_ax = (1, 1)
    y_ax = (0, 1)
    z_ax = (0, 0)
    ax.plot3D(x_ax, y_ax, z_ax, color='green')

    x_ax = (0, 0)
    y_ax = (0, 1)
    z_ax = (1, 1)
    ax.plot3D(x_ax, y_ax, z_ax, color='green')

    x_ax = (1, 1)
    y_ax = (0, 1)
    z_ax = (1, 1)
    ax.plot3D(x_ax, y_ax, z_ax, color='green')

    ax.set_xlim((-2+1, 2))
    ax.set_ylim((-2+1, 2))
    ax.set_zlim((-2+1, 2))

    plt.show()
    




# ---------------------------------------------------------
main()