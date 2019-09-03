# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 23:52:11 2018

@author: d01tkum
"""

def fibo(n):
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
    print("{0}".format(fibo(100)))