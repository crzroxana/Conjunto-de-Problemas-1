import math

print("Una formula cuadratica ax^2 + bx + c, Ingrese coeficiente en orden")
a= float(input("a"))
b= float(input("b"))
c= float(input("c"))
radical= (pow (b,2)-(4*a*c))
x1= (-b+ math.sqrt(radical))/(2*a)
x2= (-b- math.sqrt(radical))/(2*a)
print("ecuacion cuaratica x= " + str(x1) + "y x=" + str(x2))
