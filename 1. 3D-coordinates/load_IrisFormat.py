# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:14:04 2018

@author: takuma
"""

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import axes3d


def gen_3d_data(dataset):
    pca = PCA(n_components=3)
    return pca.fit_transform(dataset.data), dataset.target


def matplotlib_plt(XYZ, tgt, filename):
    fig = plt.figure()
    
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(XYZ[:,0], XYZ[:,1], XYZ[:,2], c=tgt/len(set(tgt)))
    #plt.savefig(filename)
    plt.show()
    
def main():
    iris_XYZ, iris_tgt = gen_3d_data(load_iris())
    
    print(iris_tgt)
    print(type(iris_tgt), iris_tgt.shape)
    matplotlib_plt(iris_XYZ, iris_tgt, "iris.png")
    

main()