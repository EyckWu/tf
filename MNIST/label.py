#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

from tensorflow.examples.tutorials.mnist import input_data
import numpy as np

# 读取MNIST中的数据集
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# 前20张训练图片的label
for i in range(20):
    # 得到ont-hot表示
    ont_hot_label = mnist.train.labels[i, :]
    # print(ont_hot_label)
    # 通过np.argmax获得原始的label
    label = np.argmax(ont_hot_label)
    print('mnist_train_%d.jpg label: %d' % (i, label))