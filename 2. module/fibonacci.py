# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 23:51:23 2018

@author: dadad
"""

def fibo_make(n):
    result = []
    a = 1
    b = 1

    while b < n:
        result.append(b)
        val = a + b
        b = a
        a = val
    return result

if __name__ == "__main__":
    print("{0}".format(fibo_make(100)))