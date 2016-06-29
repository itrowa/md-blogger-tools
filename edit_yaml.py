# -*- coding: utf-8 -*- 
import os
import shutil

# the path to load files from
inputpath = r"C:\users\Rikka\Desktop\posts"
# the path to save files to
outputpath = r"C:\users\Rikka\Desktop\posts\new"

for fname in os.listdir(inputpath):
	f = open(os.path.join(inputpath, fname))
	
	g = open(os.path.join(outputpath, fname), 'w')
	for line in f.readlines():
		if '---' not in line:
			g.write(line)
	g.close()
	
	f.close()

