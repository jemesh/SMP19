#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:37:12 2019

@author: ghost
"""

def gcd(a, b):
    if b==0:
        return a
    else:
        return(gcd(b,a%b))

x=int(input("A:"))
y=int(input("B:"))
if y>x:
    x,y=y,x
print(gcd(x,y))