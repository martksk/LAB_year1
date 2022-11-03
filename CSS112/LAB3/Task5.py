def tri():
    bl = int(input("Please enter the base length:"))
    h = int(input("Please enter the height:"))
    area = (1/2)*bl*h
    tri = "The area of triangle with base = "+str(bl)+" and height = "+str(h)+" is "+str(float(area))
    return tri

import math

def cub():
    bw = int(input("Please enter the base width:"))
    l = int(input("Please enter the length:"))
    h = int(input("Please enter the height:"))
    vol = bw*l*h
    cub = "The cubic volumn of width = "+str(bw)+" length = "+str(l)+" and height = "+str(h)+" is "+str(vol)
    return cub

def con():
    bd = int(input("Please enter the base diameter:"))
    h = int(input("Please enter the height:"))
    r = bd/2
    vol = (1/3)*22/7*r*r*h
    con = "The conical volumn of cone with diameter = "+str(bd)+" and height = "+str(h)+" is "+"%.12f"%vol
    return con


print("Please enter a choice for your selection:")
print("Enter 1 if you want to calculate the area of a triangle.")
print("Enter 2 if you want to calculate the volumn of a cubic.")
print("Enter 3 if you want to calculate the volumn of a cone.")
choice = int(input("Enter your choice here:"))
checkch = [1,2,3]
if choice in checkch:
    if choice == 1:
        print(tri())
    elif choice == 2:
        print(cub())
    elif choice == 3:
        print(con())
else:
    print("Invalid Choice")