# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:51:19 2018

@author: d01tkum
"""
class A:
    def method(self):
        print("class A")

class B(A):
    def __init__(self, num):
        self.num = num;
    
    def print_num(self):
        print('引数で渡された数字は{}です。'.format(self.num))
        
class C:
    pass

class D(B):
    def print_test2_info(self):
        print('このクラスはBクラスを継承しています。')
        super().print_num()  #親クラスのprint_num()を呼び出す

class E():
    def method(self):
        print("class E")

class F(C,D,E):
    pass

f = F(10)
f.method()
d = D(10)
d.print_test2_info()