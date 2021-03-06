# Modified from https://www.bragitoff.com/2020/10/3d-trajectory-animated-using-matplotlib-python/
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


def animate(num, dataSet, line):
    line.set_data(dataSet[:, :num])
    # line.set_data(dataSet[0:2, :num])    
    # line.set_3d_properties(dataSet[2, :num])    
    return line


def plot_trajectory(x, y, fileName):
    fig = plt.figure()
    # ax = Axes3D(fig)
    # dataSet = np.array([x, y, t])
    dataSet = np.array([x, y])
    numDataPoints = len(x)
    # line = plt.plot(x, y, t, lw=2, c='g')[0] # For line plot
    line = plt.plot(x, y, lw=2, c='g')[0] # For line plot
    
    # ax.set_xlabel('Projected dim 0')
    # ax.set_ylabel('Projected dim 1')
    # ax.set_zlabel('Iteration')
    plt.title('Trajectory of latent vector')
    plt.xlabel('Projected dim 0')
    plt.ylabel('Projected dim 1')
    line_ani = animation.FuncAnimation(
        fig, animate, frames=numDataPoints, 
        fargs=(dataSet, line), interval=200, blit=False)
    line_ani.save(fileName)
    plt.close()


if __name__ == '__main__':
    t = np.arange(0,20,0.2) # This would be the z-axis ('t' means time here)
    x = np.cos(t)-1
    y = 1/2*(np.cos(2*t)-1)

    plot_trajectory(x, y, 'AnimationNew.mp4')
