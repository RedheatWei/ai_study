#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 2-1.py
# @Author: Redheat
# @Date  : 2018/1/23
# @Email : qjyyn@qq.com
import urllib2
import sys
target_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
data = urllib2.urlopen(target_url)

xList = []
labels = []
for line in data:
    row = line.strip().split(",")
    xList.append(row)

sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n')
sys.stdout.write("Number of Columns of Data = "+str(len(xList[1])))

