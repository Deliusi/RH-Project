'''This is a "shebang"'''
#!usr/bin/python3

import sys
import os

def circle_info(radius):
     r = float(radius)
     pi = 3.14
     area = pi*(r**2)
     perimeter = 2*pi*r

     print("the area of the circle is: ", area)
     print("the perimeter of the circle is: ", perimeter)


def say_something(something):
    print(str(something))

if __name__ == "__main__":

     circle_info(sys.argv[1])

     say_something(sys.argv[2])
