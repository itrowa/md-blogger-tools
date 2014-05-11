# -*- coding: utf-8 -*- 


# 删除md文件名中的时间并将时间移动到文件的yaml中
# 只能处理一个目录下的东西，还做不到子目录的递归修改
import os

dirpath = "C:\users\Rikka\Desktop\posts"
for fname in os.listdir(dirpath):
	fnamenew = fname[11:]
	fdate = fname[0:10]
	
	#open original to retrieve text, and write into a new file for insert date
	text = open(os.path.join(dirpath, fname))
	line = text.readlines()
	line.insert(3, 'date: ' + fdate + '\n')
	text.close()
	
	textnew = open(os.path.join(dirpath, fnamenew), 'w')
	textnew.writelines(line)
	textnew.close()
	
	