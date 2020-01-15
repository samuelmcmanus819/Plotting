import matplotlib.pyplot as plt
import numpy
import random
import math
from mpl_toolkits import mplot3d

"""
Name: Figure Plot
Purpose: To plot 3d coordinates of a hypersphere
Author: Doctor Cooper and Samuel McManus
Uses: N/A
Used by: N/A
Date: December 2 2019
"""
def figurePlot(ranges):
    numpy.random.seed(28394837)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    for index in range(1,1000):
        r = random.random()
        r = r + ranges[0]
        r = r * (ranges[1] - ranges[0])
        theta = random.random()
        theta = theta + ranges[2]
        theta = theta * (ranges[3] - ranges[2])
        phi = random.random()
        phi = phi + ranges[4]
        phi = phi * (ranges[5] - ranges[4])
        x = math.pow(r, (1.0/3.0)) * math.cos(theta) * math.sin(phi)
        """
        Note: Using cos phi for y creates a dope little hourglass
        """
        y = math.pow(r, (1.0/3.0)) * math.sin(theta) * math.sin(phi)
        z = math.pow(r, (1.0/3.0)) * math.cos(phi)

        print(str(x) + " " + str(y) + str(z))
        ax.scatter(x,y,z,color = "green")

    plt.show()

"""
Name: Get R Bounds
Purpose: To obtain upper and lower bounds for r, theta, and phi
Author: Samuel McManus
Uses: N/A
Used By: N/A
Date: December 2 2019
"""
def getRBounds():
    ranges = []
    while(True):
        range = input('Enter the lower bound of r: ')
        try:
            range = float(range)
            ranges.append(range)
            break
        except ValueError:
            print('Error, you must enter a number')

    while(True):

        range = input('Enter the upper bound of r: ')
        try:
            range = float(range)
            ranges.append(range)
            break
        except ValueError:
            print('Error, you must enter a number')
    
    while(True):
        range = input('Enter the lower bound of theta: ')
        try:
            range = float(range)
            ranges.append(range)
            break
        except ValueError:
            print('Error, you must enter a number')

    while(True):

        range = input('Enter the upper bound of theta: ')
        try:
            range = float(range)
            ranges.append(range)
            break
        except ValueError:
            print('Error, you must enter a number')
    
    while(True):

        range = input('Enter the lower bound of phi: ')
        try:
            range = float(range)
            ranges.append(range)
            break
        except ValueError:
            print('Error, you must enter a number')

    while(True):

        range = input('Enter the upper bound of phi: ')
        try:
            range = float(range)
            ranges.append(range)
            break
        except ValueError:
            print('Error, you must enter a number')

    print('\nR will range from ' + str(ranges[0]) + ' to ' + str(ranges[1]))
    print('\nTheta will range from ' + str(ranges[2]) + ' to ' + str(ranges[3]))
    return ranges
def main():
    ranges = getRBounds()
    figurePlot(ranges)
if __name__ == "__main__":
    main()
