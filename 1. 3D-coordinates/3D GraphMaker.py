# -*- coding: utf-8 -*-
"""
Created on Sat May 19 19:44:28 2018

@author: dadad
"""
from mpl_toolkits.mplot3d import Axes3D   
import matplotlib.pyplot as plt 
import numpy as np
import math

fig = plt.figure() #プロット領域の作成
ax = fig.gca(projection='3d') #プロット中の軸の取得。gca は"Get Current Axes" の略。

x = np.arange(-20, 20, 0.05) # x点として[-2, 2]まで0.05刻みでサンプル
y = np.arange(-20, 20, 0.05) # y点として[-2, 2]まで0.05刻みでサンプル
x, y = np.meshgrid(x, y)  # 上述のサンプリング点(x,y)を使ったメッシュ生成

e = math.e

z = 1 / (1 + e**-y)
#z = np.exp(-(x**2 + y**2))  #exp(-(x^2+y^2))  を計算してzz座標へ格納する。
ax.set_zlim(0.0,1.0)
#ax.set_xlabel('X axis'); 
plt.tick_params(labelbottom='off')
#ax.set_ylabel('Y axis'); 
plt.tick_params(labelleft='off')
#ax.set_zlabel('Brightness')

ax.plot_wireframe(x, y, z, color='blue',linewidth=0.3) # ワイヤーフレームのプロット。linewidthは曲面のメッシュの線の太さ，をそれぞれ表す。

plt.show() # 絵の出力。