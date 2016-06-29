# WARNING: deprecated
# 将某个目录下的所有的形如2014-0-02-file-name.markdown的文件的file-name部分插入到yml header的slug部分中:
# slug: file-name

import os, sys, codecs

ls = os.listdir("C:\\Users\\rikka\\Downloads\\proc")
ls = [i for i in ls if i.endswith("markdown")]
insertpoint = "date:"       # insert a new line after this line

for item in ls:
    ymlmarker = 0
    index = 0

    # 1st pass
    f = open(item, "r", encoding="utf8")
    contents = f.readlines()
    # print(contents)
    f.close

    for i, line in enumerate(contents):
        if line.startswith("---"):
            ymlmarker += 1
        if ymlmarker == 1 and line.startswith(insertpoint):
            index = i
        else:
            pass

    contents.insert(index+1, "slug: " + item[11:-9] + "\n")

    # 2nd pass
    f = open(item, "w", encoding="utf8")
    contents = "".join(contents)
    f.write(contents)
    f.close

def mapfiles(inputlist, proc):
    """ apply a proc to files in inputlist.
    """

    for item in inputlist:
        f = open(item, "r", encoding="utf8")
        content = f.readlines() # 一个list, 按行隔开
        f.close

        modified = proc(content)

        f = open(item, "w", encoding="utf8")
        f.write(contents)
        f.close

def prependsthtoyml(content):
    for lineno, linecont in enumerate(content):
        if linecont.startswith("---"):
            content.insert(lineno+1, "slug: newly-added. congratulations! \n")
        else:
            pass
    return content
