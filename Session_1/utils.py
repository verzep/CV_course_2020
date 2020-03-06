import time
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()
    
    
def select_points(img, N_points):
    tellme('Click to begin')
    plt.imshow(img)

    plt.waitforbuttonpress()
    pts = []
    while True:

        while len(pts) < N_points:
            tellme('Select {} points'.format(N_points))
            pts = np.asarray(plt.ginput(N_points, timeout=-1))
            if len(pts) < N_points:
                tellme('Too few points, starting over')
                time.sleep(1)  # Wait a second
                
        tellme('Key click to confirm')

        if plt.waitforbuttonpress():
            break
            
    return pts


def draw_line(point1,point2, options = 'b'):
    
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    
    plt.plot(x_values, y_values, options)
