#!/usr/bin/python

import math
 
print("Circle/Sphere calculator")
print("Note: Pi is equal to",math.pi)
 
#Getting the radius as input
r = int(input("Radius: "))
 
#Calculations based of the radius
d = r*2
#_circle is the calculation, where pi is also calculated
PCirclePi = math.pi*r*2
SCirclePi = math.pi*r**2
#_npi is the calculation, where pi (as a symbol) is left in
PCircleNPi = r*2
SCircleNPi = r**2
#Sphere area
SSpherePi  = 4*math.pi*(r**2)
SSphereNPi = 4*(r**2)
#Sphere volume
VSpherePi = 4/3*math.pi*(r**3)
VSphereNPi = (r**3)
 
#Output
print(" ")
#Diameter
print("d =",d)
#Circle perimeter
print("P =","pi*{}".format(PCircleNPi),"or",PCirclePi)
#Circle area
print("Scircle =","pi*{}".format(SCircleNPi),"or",SCirclePi)
#Sphere area
print("Ssphere =","4*pi*{}".format(SSphereNPi)+"*{}".format(SCircleNPi),"or",SSpherePi)
#Sphere volume
print("Vsphere =","4/3*pi*{}".format(VSphereNPi),"or",VSpherePi)
