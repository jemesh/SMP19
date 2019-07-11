#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:29:59 2019

@author: ghost
"""

def gfg(x,l=[ ] ):
    for i in range(x):
        l.append(i*i)
        print(l)
#gfg appends the squares to list l, which is empty by default

gfg(2)
#This has empty list l going through states 
#[0]
#[0, 1]
gfg(3,[3,2,1])
#has a list l, but the values don't get modified, they only append to the list
#[0]
#[0, 1]
#[0, 1, 4]
gfg(3)
#the empty list from before remembers the values from when itwas run for gfg(2)
#why does it remember? because it does.
#[0, 1, 0]
#[0, 1, 0, 1]
#[0, 1, 0, 1, 4]