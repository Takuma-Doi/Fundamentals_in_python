# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 10:13:54 2018

@author: d01tkum
"""

class Camera:
    """
    constructorにして欲しい事が特に何もしない場合は、
    以下の様に'pass'と書けばいい。
    """
    def __init__(self):
        pass
    
    """
    Pythonのクラスには、'Public method', 'Private method'
    などの概念は無く、一様に外からアクセスできるmethodである。
    （ある意味全部Public method）
    
    しかし、気持ちとして、Public method的に使う場合は普通に命名
    Private method的に使う場合は頭に'_'を付ける文化が（一部で）ある。
    """
    # Public methodの気持ち
    def add(self, name, add_amount):
        total_weight = self._set_total_weight(add_amount)
        print("{2}を{0}個追加しました！\n総重量は{1}です！".format(add_amount, totalWeight, name))
    
    # Private methodの気持ち
    def _set_total_weight(self, amount):
        return amount * 10


if __name__ == '__main__':
    camera = Camera()
    camera.add(name="Mycamera", add_amount=3)
