'''this program finds the euclidean distance between two points taken as input fron user '''

import math #importing module

x1,y1= map(float, input("Enter the first coordinate").split())
x2,y2=map(float, input("Enter the second coordinate").split ())

#calculating euclidian distance
euclidian_distance= math.sqrt((x2-x1)**2 + (y2-y1)**2)

#printing the output
print(f"Euclidean distance between ({x1}), ({y1}) and ({x2}), ({y2}) is:{euclidian_distance:.2f}")
