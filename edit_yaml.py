# -*- coding: utf-8 -*- 
import os
import shutil

dirpath = r"C:\users\Rikka\Desktop\posts"
dirpathnew = r"C:\users\Rikka\Desktop\posts\new"

for fname in os.listdir(dirpath):
	f = open(os.path.join(dirpath, fname))
	
	g = open(os.path.join(dirpathnew, fname), 'w')
	for line in f.readlines():
		if '---' not in line:
			g.write(line)
	g.close()
	
	f.close()






# for fname in os.listdir(dirpath):
	# with open(fname, 'r') as f:
		# with open(os.path.join(dirpathnew,fname), 'w') as g:
			# for line in f.readlines():
				# if '---' not in line:             
					# g.write(line)
	# shutil.move(os.path.join(dirpathnew, fname), os.path.join(dirpath, fname))