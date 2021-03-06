#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 2-5-pandasReadSummarizer.py
# @Author: Redheat
# @Date  : 2018/1/23
# @Email : qjyyn@qq.com
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url,header=None, prefix="V")

#print head and tail of data frame
print(rocksVMines.head())
print(rocksVMines.tail())

#print summary of data frame
summary = rocksVMines.describe()
print(summary)