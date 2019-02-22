#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# x 为训练图像的占位符， y_为训练图像标签的占位符
x = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 10])

# 将单张图片从784维向量重新还原为28*28的矩阵图片
x_image = tf.reshape(x, [-1, 28, 28, 1])

