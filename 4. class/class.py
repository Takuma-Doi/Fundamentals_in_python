# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 10:13:54 2018

@author: dadad
"""

class camera:
    
    def __init__(self):
        pass
        
    def add(self, name, add_amount):
        
        totalWeight = self._setTotalWeight(add_amount)
        print("{2}を{0}個追加しました！\n総重量は{1}です！".format(add_amount, totalWeight, name))
    
    def _setTotalWeight(self, amount):
        return amount * 10


cam = camera()
cam.add(name = "Mycamera", add_amount=3)