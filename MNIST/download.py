#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# 查看训练数据的大小
print(mnist.train.images.shape)
print(mnist.train.labels.shape)

# 查看验证数据的大小
print(mnist.validation.images.shape)
print(mnist.validation.labels.shape)

# 查看测试数据的大小
print(mnist.test.images.shape)
print(mnist.test.labels.shape)