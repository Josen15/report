#!/usr/bin/env python
#coding:utf-8

from csv import reader
#读取csv文件
def getCsv(file_name):
	h=file(file_name,"r")
	n=reader(h)
	print n
	list=[]
	for x in n:
		list.append(x)
	a=list[1:]
	return a
getCsv(r'C:\\workspace\\n.csv')

