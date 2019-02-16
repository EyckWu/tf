#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))