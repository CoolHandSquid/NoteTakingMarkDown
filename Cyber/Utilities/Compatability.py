#!/usr/bin/env python3
import os
import re

def getfilelist():
    filelist    = []
    for currentpath, folders, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.md'):
                filelist.append(os.path.join(currentpath, file))
    return filelist

def fileparse(file):
    openyaml    = False
    tagline     = False
    closeyaml   = False
    foldcongru  = True 
    with open(file) as f:
        contents    = f.readlines()
        firstline   = True
        for line in contents:
            if firstline == True:
                if re.match("^---.*", line):
                    openyaml    = True
                    firstline   = False
                    continue
                else:
                    break
            if tagline == False:
                if re.match("^tags:.*", line):
                    tagline = True
                    continue
                else:
                    continue
            if closeyaml == False:
                if re.match("^---.*", line):
                    closeyaml = True
                    continue
                else:
                    continue
            if foldcongru == True:
                if re.match("^#{2,6}[^#].*", line) and not re.match(".*[<][?][?][>].*", line):
                    return "{}: Found header without an openfold '<??>'".format(file)
                elif re.match("^#{1,6}[^#].*[<][?][?][>].*", line):
                    if re.match("^#{7,}.*", line):
                        return "{}: Headers go more than 6 deep".format(file)
                    foldcongru = False
                    continue
                else:
                    continue
            elif foldcongru == False:
                if re.match("<!----->.*", line):
                    foldcongru = True
                    continue
                elif re.match("^#{1,6}[^#].*[<][?][?][>].*", line):
                    break
                else:
                    continue
    if openyaml == True and tagline == True and closeyaml == True and foldcongru == True:
        return "{}: Pass".format(file) 
    else:
        if openyaml != True:
            return "{}: Missing openyaml".format(file)
        elif tagline != True:
            return "{}: Missing tagline 'tags:'".format(file)
        elif closeyaml != True:
            return "{}: Missing closeyaml".format(file)
        elif foldcongru != True:
            return "{}: Mismatched fold congruency '<??> and <!----->'".format(file)
        else:
            print("We should have never got here")


if __name__ == "__main__":
    for file in getfilelist():
        try:
            print(fileparse(file))
        except:
            print("{}: Failed to parse. Possible bad char (Often comes from copying rich text)".format(file))