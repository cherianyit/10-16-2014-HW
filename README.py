#10-16-2014-HW
=============
#Discussion 1
7.4
5.0
8
Illegal domain error
11
27
#Discussion 3
0-5
3-10
4,7,10,13
15,13,11,9,7,5
5,4,3
#Discussion 4
1,4,9,16,25,36,49,64,81,100
1 : 1, 3 : 27, 5 : 125, 7 : 343, 9 : 729, 9
012, 212, 412, 612, 812, done
1,2,3,4,5,6,7,8,9,10,11,385
#Discussion 6
-4
2
-4
-2
3
#Exercise 1
#Volume and Surface Area of a Sphere
from math import *
def volSurfSphere():
    radi=eval(input("What is the radius? "))
    vol=(4/3)*pi*radi**3
    area=4*pi*radi**2
    print ("Volume = ",vol)
    print ("Surface Area = ",area)
#Exercise 5
#Pound Thing
def pound():
    pound=eval(input("How many pounds are being ordered? "))
    cost=pound*10.50+pound*0.86+1.50
    print("The cost is: ",cost)
#Exercise 6
#Slope Formula
def slope():
    x1,y1=eval(input("Type in the x1 and y1 coordinates seperated by a comma: "))
    x2,y2=eval(input("Type in the x2 and y2 coordinates seperated by a comma: "))
    slope=(y2-y1)/(x2-x1)
    print("The slope is: ",slope)
