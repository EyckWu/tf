#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)