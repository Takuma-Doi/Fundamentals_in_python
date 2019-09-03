# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:23:08 2018

@author: d01tkum
"""

class MyClass:
    """
    'def __init__(self)' がconstructorです。
    constructorとは、クラスからインスタンスを作成した際に実行される関数です。
    つまり、クラスの初期状態を設定する関数をconstructorと言います。
    """
    def __init__(self,val):
        # 'val'が与えられていない場合、怒りを返して終了
        raise val==None, "Please set argument: 'val'"
        
        self.count = val
        self.count += 1          # クラス変数（self.count）をカウントアップ


if __name__=="__main__":
    
    # 明示的に引数を与える場合
    instance1 = MyClass(val=1)
    print("instance1.count:{0}".format(instance1.count))
    
    # これ↓でも大丈夫
    instance2 = MyClass(2)
    print("instance2.count:{0}".format(instance2.count))
