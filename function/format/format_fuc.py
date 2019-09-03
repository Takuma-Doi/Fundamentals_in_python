# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 23:41:56 2018

@author: d01tkum
"""

apple = 100
orange = 50
total = apple + orange

print("0: りんご：{}円, オレンジ：{}円, 合計：{}円".format(apple, orange, total))
print("1: りんご：{0}円, オレンジ：{1}円, 合計：{2}円".format(apple, orange, total))

lists = [apple, orange, total]
print("2: りんご：{0[0]}円, オレンジ：{0[1]}円, 合計：{0[2]}円".format(lists))

tuples = (apple, orange, total)
print("3: りんご：{0[0]}円, オレンジ：{0[1]}円, 合計：{0[2]}円".format(tuples))

dicts = {"apple":apple, "orange":orange, "total":total}
print("4: りんご：{0[apple]}円, オレンジ：{0[orange]}円, 合計：{0[total]}円".format(dicts))


# 2進数：Binary，8進数：Octal，10進数：Decimal，16進数：Hexadecimal
decimal = 120
print('5: {0}は2進数だと{0:b}、8進数だと{0:o}、10進数だと{0:d}、16進数だと{0:X}'.format(decimal))


# こんな書き方もできる
string1 = '左詰め'
string2 = '中央寄せ'
string3 = '右詰め'

print('6: {0:<10}'.format(string1))
print('7: {0:^10}'.format(string2))
print('8: {0:>10}'.format(string3))