import os
import glob
import shutil

cnnPath = "/home/user/Summarization/cnn/"
sub = "stories"
curSub = ""
count = 0
countDir = 0
maxInDir = 10000

os.chdir(cnnPath + sub)
for f in glob.glob("*"):
    if count%maxInDir == 0:
        countDir += 1
        curSub = "%s%d"%(sub, countDir)
        os.makedirs(cnnPath + curSub, exist_ok=True)
        count = 0
    count += 1
    inPath = cnnPath + sub + "/" + f
    outPath = cnnPath + curSub + "/" + f
    shutil.copy(inPath, outPath)

