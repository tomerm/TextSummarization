import os
import glob
import json

rootPath = "/home/user/Summarization/DUC/ducAra/input/2007/"
storiesPath = rootPath + "stories"
fIn = rootPath + "sentences-json.txt"
fNames = []
cont = []
count = 0
fDoc = []

os.chdir(storiesPath)
for f in glob.glob("*"):
    fNames.append(f)
print ("Got names for %d files."%(len(fNames)))

with open(fIn, 'r', encoding='UTF-8') as tc:
    for line in tc:
        cont.append(line.strip())
tc.close()
print ("Read %d lines from file %s."%(len(cont), fIn))

for i in range(len(cont)):
    data = json.loads(cont[i], encoding="UTF-8")
    docs = data["documents"]
    for j in range(len(docs)):
        doc = docs[j]
        if doc["position"] == 0:
            if len(fDoc) > 0:
                fOut = rootPath + "results/" + fNames[count]
                f = open(fOut, "w", encoding="UTF-8")
                f.write("\n".join(fDoc))
                f.close()
                count += 1
            fDoc = []
        fDoc.append(doc["text"])
    if len(fDoc) > 0:
        fOut = rootPath + "results/" + fNames[count]
        f = open(fOut, "w", encoding="UTF-8")
        f.write("\n".join(fDoc))
        f.close()
        count += 1
print ("Saved %d documents."%(count))