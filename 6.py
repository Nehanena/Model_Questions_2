#Quadratic Equation Solver

import cmath  
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = cmath.sqrt(b**2 - 4*a*c)
root1 = (-b + d) / (2*a)
root2 = (-b - d) / (2*a)
print("Root 1:", root1)
print("Root 2:", root2)
