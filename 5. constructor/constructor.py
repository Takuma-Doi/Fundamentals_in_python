# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:23:08 2018

@author: dadad
"""
"""
class MyClass():
    def __init__(self, message):
        self.value = message
 
myinstance = MyClass("Hello!")
print(myinstance.value)
print(MyClass)
"""

class MyClass:
    #count = 0                       # クラス変数を初期化

    def __init__(self,a):
        self.count = a
        self.count += 1          # クラス変数をカウントアップ

a1 = MyClass(a=1)
a2 = MyClass(2)

print(a1.count)
#print(a2.count)
#print(MyClass.count ) 