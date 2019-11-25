import os
import glob


fIn = "/home/user/BertSum/results/cnndm_step0.candidate"
fOut = "/home/user/BertSum/results/cnn_rouge3.candidate"
cont = []
with open(fIn, 'r', encoding='UTF-8') as tc:
    for line in tc:
        cont.append(line.strip().replace("<q>", " <eos>  "))
tc.close()
print ("Read %d lines from file %s."%(len(cont), fIn))

f = open(fOut, "w", encoding="UTF-8")
f.write("\n".join(cont))
f.close()