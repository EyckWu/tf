#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

from tensorflow.examples.tutorials.mnist import input_data
import scipy.misc
import os

mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)

save_dir = 'MNIST_data/raw/'
if os.path.exists(save_dir) is False:
    os.mkdir(save_dir)

# 保存前20张图片
for i in range(20):
    # 第i张图片
    image_array = mnist.train.images[i, :]
    # 还原为28*28维的图像
    image_array = image_array.reshape(28, 28)
    # 保存文件格式 mnist_train_0.jpg
    filename = save_dir + 'mnist_train_%d.jpg' % i
    # 转换为图片，然后保存
    scipy.misc.toimage(image_array, cmin=0.0, cmax=1.0).save(filename)