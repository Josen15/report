#!/usr/bin/env python
# -*- coding: utf-8 -*-

from splinter import Browser
import time
import random
browser=Browser('chrome')
url='http://admin2.okzaijia.com.cn/Account/login'
browser.visit(url)
browser.find_by_id('UserName').fill('101')
browser.find_by_id('Password').fill('123456')
browser.find_by_id('LoginOn').click()
time.sleep(2)

#browser.find_by_xpath("//tr/td/a[text()='KX160419104003163']").click()/td[4]/td[1]
#print browser.find_by_xpath("//tr/td/a[text()='KX160419104003163']").text
#n=browser.find_by_xpath("//tr/td/a[text()='KX160419104003163']").text
def a(m,n,d):
	c='http://admin2.okzaijia.com.cn/Task/MyTask?TaskType=%s&Status=%s'%(m,n)
	browser.visit(c)
	if browser.find_by_text(u"尾页"):
		browser.find_by_text(u"尾页").click()
		m="//tr/td/a[text()='%s']/../../td[4]"%d
		print browser.find_by_xpath(m).text
		n="//tr/td/a[text()='%s']/../../td[6]/ul/li/a"%d
		print n
		browser.find_by_xpath(n).click()
	else:
		pass
	#m="//tr/td/a[text()='%s']/../../td[4]"%d
	#print browser.find_by_xpath(m).text
	#if u'联系任务'==browser.find_by_xpath("//tr/td/a[text()='KX160419104003163']/../../td[4]").text:
	#	print u'通过'
	#else:
		#print 'false' 

a('7','1','KX160419104003163')