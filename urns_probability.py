#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 00:11:49 2020

@author: alaaeddinemahi
"""

def winning_number(n):
    res = 0
    index = 0 
    for i in range(1,n+1):
        for j in range(1, n+1):
            try:
                p = 0.5*(i/i+j) + 0.5*((5-i)/(10-i-j))
            except:
               continue 
            if p > res:
                res = p
                index = i
    return p, index