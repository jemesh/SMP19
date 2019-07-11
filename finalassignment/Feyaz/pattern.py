#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:44:51 2019

@author: ghost
"""

# I really want to hardcode the pattern in, but I won't.
n=int(input("Enter no. of levels:"))
#print("     *\n    ***\n   *****\n  *******\n *********\n")
for x in range(n+1):
    for y in range(n-x):
        print(" ", end="")
    for y in range(2*x-1):
        print("*", end="")
    print("")