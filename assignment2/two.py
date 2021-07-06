# Write a program to calculate direction and magnitude of the vector described by the following points.
# A = (20,30)
# B = (30,40)
import numpy as vec
import math

#calculating Vector
def magnitude(x):
    return math.sqrt(sum(pow(element,2) for element in x))

# Storing vector data
A=vec.array([20,30])
B=vec.array([30,40])

# Storing vector result
Ans1=magnitude(A)
Ans2=magnitude(B)

#printing result of magnitude
print(f"magnitude of {A} is {Ans1} \nmagnitude of {B} is {Ans2}")

