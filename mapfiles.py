import os, sys, codecs

def mapfiles(filelist, proc):
    """ apply a proc to files in filelist.
        filelist: the url list of all files. like: "[D:\\proc\1.txt, D:\\proc\2.txt]"
        proc: a process that take content as argument then return the mapped content.
            the argument content is a list, contains all physical lines in a txt file.
    """

    for item in filelist:
        print(item)
        f = open(item, "r", encoding="utf8")
        content = f.readlines() # get a list of txt lines
        f.close

        modified = proc(content)

        f = open(item, "w", encoding="utf8")
        content = "".join(content) # convert list to str
        f.write(content)
        f.close

def prependsthtoyml(content):
    """ prepend a line with string into content. conent should be a list of lines.
    """
    for lineno, linecont in enumerate(content):
        if linecont.startswith("---"):
            content.insert(lineno+1, "slug: newly-added. congratulations! \n")
        else:
            pass
    return content

# test:  
inputdir = "D:\\Desk-Sync\\832_md-Blogger-tools\\md-blogger-tools\\proc\\"
files = os.listdir(inputdir)
files = [i for i in files if i.endswith("markdown")]
fileurls = [inputdir + str(filename) for filename in files]
print(files)
print(fileurls)
mapfiles(fileurls, prependsthtoyml)

