# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:59:30 2018

@author: dadad
"""
class Spam:
    __aaa = 100
    def __init__(self):
        self.__aaa = 999
        print(self.__aaa)
        
    def method(self):
        self.__method()
        print(self.__aaa)
        
    def __method(self):
        print(self.__aaa)

spam =Spam()
spam.method()   #OK
#spam.__method() #NG
#spam.__attr     #NG