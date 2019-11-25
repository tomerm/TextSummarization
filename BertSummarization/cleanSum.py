import os
import glob
import shutil

inPath = "/home/user/Summarization/Summarization/"
outPath = "/home/user/Summarization/Clean/"
count = 0
countWrong = 0

os.chdir(inPath)
for f in glob.glob("*"):
    count += 1
    wrongDoc = False
    prevHighlight = False
    fIn = inPath + f
    cont = []
    countHL = 0
    with open(fIn, 'r', encoding='UTF-8') as tc:
        for line in tc:
            cont.append(line.strip())
    tc.close()
    for i in range(len(cont)):
        if cont[i].find("@highlight") >= 0:
            if i == 0 or i == len(cont) - 1 or prevHighlight:
                wrongDoc = True
                break
            prevHighlight = True
            countHL += 1
        else:
            prevHighlight = False
    if not wrongDoc and countHL > 0:
        fOut = outPath + f
        shutil.copy(fIn, fOut)
    else:
        countWrong += 1
print ("Docs at all: %d, wrong docs: %d, copied: %d"%(count, countWrong, count-countWrong))