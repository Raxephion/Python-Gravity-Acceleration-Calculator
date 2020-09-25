# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:48:26 2020

@author: Pierre-Henri Rossouw

This script calculates the gravity acceleration at any point in the known universe 
up to 15 decimal places accuracy
"""

G = 6.673*10**-11
M_Input = input(" What is the mass of the planet/moon/star/asteroid/comet or other heavenly body? ")
d_Input = input("What is the radius of the object? ")


M = eval(M_Input)
d = eval(d_Input)
eg=9.8


g=(G*M)/d**2
ng=g/eg
print("The mass of your object is ", M, "kg")
print("The radius of your object is ", d, "metres")
print("The Gravity Acceleration for your point is: ", g," metres per second squared")

print("That means the gravity you are experiencing is ", ng , " times that of on Earth")