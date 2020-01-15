import matplotlib.pyplot as plt
import numpy
import random
import math
from mpl_toolkits import mplot3d

"""
Name: Figure Plot
Purpose: To plot coordinates determined by the user
Author: Doctor Cooper and Samuel McManus
Uses: N/A
Used By: N/A
Date: December 2, 2019
"""
def figurePlot(ranges):
    numpy.random.seed(28394837)
    fig = plt.figure()
    for index in range(1,5000):
        r = random.random()
        r = r * (ranges[1] - ranges[0])
        r = r + ranges[0]
        theta = random.random()
        theta = theta * (ranges[3] - ranges[2]) 
        phi = random.random() * math.pi
        x = math.sqrt(abs(r)) * math.cos(theta)
       
        y = math.sqrt(abs(r)) * math.sin(theta)
        ax = plt.scatter(x,y,color = "green")
    plt.show()

"""
Name: Get R Bounds
Purpose: To obtain the lower and upper bounds of r, theta, and phi
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
    
    print('\nR will range from ' + str(ranges[0]) + ' to ' + str(ranges[1]))
    print('\nTheta will range from ' + str(ranges[2]) + ' to ' + str(ranges[3]))
    return ranges
def main():
    ranges = getRBounds()
    figurePlot(ranges)
if __name__ == "__main__":
    main()

